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

        self.toRem = []


    #Module Work
    def runControlc2c(self):
        self.startServer()
        while True:
            self.verifyClientQueue()
            self.processIncomingMessages()
            self.processToSendMessages()

    def processIncomingMessages(self):
        for key,value in self.intDict.items():
            if(not key in self.toRem):
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
                    if(not key in self.toRem):
                        self.toRem.append(key)
                    exc_info = sys.exc_info()
                    traceback.print_exception(*exc_info)
                    print("ojo con esta")
        while (len(self.toRem)>0):
            self.intDict.pop(self.toRem.pop())
    
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
                if(msg["COMANDO"] == 'FIN-COM'):
                    self.finalRemoveConection(msg["TO"])
                
            except:
                exc_info = sys.exc_info()
                traceback.print_exception(*exc_info)
                print("[C2C]errores process To Send Messages")

    def crearEntradaConSocket(self,ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        try:
            s.connect((ip, 15000))
            s.settimeout(1)
            self.intDict.update({ip:s})
        except:
            print("error al querer conectar con el servidor del cliente destino")
            return None
        return s

    def verifyClientQueue(self):
        while(self.clientQueue.empty()== False):
            try:
                entry = self.clientQueue.get(timeout=0.5)
                self.intDict.update(entry)
            except:
                print("[C2C]timeout")

    def removeConnectionFinCom(self,ip):
        self.toRem.append(ip)
        # self.preRemoveThread = Thread(target=self.finalRemoveConection,args=(ip,))    #Client connection thread.
        # self.preRemoveThread.start()
        #s = self.intDict.pop(ip)
        #s.close()

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
            c.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            comqueue.put({str(addr[0]):c}) #agrego un par ip:cliente en la cola.


if __name__ =="__main__":

    q1 = queue.Queue()
    q2 = queue.Queue()
    a1 = [q1,q2]
    app = Controlc2c(a1)
    app.runControlc2c()