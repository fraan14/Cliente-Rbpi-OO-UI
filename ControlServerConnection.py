import sys 
import queue
import socket
from threading import Thread
import time
import json
import traceback

class ControlServerConnection:
    def __init__(self,colaSC, data = None):
        self.usrData = data
        self.serverSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = self.getServerInfo()
        self.colasServerControl = colaSC       # 0 mensajes para envio  / 1 mensajes para recepcion
        self.keepThreadRunning = True

        #Cuando se crea el objeto ya directamente arranca queriendo conectarse, de no ser posible lo informa por las colas de salida
        self.connection = False

    #main method, thread target.
    def runControlServerConnection(self):
        while not self.connection:
            self.makeConnection()                  #una vez que logra conectarse continua
            self.connection = self.checkResponse() #si no es una respuesta aceptable cierra el socket e intenta conectarse nuevamente
        self.serverSoc.settimeout(1)
        while self.keepThreadRunning:
            #miro si tengo algo para enviar y lo envio de ser necesario
            self.AlertaEnvioMensaje()
            #veo si llego algo y lo pongo en la cola de respuestas 
            self.AlertaRecepcionMensaje()

    def AlertaRecepcionMensaje(self):
        try:
            response = self.serverSoc.recv(4096)
            response = json.loads(response.decode('utf-8'))
            self.colasServerControl[1].put(response)
        except socket.timeout:
            pass
        except socket.error:
            #template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            #message = template.format(type(ex).__name__, ex.args)
            self.finalizacionSocket()
        except:
            pass

    def AlertaEnvioMensaje(self):
        # try:
        #     res = self.colasServerControl[0].get(timeout=1)
        #     self.serverSoc.sendall(json.dumps(res).encode())
        # except socket.error:
        #     return self.finalizacionSocket()
        # except:
        #     pass
        
        if(self.colasServerControl[0].empty() == False):
            try:
                res = self.colasServerControl[0].get(timeout=1)

                if(res == "FIN-EXECUTION"):
                    self.keepThreadRunning = False
                else:
                    self.serverSoc.sendall(json.dumps(res).encode())
            except socket.error:
                return self.finalizacionSocket()
            except:
                pass


    def checkResponse(self):
        response = self.serverSoc.recv(4096)
        response = json.loads(response)
        if(response["RESPUESTA"] != "CONEXION-ESTABLECIDA"):
            return self.finalizacionSocket()
        else:
            return True

    def makeConnection(self):
        while True:
            try:
                self.serverSoc.connect(self.server_address)
                return 0
            except:
                self.colasServerControl[1].put({"COMANDO":"FALLA-CONEXION-SRV","FROM":"LOCALHOST"})
                time.sleep(1)
                #self.serverSoc.close()
                #return -1
    
    def finalizacionSocket(self):
        self.colasServerControl[1].put({"COMANDO":"FALLA-CONEXION-SRV","FROM":"SERVER"})
        self.serverSoc.close()
        #exc_info = sys.exc_info()
        #traceback.print_exception(*exc_info)
        return False

    def getServerInfo(self):
        '''
        Este metodo toma la informacion del servidor de un archivo de configuracion.
        Por ahora esta hardcodeado.
        '''
        return ("172.0.0.5",16000) #TODO: Obtener desde un archivo de configuracion.

    #DEPRECATED
    def inicioSesion(self):
        data = self.getUserInfo()
        try:
            data = json.dumps(data)
            self.serverSoc.sendall(data.encode())
            response = self.serverSoc.recv(4096)
            response = json.loads(response.decode('utf-8'))
            self.colasServerControl[1].put(response)
            return response["RESPUESTA"]
        except:
            pass
            #exc_info = sys.exc_info()
            #traceback.print_exception(*exc_info)
            #self.finalizacionSocket()
    
    
    def getUserInfo(self):
        return {'COMANDO':'LOGIN',
                'NOMBRE':'RaspET2',
                'PASSWORD':'Rasp2',
                'HASH':'224-1',
                'DESTINO':'ETPB'}

if __name__ =="__main__":

    q1 = queue.Queue()
    q2 = queue.Queue()
    a1 = [q1,q2]
    app = ControlServerConnection(a1)
    app.runControlServerConnection()