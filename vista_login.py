import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import vista_frame_usuario
from  constantes import *

class VistaLogin(QtCore.QObject):

    Evento_Salir = QtCore.pyqtSignal()   #Emit SIGNAL
    Evento_Login = QtCore.pyqtSignal(str,str)   #Emit SIGNAL
    #Evento_Login = QtCore.pyqtSignal(str)   #Emit SIGNAL

    def __init__(self):
        super().__init__()
        self.MainWindow = uic.loadUi(Get_Path_UI() + "login_ui.ui")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(Get_Path_Imagenes() + "llamada_reposo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(self.icon)
        self.MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.label_mensaje.setText("Formulario de Login...")

        self.CargarEventosBotones()
        self.nombre_usuario = None
        self.contrasena_usuario = None

    def CargarEventosBotones(self):
        self.MainWindow.pushButton_salir.clicked.connect(self.Atencion_Evento_Salir)
        self.MainWindow.pushButton_login.clicked.connect(self.Atencion_Evento_Login)

    def Atencion_Evento_Salir(self):
        resultado = QtWidgets.QMessageBox.question(self.MainWindow, 'Salir...',"¿Seguro que quieres salir de la aplicación?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if resultado == QtWidgets.QMessageBox.Yes:
            self.MainWindow.hide()
            self.Evento_Salir.emit()   #Emit SIGNAL
        

    def Atencion_Evento_Login(self):
        self.nombre_usuario = str(self.MainWindow.lineEdit_nombre_usuario.text())
        self.contrasena_usuario = str(self.MainWindow.lineEdit_contrasena.text())
        if ((self.nombre_usuario != "") and (self.contrasena_usuario != "")):
            self.Evento_Login.emit(self.nombre_usuario,self.contrasena_usuario)   #Emit SIGNAL
            #self.Evento_Login.emit(self.nombre_usuario)   #Emit SIGNAL
        else:
            self.MainWindow.label_mensaje.show()
            self.MainWindow.label_mensaje.setText("Se se permiten datos en blanco !!!")
        

    def Set_Mensaje_Informacion(self,mensaje):
        self.MainWindow.lineEdit_nombre_usuario.setText("")
        self.MainWindow.lineEdit_contrasena.setText("")
        self.MainWindow.label_mensaje.setText(mensaje)