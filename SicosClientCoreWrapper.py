from PyQt5 import QtCore
from threading import Thread
import time
import queue
import SicosClientCore
import FormateadorAJson

class SicosClientCoreWrapper(QtCore.QObject):
    #server signals
    logueo_exitoso = QtCore.pyqtSignal(list)
    login_nuevo_usuario = QtCore.pyqtSignal(dict)
    logout = QtCore.pyqtSignal(dict)
    login_rechazado = QtCore.pyqtSignal()
    login_existente = QtCore.pyqtSignal()
    my_token = QtCore.pyqtSignal(str)

    #other client signals
    solicitud_com = QtCore.pyqtSignal(str)
    solicitud_com_aceptada = QtCore.pyqtSignal(str)
    solicitud_com_rechazada = QtCore.pyqtSignal(str)
    fin_com = QtCore.pyqtSignal(str)

    #disconected
    desconexion =QtCore.pyqtSignal()
    Running = True


    def __init__(self):
        super(SicosClientCoreWrapper,self).__init__()
        
        self.colaRecepcion = queue.Queue()
        self.core = SicosClientCore.SicosClientCore(self.colaRecepcion) #creo el objeto
        self.core.preInitComunication()            #inicio la comunicacion

        self.iniciarLectura = Thread(target=self.checkIncomingMessageQueue)
        self.iniciarLectura.start()

        #dat = FormateadorAJson.generarMensajeLogin("RaspET1","Rasp1")
        #dat = FormateadorAJson.generarEnvioMensaje("LOGIN","SERVER",dat)
        #print(dat)
        #self.enviarMensaje(dat)

    def enviarMensaje(self,msg):
        self.core.sendMessage(msg)
        #este mensaje debe estar formateado con el json {COMANDO:xxx , TO:xxxx, CONTENIDO:xxx }

    def checkIncomingMessageQueue(self):
        while self.Running:
            data = self.colaRecepcion.get()
            print("Cola Recepcion: ", data)
            if(data["COMANDO"] == "LOGUEO-EXITOSO"):
                if(data["CONTENIDO"]["CONTENIDO"]["USUARIOS"]==''):
                    self.logueo_exitoso.emit([])
                else:
                    self.logueo_exitoso.emit(data["CONTENIDO"]["CONTENIDO"]["USUARIOS"])
                self.my_token.emit(data["CONTENIDO"]["CONTENIDO"]["TOKEN"])
            if(data["COMANDO"] == "LOGIN-NUEVO-USUARIO"):
                self.login_nuevo_usuario.emit(data["CONTENIDO"]["CONTENIDO"]["USUARIOS"][0])
            if(data["COMANDO"] == "LOGOUT"):
                self.logout.emit(data["CONTENIDO"]["CONTENIDO"]["USUARIOS"][0])
            if(data["COMANDO"] == "LOGIN-RECHAZADO"):
                self.login_rechazado.emit()
            if(data["COMANDO"] == "LOGIN-EXISTENTE"):
                self.login_existente.emit()
            if(data["COMANDO"] == "DESCOENCTADO"):
                self.desconexion.emit()
            if(data["COMANDO"] == "SOLICITUD-COM"):
                self.solicitud_com.emit(data["FROM"])
            if(data["COMANDO"] == "SOLICITUD-COM-ACEPTADA"):
                self.solicitud_com_aceptada.emit(data["FROM"])
            if(data["COMANDO"] == "SOLICITUD-COM-RECHAZADA"):
                self.solicitud_com_rechazada.emit(data["FROM"])
            if(data["COMANDO"] == "FIN-COM"):
                self.fin_com.emit(data["FROM"])

    def finishExecution(self):
        self.Running = False

if __name__ == "__main__":
    rbpiSC = SicosClientCoreWrapper()
    