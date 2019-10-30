import sys 
import socket
import queue
import time
import traceback
from threading import Thread
import ControlServerConnection
import ControlCliente2Cliente
import ControlVoiceStreaming
import json

class SicosClientCore:
    
    def __init__(self, respuestaQueue = None):
        
        #Variables de control
        self.logtry = False
        self.envioExterno = queue.Queue()      #para enviar al server
        if( respuestaQueue == None):
            self.recepcionExterna =  queue.Queue()  #para recibir del server
        else:
            self.recepcionExterna = respuestaQueue

        #csc
        self.qControlConServerRecepcion = queue.Queue() #cola para recepcion de mensajes de control
        self.qControlConServerEnvio = queue.Queue() #cola para envio de mensajes a traves del canal de control con el server
        self.aControlConserver = [self.qControlConServerEnvio,self.qControlConServerRecepcion]  #lista que agrupa las colas que interactuan con el modulo controlserverconnection.
        self.controlsc = ControlServerConnection.ControlServerConnection(self.aControlConserver)   #creo instancia de la clase csc.
        self.usuariosConectados = dict()    #este diccionario almacena pares {usuario:ip} de los conectados al sistema informados por csc.
        self.cscThread = None               #thread para el manejo de csc.

        #c2c
        self.c2cQRecepcion = queue.Queue()
        self.c2cQEnvio = queue.Queue()
        self.aC2Cliente = [self.c2cQEnvio,self.c2cQRecepcion]
        self.controlC2C = ControlCliente2Cliente.Controlc2c(self.aC2Cliente)
        self.c2cThread = None

        #Audio
        self.toStreamIps = []
        self.voicestreaming = ControlVoiceStreaming.ControlVoiceStreaming(self.toStreamIps)


    def preInitComunication(self):
        self.initThread = Thread(target=self.initComunication)
        self.initThread.start()

    def initComunication(self):
        while True:
            #self.checkModuloEnvio()
            if(self.cscThread == None):
                self.cscThread = Thread(target=self.controlsc.runControlServerConnection)
                self.cscThread.start()
            if(self.c2cThread == None):
                self.c2cThread = Thread(target=self.controlC2C.runControlc2c)
                self.c2cThread.start()
            
            
            #verifico si existen mensajes para mandar al server 
            self.checkModuloEnvio()
            #verifico si hay mensajes del servidor
            self.checkControlConServer()
            #verifico si hay mensajes de otros clientes.
            self.checkControlC2C()

    #---------------------------Modulos de envio y recepcion externos-------------------
    
    #recibo desde algun servidor
    def ModuloRecepcion(self, dato):
        self.recepcionExterna.put(dato) #escribe los mensjaes que llegan en la cola correspondiente de salida del core.
    
    #envio hacia algun servidor
    def ModuloEnvio(self,dato):
        if (dato["COMANDO"] == "LOGIN"):
            self.procesadorEnvioCsc(dato)
        elif(dato["COMANDO"] == "LOGOUT"):
            self.procesadorEnvioCsc(dato)                   #TODO: Eliminar diccionario de conectados.
        elif(dato["COMANDO"] == "SOLICITUD-COM"):
            self.procesadorEnvioc2c(dato)
        elif(dato["COMANDO"] == "SOLICITUD-COM-ACEPTADA"):  #TODO Verificar
            self.AgregarIpVS(dato["TO"])
            self.procesadorEnvioc2c(dato)
        elif(dato["COMANDO"] == "SOLICITUD-COM-RECHAZADA"):
            self.procesadorEnvioc2c(dato)        
        elif(dato["COMANDO"] == "FIN-COM"):                 #TODO Eliminar ip de lista de ips voip
            self.EliminarIpVS(dato["TO"])
            self.procesadorEnvioc2c(dato)
            #self.controlC2C.removeConnectionFinCom(dato["TO"]) NO ELIMINAR, elimina una vez que envio sino cierra el socket
    
    #la info tiene que venir en un diccionario.
    def checkModuloEnvio(self):
        while(not self.envioExterno.empty()):
            try:
                data = self.envioExterno.get(timeout=1)
                self.ModuloEnvio(data)
            except:
                exc_info = sys.exc_info()
                traceback.print_exception(*exc_info)
                print("[SCC]errores checkModuloEnvio")    #TODO: hacer excepcion si el json no viene serializado en string


    #----------------------------Metodos Control Voice Streaming ------------------------

    def AgregarIpVS(self,ip):
        #self.toStreamIps.append(ip)
        self.voicestreaming.addIpToStream(ip)

    def EliminarIpVS(self,ip):
        #self.toStreamIps.remove(ip)
        try:
            self.voicestreaming.removeIpToStream(ip)
        except:
            print("[SCC]ip: "+ip+" no esta en la lista para eliminar")

    #----------------------------Metodos Control Cliente 2 Cliente ----------------------

    def checkControlC2C(self):
        while(not self.aC2Cliente[1].empty()):
            try:
                data = self.aC2Cliente[1].get(timeout=1)
                self.procesadorRecepcionc2c(data)
            except:
                pass    #TODO: hacer excepcion si el json no viene serializado en string

    def procesadorRecepcionc2c(self,data):      #escribe como diccionario el resultado
        #print(data)
        #este metodo es el que termina informandole a la vista el mensaje, pero como ahora no hay vista este decide aceptar las coms
        msg = data
        if (msg["CONTENIDO"]["COMANDO"] == "SOLICITUD-COM"):
            pass
        if (msg["CONTENIDO"]["COMANDO"] == "SOLICITUD-COM-ACEPTADA"):
            self.AgregarIpVS(data["FROM"])
        if (msg["CONTENIDO"]["COMANDO"] == "SOLICITUD-COM-RECHAZADA"):
            self.controlC2C.removeConnectionFinCom(data["FROM"])
        if (msg["CONTENIDO"]["COMANDO"] == "FIN-COM"):
            self.EliminarIpVS(data["FROM"])
            self.controlC2C.removeConnectionFinCom(data["FROM"])
        self.ModuloRecepcion(msg)
        
    def procesadorEnvioc2c(self,data):
        try:
            #toEnv = json.dumps(env)
            self.aC2Cliente[0].put(data)
        except:
            pass
            #TODO: informar al superior que el mensaje esta mal formateado.

    #----------------------------Metodos Control Server Connection ----------------------
    def checkControlConServer(self):
        try:
            res = self.aControlConserver[1].get(timeout=1)      #veo si hay algo en la cola de recepcion de mensajes.
            self.procesadorRecepcionCsc(res)
        except socket.error:
            self.cscThread._stop()
            self.cscThread = None
            time.sleep(1)
        except Exception :
            pass
        # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        # message = template.format(type(ex).__name__, ex.args)
            #exc_info = sys.exc_info()
            #traceback.print_exception(*exc_info)
    
    #Escribe en la cola de envio del control server connection.
    def procesadorEnvioCsc(self, env):              #esta no es encesario que tenga TO porq es siempre hacia el servidor
        try:
            toEnv = env["CONTENIDO"]                                        
            self.aControlConserver[0].put(toEnv)
        except:
            pass
            #TODO: informar al superior que el mensaje esta mal formateado.
    
    def procesadorRecepcionCsc(self, res):
        if(res["RESPUESTA"]=="LOGUEO-EXITOSO"):
            self.procesarDiccionarioUsuarios(res["CONTENIDO"]["USUARIOS"])  #TODO: este debe generar señal de nuevos usuarios
        if(res["RESPUESTA"]=="LOGIN-NUEVO-USUARIO"):
            self.procesarNuevoUsuario(res["CONTENIDO"]["USUARIOS"])         #TODO: este debe generar señal de nuevo usuario
        if(res["RESPUESTA"]=="LOGOUT"):
            self.procesarBajaUsuario(res["CONTENIDO"]["USUARIOS"])          #TODO: este debe generar señal de usuario eliminado
        if(res["RESPUESTA"]=="LOGIN-RECHAZADO"):                            #TODO: este debe devolver el mensaje entero o una señal correspondiente
            pass
        if(res["RESPUESTA"]=="LOGIN-EXISTENTE"):                            #TODO: este debe devovler el mensaje entero o una señal correspondiente
            pass
        #lo dejamos igual que el de c2c
        toRet = {"COMANDO":res["RESPUESTA"],"FROM":"SERVER","CONTENIDO":res}
        self.ModuloRecepcion(toRet)

    def procesarDiccionarioUsuarios(self,dicc):
        #esto itera sobre una lista de diccionarios
        for usuario in dicc:
            usr = usuario["NOMBRE"]
            ip = usuario["IP"]
            self.usuariosConectados.update({ip:usr})
        print(self.usuariosConectados)
        
    def procesarNuevoUsuario(self,dicc):
        #se que es uno solo
        usr = dicc[0]["NOMBRE"]
        ip = dicc[0]["IP"]
        self.usuariosConectados.update({ip:usr})
        print(self.usuariosConectados)

    def procesarBajaUsuario(self,dicc):
        #se que es uno solo
        #usr = dicc[0]["NOMBRE"]
        ip = dicc[0]["IP"]
        self.usuariosConectados.pop(ip)
        print(self.usuariosConectados)

    
    def sendMessage(self,msg):
        self.envioExterno.put(msg)

if __name__ == "__main__":
    q1 = queue.Queue()
    q2 = queue.Queue()
    a1 = [q1,q2]
    rbpiSC = SicosClientCore()
    rbpiSC.initComunication()