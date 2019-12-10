
# Clase que represneta cada Frame con los botones y etiquetas que se va añadiento por cada cliente en la lista

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import threading
from  constantes import *
import time

class Frame_Usuario(QtWidgets.QFrame):

    #***************************************
    #SEÑALES (SIGNALS) que son generados/enviados al presionar sobre los botones
    #de LLAMADA, CORTE y PTT a la
    #***************************************
    Evento_Iniciar_Llamada = QtCore.pyqtSignal(str)   #Emit SIGNAL
    Evento_Aceptar_Llamada = QtCore.pyqtSignal(str)   #Emit SIGNAL
    Evento_Cortar_Llamada = QtCore.pyqtSignal(str)   #Emit SIGNAL
    Evento_Rechazar_Llamada = QtCore.pyqtSignal(str)   #Emit SIGNAL
    Evento_PPT_ON = QtCore.pyqtSignal(str)   #Emit SIGNAL
    Evento_PPT_OFF = QtCore.pyqtSignal(str)   #Emit SIGNAL

    def __init__(self,nombre_usuario,destino_usuario,dir_ip,tipo_usuario):
        #super().__init__(obj_widget)
        super().__init__()
        self.label_img_usuario = None
        self.label_nombre_usuario = None
        self.label_nombre_destino = None
        self.pushButton_img_llamada = None
        self.pushButton_img_llamada_corte = None
        self.nombre_usuario = nombre_usuario
        self.destino_usuario = destino_usuario
        self.dir_ip = dir_ip
        self.tipo_usuario = tipo_usuario
        self.usuario_corto_comunicacion = None     #se utiliza para saber quien es el que corta la comunicacion si el usuario local o el corte de comunicacion proviene del usuario remoto, se utilia cuando se procesa el diagrama de estados   
        #El estado de la llamada se tiene en cuenta cuando se utiliza el protocolo de establecimiento 
        #de una comunicacion entre los clientes, si se trabaja con PTT no se tiene en cuenta
        self.estado_llamada = REPOSO   #REPOSO,LLAMADA_ENTRANTE,LLAMADA_SALIENTE,CORTE
        self.objThread_llamada = None
        
        self.icon_LLAMADA_REPOSO = QtGui.QIcon()
        self.icon_LLAMADA_REPOSO.addPixmap(QtGui.QPixmap(PATH + "\\llamada_reposo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_ENTRANTE_ON = QtGui.QIcon()
        self.icon_LLAMADA_ENTRANTE_ON.addPixmap(QtGui.QPixmap(PATH + "\\llamada_entrante_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_LLAMADA_ENTRANTE_OFF = QtGui.QIcon()
        self.icon_LLAMADA_ENTRANTE_OFF.addPixmap(QtGui.QPixmap(PATH + "\\llamada_entrante_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_SALIENTE_ON = QtGui.QIcon()
        self.icon_LLAMADA_SALIENTE_ON.addPixmap(QtGui.QPixmap(PATH + "\\llamada_saliente_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_LLAMADA_SALIENTE_OFF = QtGui.QIcon()
        self.icon_LLAMADA_SALIENTE_OFF.addPixmap(QtGui.QPixmap(PATH + "\\llamada_saliente_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_CORTE = QtGui.QIcon()
        self.icon_LLAMADA_CORTE.addPixmap(QtGui.QPixmap(PATH + "\\llamada_corte.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_MINICORTE = QtGui.QIcon()
        self.icon_LLAMADA_MINICORTE.addPixmap(QtGui.QPixmap(PATH + "\\llamada_corte.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_PTT_ON = QtGui.QIcon()
        self.icon_LLAMADA_PTT_ON.addPixmap(QtGui.QPixmap(PATH + "\\llamada_ptt_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon_LLAMADA_PTT_OFF = QtGui.QIcon()
        self.icon_LLAMADA_PTT_OFF.addPixmap(QtGui.QPixmap(PATH + "\\llamada_ptt_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.ArmarContenidoFrame()


    def ArmarContenidoFrame(self):
        #Parametros del FRAME
        self.setEnabled(True)
        self.setMinimumSize(QtCore.QSize(0, 81))
        self.setMaximumSize(QtCore.QSize(16777215, 81))
        self.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setObjectName("FRAME")
        
        #Etiqueta NOMBRE DEL USUARIO
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_nombre_usuario = QtWidgets.QLabel(self)
        self.label_nombre_usuario.setGeometry(QtCore.QRect(82, 19, 141, 21))
        self.label_nombre_usuario.setFont(font)
        self.label_nombre_usuario.setText(self.nombre_usuario)
        self.label_nombre_usuario.setObjectName("label_1")

        #Etiqueta DESTINO DEL USUARIO
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_nombre_destino = QtWidgets.QLabel(self)
        self.label_nombre_destino.setGeometry(QtCore.QRect(82, 42, 51, 21))
        self.label_nombre_destino.setFont(font)
        self.label_nombre_destino.setText(self.destino_usuario)
        self.label_nombre_destino.setObjectName("label_2")

        #Etiqueta IMAGEN de la PERSONA O DESTINO
        self.label_img_usuario = QtWidgets.QLabel(self)
        self.label_img_usuario.setGeometry(QtCore.QRect(9, 8, 65, 65))
        self.label_img_usuario.setText("")
        if (self.tipo_usuario == "PTT"):
            self.label_img_usuario.setPixmap(QtGui.QPixmap("imagenes\\usuario_pc.png"))  #Modificar para Persona o Pollux o Dispositivo al eq de rf
        else:   
            self.label_img_usuario.setPixmap(QtGui.QPixmap("imagenes\\usuario_persona.png"))  #Modificar para Persona o Pollux o Dispositivo al eq de rf

        self.label_img_usuario.setScaledContents(True)
        self.label_img_usuario.setObjectName("label_12")
       
        #Etiqueta IMAGEN LLAMADA
        self.pushButton_img_llamada = QtWidgets.QPushButton(self)
        self.pushButton_img_llamada.setGeometry(QtCore.QRect(261, 20, 44, 44))
        self.pushButton_img_llamada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_img_llamada.setToolTip("")
        self.pushButton_img_llamada.setAutoFillBackground(False)
        self.pushButton_img_llamada.setStyleSheet("border-style: outset;")
        self.pushButton_img_llamada.setText("")
        self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_REPOSO)
        self.pushButton_img_llamada.setIconSize(QtCore.QSize(44, 44))
        self.pushButton_img_llamada.setCheckable(False)
        self.pushButton_img_llamada.setAutoDefault(False)
        self.pushButton_img_llamada.setDefault(False)
        self.pushButton_img_llamada.setFlat(False)
        self.pushButton_img_llamada.setObjectName("pushButton_1")
        if (self.tipo_usuario == "PTT"):
            self.pushButton_img_llamada.hide()

        #Etiqueta IMAGEN PTT
        self.pushButton_img_PTT = QtWidgets.QPushButton(self)
        self.pushButton_img_PTT.setGeometry(QtCore.QRect(261, 20, 44, 44))
        self.pushButton_img_PTT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_img_PTT.setToolTip("")
        self.pushButton_img_PTT.setAutoFillBackground(False)
        self.pushButton_img_PTT.setStyleSheet("border-style: outset;")
        self.pushButton_img_PTT.setText("")
        self.pushButton_img_PTT.setIcon(self.icon_LLAMADA_PTT_OFF)
        self.pushButton_img_PTT.setIconSize(QtCore.QSize(44, 44))
        self.pushButton_img_PTT.setCheckable(False)
        self.pushButton_img_PTT.setAutoDefault(False)
        self.pushButton_img_PTT.setDefault(False)
        self.pushButton_img_PTT.setFlat(False)
        self.pushButton_img_PTT.setObjectName("pushButton_PTT")
        if (not (self.tipo_usuario == "PTT")):
            self.pushButton_img_PTT.hide()


        #Etiqueta IMAGEN LLAMADA CORTE 
        self.pushButton_img_llamada_minicorte = QtWidgets.QPushButton(self)
        #self.pushButton_img_llamada_minicorte.setEnabled(True)
        self.pushButton_img_llamada_minicorte.setGeometry(QtCore.QRect(306, 52, 25, 25))
        self.pushButton_img_llamada_minicorte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_img_llamada_minicorte.setToolTip("")
        self.pushButton_img_llamada_minicorte.setAutoFillBackground(False)
        self.pushButton_img_llamada_minicorte.setStyleSheet("border-style: outset;")
        self.pushButton_img_llamada_minicorte.setText("")
        self.pushButton_img_llamada_minicorte.setIcon(self.icon_LLAMADA_CORTE)
        self.pushButton_img_llamada_minicorte.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_img_llamada_minicorte.setCheckable(False)
        self.pushButton_img_llamada_minicorte.setAutoDefault(False)
        self.pushButton_img_llamada_minicorte.setDefault(False)
        self.pushButton_img_llamada_minicorte.setFlat(False)
        self.pushButton_img_llamada_minicorte.setObjectName("pushButton_2")        
        self.pushButton_img_llamada_minicorte.hide()

        self.pushButton_img_llamada.clicked.connect(self.Atencion_Evento_Llamada)
        self.pushButton_img_llamada_minicorte.clicked.connect(self.Atencion_Evento_Llamada_Corte)
        self.pushButton_img_PTT.pressed.connect(self.Atencion_Evento_PTT_ON)
        self.pushButton_img_PTT.released.connect(self.Atencion_Evento_PTT_OFF)



    #Crear Thread para cambiar el estado del boton correspondiente a la llamada
    #estados posible: REPOSO , LLAMADA_ENTRANTE , LLAMADA_SALIENTE , CORTE, PTT_ON, PTT_OFF
    def Atencion_Evento_Llamada (self):
        #print("Boton LLAMADA (usuario): ", self.nombre_usuario)
        if (self.estado_llamada == REPOSO):
            print("Boton LLAMADA (usuario): ", self.nombre_usuario)
            estado_nuevo = LLAMADA_SALIENTE
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)
        elif (self.estado_llamada == CORTE):
            print("Boton LLAMADA (usuario): ", self.nombre_usuario)
            estado_nuevo = REPOSO
            self.usuario_corto_comunicacion = USUARIO_LOCAL
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)
        elif (self.estado_llamada == LLAMADA_ENTRANTE):
            print("Boton LLAMADA (usuario): ", self.nombre_usuario)
            estado_nuevo = CORTE
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)

            
    def Atencion_Evento_Llamada_Corte(self):
        #print("Boton Mini CORTE (usuario): ", self.nombre_usuario)
        if (self.estado_llamada == LLAMADA_SALIENTE):
            print("Boton Mini CORTE (usuario): ", self.nombre_usuario)
            estado_nuevo = REPOSO
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)
        elif (self.estado_llamada == LLAMADA_ENTRANTE):
            print("Boton Mini CORTE (usuario): ", self.nombre_usuario)
            estado_nuevo = REPOSO
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)


    def Atencion_Evento_PTT_ON(self):
        self.pushButton_img_PTT.setIcon(self.icon_LLAMADA_PTT_ON)
        QtWidgets.QApplication.processEvents()
        self.Evento_PPT_ON.emit(self.dir_ip)   #Emit SIGNAL


    def Atencion_Evento_PTT_OFF(self):
        self.pushButton_img_PTT.setIcon(self.icon_LLAMADA_PTT_OFF)
        QtWidgets.QApplication.processEvents()
        self.Evento_PPT_OFF.emit(self.dir_ip)   #Emit SIGNAL



    #***************************************
    #Verificar todos estos cambios de estado
    #***************************************
    #REPOSO , LLAMADA_SALIENTE
    #CORTE , REPOSO
    #LLAMADA_ENTRANTE , CORTE

    #LAMADA_SALIENTE , REPOSO
    #LLAMADA_ENTRANTE , REPOSO
    def Procesar_Cambio_Estado(self,estado_actual,estado_nuevo):
        if ((estado_actual == REPOSO) and (estado_nuevo == LLAMADA_SALIENTE)):
            self.estado_llamada = LLAMADA_SALIENTE
            self.pushButton_img_llamada_minicorte.show()
            QtWidgets.QApplication.processEvents()
            self.Activar_Blink_Llamada()
            self.Evento_Iniciar_Llamada.emit(self.dir_ip)   #Emit SIGNAL

        elif ((estado_actual == CORTE) and (estado_nuevo == REPOSO)):
            self.estado_llamada = REPOSO
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_REPOSO)
            QtWidgets.QApplication.processEvents()
            if (self.usuario_corto_comunicacion == USUARIO_LOCAL):
                self.Evento_Cortar_Llamada.emit(self.dir_ip)   #Emit SIGNAL

        elif ((estado_actual == LLAMADA_ENTRANTE) and (estado_nuevo == CORTE)):
            self.estado_llamada = CORTE
            #Parar Blink: al cambiar estado_llamada de estado distinto de LLAMADA_SALIENTE y LLAMADA_ENTRANTE
            #directamente el Thread ya no hace Blink de imagen y termina
            self.pushButton_img_llamada_minicorte.hide()
            QtWidgets.QApplication.processEvents()
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_CORTE)
            QtWidgets.QApplication.processEvents()
            self.Evento_Aceptar_Llamada.emit(self.dir_ip)   #Emit SIGNAL

        elif ((estado_actual == LLAMADA_SALIENTE) and (estado_nuevo == REPOSO)):
            self.estado_llamada = REPOSO
            #Parar Blink: al cambiar estado_llamada de estado distinto de LLAMADA_SALIENTE y LLAMADA_ENTRANTE
            #directamente el Thread ya no hace Blink de imagen y termina
            self.pushButton_img_llamada_minicorte.hide()
            QtWidgets.QApplication.processEvents()
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_REPOSO)
            QtWidgets.QApplication.processEvents()
            self.Evento_Cortar_Llamada.emit(self.dir_ip)   #Emit SIGNAL

        elif ((estado_actual == LLAMADA_ENTRANTE) and (estado_nuevo == REPOSO)):
            self.estado_llamada = REPOSO
            #Parar Blink: al cambiar estado_llamada de estado distinto de LLAMADA_SALIENTE y LLAMADA_ENTRANTE
            #directamente el Thread ya no hace Blink de imagen y termina
            self.pushButton_img_llamada_minicorte.hide()
            QtWidgets.QApplication.processEvents()
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_REPOSO)
            QtWidgets.QApplication.processEvents()
            self.Evento_Rechazar_Llamada.emit(self.dir_ip)   #Emit SIGNAL

        elif ((estado_actual == REPOSO) and (estado_nuevo == LLAMADA_ENTRANTE)):
            self.estado_llamada = LLAMADA_ENTRANTE
            self.pushButton_img_llamada_minicorte.show()
            QtWidgets.QApplication.processEvents()
            self.Activar_Blink_Llamada()

        elif ((estado_actual == LLAMADA_SALIENTE) and (estado_nuevo == CORTE)):
            self.estado_llamada = CORTE
            #Parar Blink: al cambiar estado_llamada de estado distinto de LLAMADA_SALIENTE y LLAMADA_ENTRANTE
            #directamente el Thread ya no hace Blink de imagen y termina
            self.pushButton_img_llamada_minicorte.hide()
            QtWidgets.QApplication.processEvents()
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_CORTE)
            self.pushButton_img_llamada.show()
            QtWidgets.QApplication.processEvents()
            #La logina se encarga de establecer la comunicacion VoIP y comenzar a enviar paquetes

        elif ((estado_actual == LLAMADA_SALIENTE) and (estado_nuevo == REPOSO)):
            self.estado_llamada = REPOSO
            #Parar Blink: al cambiar estado_llamada de estado distinto de LLAMADA_SALIENTE y LLAMADA_ENTRANTE
            #directamente el Thread ya no hace Blink de imagen y termina
            self.pushButton_img_llamada_minicorte.hide()
            QtWidgets.QApplication.processEvents()
            self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_REPOSO)
            QtWidgets.QApplication.processEvents()
            #La logina se encarga de establecer la comunicacion VoIP y comenzar a enviar paquetes



    def Activar_Blink_Llamada(self):
        self.objThread_llamada = threading.Thread(target=self.Control_Llamada)
        self.objThread_llamada.start()


    def Control_Llamada(self):
        #estados posible: REPOSO , LLAMADA_ENTRANTE , LLAMADA_SALIENTE , CORTE        
        bandera = False
        salir = False
        while (not salir):
            if (self.estado_llamada == LLAMADA_SALIENTE):
                if (bandera):
                    bandera = False
                    self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_SALIENTE_OFF)
                    QtWidgets.QApplication.processEvents()
                else:
                    bandera = True
                    self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_SALIENTE_ON)
                    QtWidgets.QApplication.processEvents()
            elif (self.estado_llamada == LLAMADA_ENTRANTE):
                if (bandera):
                    bandera = False 
                    self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_ENTRANTE_OFF)
                    QtWidgets.QApplication.processEvents()                
                else:
                    bandera = True
                    self.pushButton_img_llamada.setIcon(self.icon_LLAMADA_ENTRANTE_ON)
                    QtWidgets.QApplication.processEvents()                
            else:            
                salir = True
            if (not salir):
                time.sleep(0.25)            


    def Get_Usuario_IP(self):
        return self.dir_ip


    #*******************************************************************************
    #METODOS invocados al llegar mensajeria por la RED: proveniente del Wrapper
    #*******************************************************************************
    def Mensaje_Llamada_Entrante(self):  #Metodo invocado al llegar mensajeria por la RED: Llamada Entrante
        if (self.estado_llamada == REPOSO):
            estado_nuevo = LLAMADA_ENTRANTE
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)


    def Mensaje_Llamada_Aceptada(self):  #Metodo invocado al llegar mensajeria por la RED: Llamada Aceptada
        if (self.estado_llamada == LLAMADA_SALIENTE):
            estado_nuevo = CORTE
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)

   
    def Mensaje_Llamada_Rechazada(self):  #Metodo invocado al llegar mensajeria por la RED: Llamada Rechazada 
        if (self.estado_llamada == LLAMADA_SALIENTE):
            estado_nuevo = REPOSO
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)


    def Mensaje_Llamada_Fin(self):  #Metodo invocado al llegar mensajeria por la RED: Llamada Fin 
        if (self.estado_llamada == CORTE):
            estado_nuevo = REPOSO
            self.usuario_corto_comunicacion = USUARIO_REMOTO
            self.Procesar_Cambio_Estado(self.estado_llamada,estado_nuevo)
