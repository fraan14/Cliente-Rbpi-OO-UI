import pyaudio
import socket
import audioop
import traceback
from threading import Thread
import time

class ControlVoiceStreaming:

    def __init__(self, ipHabilitadas):
        self.ipHabilitadas = ipHabilitadas
        self.udpCallback = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # lo envio por broadcast
        hostname = socket.gethostname() 
        print(hostname)
        self.IPAddr = socket.gethostbyname(hostname)
        print(self.IPAddr)
        self.pi = pyaudio.PyAudio()
        #print(self.pi.get_default_input_device_info())
        self.FORMAT = pyaudio.paInt16
        self.CHUNK = 2205
        self.CHANNELS = 1
        self.RATE = 44100
        self.streamInput = self.pi.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK,
                                  stream_callback=self.FuncionCall)
        self.streamInput.start_stream()

        self.stout = self.pi.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         output=True,
                         frames_per_buffer=self.CHUNK)

        #self.udpCallback.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Para habilitar el Broadcast
        TServer = Thread(name="T-VoiceStream",target=self.VoiceStream)
        TServer.start()

    def FuncionCall(self, in_data, frame_count, time_info, status):
        
        if(len(self.ipHabilitadas)>0):
            audio = in_data
            encSoundData = audioop.lin2alaw(audio, 2)
            tosend = bytearray()  # creo el paquete
            tosend.extend(encSoundData)  # le agrego el sonido
           
            for ip in self.ipHabilitadas:
                self.udpCallback.sendto(tosend, (ip,45000))
        return (in_data, pyaudio.paContinue)

    def VoiceStream(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.bind(('', 45000))
        silence = chr(0) * 2
        while True:
            try:
                udpData, addr = udp.recvfrom(self.CHUNK)
                #print(addr)
                if(self.IPAddr != addr):
                    soundData = audioop.alaw2lin(udpData, 2)   #audio a reproducir decodificado
                    self.stout.write(soundData, self.CHUNK)
                    free = self.stout.get_write_available()  # Esto es por si viene audio vacio
                    if free > self.CHUNK:            # Is there a lot of space in the buffer?
                        tofill = free - self.CHUNK
                        self.stout.write(silence * tofill)   # Fill it with silence
            except Exception :
               traceback.print_exc()

    def addIpToStream(self,ip):
        self.ipHabilitadas.append(ip)

    def removeIpToStream(self,ip):
        self.ipHabilitadas.remove(ip)

if __name__ =="__main__":
    app = ControlVoiceStreaming(["172.0.0.3"])
    