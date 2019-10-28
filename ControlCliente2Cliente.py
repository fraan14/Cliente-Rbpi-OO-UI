import sys 
import queue
import socket
from threading import Thread
import time
import json
import traceback

class Controlc2c:
    def __init__(self,colaC2C):
        self.intDict = dict()
        self.clientQueue = queue.Queue() #esta cola va a ser la encargada de pasar nuevas conexiones de clientes desde el thread del server
        self.ClienteControlServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ClienteControlServer.bind(("",15000))
        self.colaC2C = colaC2C


    #Module Work
    def runControlc2c(self):
        self.startServer()
        while True:
            self.verifyClientQueue()
            self.processIncomingMessages()
            self.processToSendMessages()

    def processIncomingMessages(self):
        toRem = []
        for key,value in self.intDict.items():
            try:
                data = value.recv(4096)
                if (data):
                    data = json.loads(data.decode())
                    toRet = {"COMANDO":data["COMANDO"],"FROM":key,"CONTENIDO":data}
                    print("INCOMING MESSAGE from "+key)
                    print(toRet)
                    self.colaC2C[1].put(toRet)
            except socket.timeout:
                pass
            except:
                toRem.append(key)
                exc_info = sys.exc_info()
                traceback.print_exception(*exc_info)
                print("ojo con esta")
        while (len(toRem)>0):
            self.intDict.pop(toRem.pop())
    
    def processToSendMessages(self):
        while (not self.colaC2C[0].empty()):
            try:
                msg = self.colaC2C[0].get(timeout=1)
                ip = msg["TO"]
                toSend = json.dumps(msg["CONTENIDO"]).encode()
                if (ip in self.intDict): 
                    self.intDict[ip].sendall(toSend) #aca tengo que verificar que exista la entrada en el diccionario sino tendria que crear un socket y crear la entrada.
                else:
                    s = self.crearEntradaConSocket(ip)
                    self.intDict[ip].sendall(toSend)
                    # if (s != None):
                    #     s.sendall(toSend)
                    #     s.close()
            except:
                exc_info = sys.exc_info()
                traceback.print_exception(*exc_info)
                print("errores muchacho")

    def crearEntradaConSocket(self,ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, 15000))
        except:
            print("error al querer conectar con el servidor del cliente destino")
            return None
        self.intDict.update({ip:s})
        return s

    def verifyClientQueue(self):
        while(not self.clientQueue.empty()):
            try:
                entry = self.clientQueue.get(timeout=0.5)
                self.intDict.update(entry)
            except:
                print("timeout")

    def removeConnectionFinCom(self,ip):
        # self.preRemoveThread = Thread(target=self.finalRemoveConection,args=(ip,))    #Client connection thread.
        # self.preRemoveThread.start()
        s = self.intDict.pop(ip)
        s.close()

    def finalRemoveConection(self,ip):
        time.sleep(1)
        self.intDict.pop(ip)

    #SERVER C2C
    def startServer(self):
        self.ccThread = Thread(target=self.serverWork,args=(self.clientQueue,))    #Client connection thread.
        self.ccThread.start()

    def serverWork(self,comqueue):
        self.ClienteControlServer.listen()
        while(True):
            c, addr = self.ClienteControlServer.accept()
            c.settimeout(1)
            comqueue.put({str(addr[0]):c}) #agrego un par ip:cliente en la cola.


if __name__ =="__main__":

    q1 = queue.Queue()
    q2 = queue.Queue()
    a1 = [q1,q2]
    app = Controlc2c(a1)
    app.runControlc2c()