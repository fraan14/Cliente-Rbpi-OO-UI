import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#from PyQt5.QtWidgets import QMessageBox
#from PyQt5.QtWidgets import QApplication, QMessageBox
import vista_frame_usuario
import vista_login
import SicosClientCoreWrapper
import FormateadorAJson

class VistaPrincipal(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ui\\ppal_ui_1.ui", self)        
        
        self.obj_wrapper_sicos_client_core = SicosClientCoreWrapper.SicosClientCoreWrapper()
        #SIGNAL enviadas por el Wrapper provenientes del Servidor - Tema LOGIN    
        self.obj_wrapper_sicos_client_core.logueo_exitoso.connect(self.Evento_Logueo_Exitoso)           #devuelve list
        self.obj_wrapper_sicos_client_core.login_nuevo_usuario.connect(self.Evento_Login_Nuevo_Usuario) #devuelve dict
        self.obj_wrapper_sicos_client_core.logout.connect(self.Evento_Logout)                           #devuelve dict
        self.obj_wrapper_sicos_client_core.login_rechazado.connect(self.Evento_Login_Rechazado)         #devuelve nada
        self.obj_wrapper_sicos_client_core.login_existente.connect(self.Evento_Login_Existente)         #devuelve nada
        self.obj_wrapper_sicos_client_core.my_token.connect(self.Evento_My_Token)                       #devuelve str
        #SIGNAL enviadas por el Wrapper provenientes del Cliente - Tema COMUNICACION entre CLIENTES
        self.obj_wrapper_sicos_client_core.solicitud_com.connect(self.Evento_Solicitud_Com)                     #devuelve str
        self.obj_wrapper_sicos_client_core.solicitud_com_aceptada.connect(self.Evento_Solicitud_Com_Aceptada)   #devuelve str
        self.obj_wrapper_sicos_client_core.solicitud_com_rechazada.connect(self.Evento_Solicitud_Com_Rechazada) #devuelve str
        self.obj_wrapper_sicos_client_core.fin_com.connect(self.Evento_Fin_Com)                                 #devuelve str
        #SIGNAL enviadas por el Wrapper provenientes del Servidor - Tema DESCONEXION
        self.obj_wrapper_sicos_client_core.desconexion.connect(self.Evento_Desconectado)                        #devuelve nada

        
        #self.MainWindow = uic.loadUi("ui\\ppal_ui_1.ui")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("ui\\llamada_reposo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        self.CargarEventosBotones()
        
        self.obj_vista_login = vista_login.VistaLogin()
        self.obj_vista_login.Evento_Salir.connect(self.Evento_Salir_Login)
        self.obj_vista_login.Evento_Login.connect(self.Evento_Login_Login)
        self.cerrado_desde_ventana_login = False
        self.Iniciar_Ventana_login()


    def Iniciar_Ventana_login(self):
        self.obj_vista_login.MainWindow.show()

               
    def CargarEventosBotones(self):
        self.pushButton_10.clicked.connect(self.Evento_10) #Agregar Us. 1
        self.pushButton_11.clicked.connect(self.Evento_11) #Agregar Us. 2
        self.pushButton_12.clicked.connect(self.Evento_12) #Agregar Us. 3
        self.pushButton_13.clicked.connect(self.Evento_13) #Agregar Us. 4
        self.pushButton_14.clicked.connect(self.Evento_14) #Mensaje Llamada Entrante
        self.pushButton_15.clicked.connect(self.Evento_15) #Mensaje Llamada Aceptada
        self.pushButton_16.clicked.connect(self.Evento_16) #Mensaje Llamada Rechazada
        self.pushButton_17.clicked.connect(self.Evento_17)



    def Evento_10(self):
        print("Boton 10 - Agregar Usuario 1")
        nombre_usuario = "USUARIO-1"
        destino_usuario = "SIAG"
        dir_ip = "192.168.0.10"
        #frame_nuevo = vista_frame_usuario.Frame_Usuario(self.MainWindow.scrollAreaWidgetContents_3,nombre_usuario,destino_usuario)
        frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
        frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
        frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
        frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
        frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
        self.verticalLayout.insertWidget(0,frame_nuevo)

    def Evento_11(self):
        print("Boton 11 - Agregar Usuario 2")
        nombre_usuario = "USUARIO-2"
        destino_usuario = "COAA"
        dir_ip = "192.168.0.11"
        #frame_nuevo = vista_frame_usuario.Frame_Usuario(self.MainWindow.scrollAreaWidgetContents_3,nombre_usuario,destino_usuario)
        frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
        frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
        frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
        frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
        frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
        self.verticalLayout.insertWidget(0,frame_nuevo)        

    def Evento_12(self):
        print("Boton 12 - Agregar Usuario 3")
        nombre_usuario = "USUARIO-3"
        destino_usuario = "ESTT"
        dir_ip = "192.168.0.12"
        #frame_nuevo = vista_frame_usuario.Frame_Usuario(self.MainWindow.scrollAreaWidgetContents_3,nombre_usuario,destino_usuario)
        frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
        frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
        frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
        frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
        frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
        self.verticalLayout.insertWidget(0,frame_nuevo)        

    def Evento_13(self):
        print("Boton 13 - Agregar Usuario 4")
        nombre_usuario = "USUARIO-4"
        destino_usuario = "EEOA"
        dir_ip = "192.168.0.13"
        #frame_nuevo = vista_frame_usuario.Frame_Usuario(self.MainWindow.scrollAreaWidgetContents_3,nombre_usuario,destino_usuario)
        frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
        frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
        frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
        frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
        frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
        self.verticalLayout.insertWidget(0,frame_nuevo)
    
    #*************************
    #Mensajes entrante por RED
    #*************************
    def Evento_14(self):
        print("Boton 14 - Mensaje Entrante: LLAMADA ENTRANTE")
        dir_ip = "192.168.0.13"
        frame_usuario = self.Mover_Frame_Usuario_Top(dir_ip)
        if (frame_usuario != None):
            print("Usuario: ", frame_usuario.nombre_usuario)
            frame_usuario.Mensaje_Llamada_Entrante()


    def Evento_15(self):
        print("Boton 15 - Mensaje Entrante: LLAMADA ACEPTADA")
        #*************************
        dir_ip = "192.168.0.13"
        #*************************
        frame_usuario = self.Get_Frame_Usuario(dir_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Aceptada()        
    

    def Evento_16(self):
        print("Boton 16 - Mensaje Entrante: LLAMADA RECHAZADA")
        #*************************
        dir_ip = "192.168.0.13"
        #*************************
        frame_usuario = self.Get_Frame_Usuario(dir_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Rechazada()        
    

    def Evento_17(self):
        print("Boton 17")
        print("Cantidad Componentes del Layout: ",self.verticalLayout.count())


    def Mover_Frame_Usuario_Top(self,dir_ip):
        frame_usuario = self.Get_Frame_Usuario(dir_ip)
        if (frame_usuario != None):
            nombre_usuario = frame_usuario.nombre_usuario
            destino_usuario = frame_usuario.destino_usuario
            #Elimino Frame Usuario
            self.verticalLayout.removeWidget(frame_usuario)
            frame_usuario.deleteLater()
            #self.Eliminar_Frame_Usuario(dir_ip)
            #Agrego Frame Usuario
            frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
            frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
            frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
            frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
            frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
            self.verticalLayout.insertWidget(0,frame_nuevo)
            return(frame_nuevo)
        return(None)


    def Get_Frame_Usuario(self,dir_ip):
        for i in range(self.verticalLayout.count()):
            if (i <= self.verticalLayout.count()):
                item_layout = self.verticalLayout.itemAt(i)
                if item_layout is not None:
                    widget = item_layout.widget()
                    if widget is not None:
                        nombre_widget = widget.objectName()
                        if (nombre_widget.find("FRAME") != -1):
                            if (widget.Get_Usuario_IP() == dir_ip):
                                return(widget)
        return(None)



    def closeEvent(self, event):
        if (not self.cerrado_desde_ventana_login):
            resultado = QtWidgets.QMessageBox.question(self, 'Salir...',"¿Seguro que quieres salir de la aplicación?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if resultado == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:         
            event.accept()

    #*******************************************************************************
    #SEÑALES emitidas por la ventana de LOGIN
    #*******************************************************************************
    def Evento_Salir_Login(self):
        #self.obj_vista_login.MainWindow.hide()
        self.cerrado_desde_ventana_login = True
        self.close()



    def Evento_Login_Login(self,nombre_usuario,contrasena_usuario):
        datos = FormateadorAJson.generarMensajeLogin(nombre_usuario,contrasena_usuario)
        datos = FormateadorAJson.generarEnvioMensaje("LOGIN","SERVER",datos)
        print("")
        print ("MENSAJE A ENVIAR: ", datos)
        print("")
        self.obj_wrapper_sicos_client_core.enviarMensaje(datos)



    #*******************************************************************************
    #SEÑALES emitidas por un Usuario de "vista_frame_usuario" para llamar al WRAPPER
    #*******************************************************************************
    def Evento_Iniciar_Llamada(self,dir_ip):
        print("SIGNAL - INICIAR_LLAMADA: ", dir_ip)

        datos = FormateadorAJson.generarMensajeSolicitudCom()
        datos = FormateadorAJson.generarEnvioMensaje("SOLICITUD-COM",dir_ip,datos)
        print("")
        print ("MENSAJE A ENVIAR: ", datos)
        print("")
        self.obj_wrapper_sicos_client_core.enviarMensaje(datos)


    def Evento_Aceptar_Llamada(self, dir_ip):
        print("SIGNAL - ACEPTAR_LLAMADA: ", dir_ip)
        datos = FormateadorAJson.generarMensajeSolicitudComAceptada()
        datos = FormateadorAJson.generarEnvioMensaje("SOLICITUD-COM-ACEPTADA",dir_ip,datos)
        self.obj_wrapper_sicos_client_core.enviarMensaje(datos)


    def Evento_Cortar_Llamada(self,dir_ip):
        print("SIGNAL - CORTAR_LLAMADA: ", dir_ip)
        datos = FormateadorAJson.generarMensajeFinCom()
        datos = FormateadorAJson.generarEnvioMensaje("FIN-COM",dir_ip,datos)
        self.obj_wrapper_sicos_client_core.enviarMensaje(datos)


    def Evento_Rechazar_Llamada(self,dir_ip):
        print("SIGNAL -RECHAZAR_LLAMADA: ", dir_ip)
        datos = FormateadorAJson.generarMensajeSolicitudComRechazada()
        datos = FormateadorAJson.generarEnvioMensaje("SOLICITUD-COM-RECHAZADA",dir_ip,datos)
        self.obj_wrapper_sicos_client_core.enviarMensaje(datos)



    #********************************************************************
    #SEÑALES emitidas por el Wrapper
    #********************************************************************
    #SIGNAL enviadas por el Wrapper provenientes del Servidor - LOGIN
    def Evento_Logueo_Exitoso(self,lista_usuarios):
        print("LOGUEO EXITOSO")
        self.obj_vista_login.MainWindow.hide()
        self.Agregar_Clientes_Ala_Lista(lista_usuarios)

    def Evento_Login_Nuevo_Usuario(self,dict_usuario):
        print("NUEVO USUARIO")
        usuario_destino = dict_usuario['DESTINO']
        usuario_ip = dict_usuario['IP']
        usuario_nombre = dict_usuario['NOMBRE']
            
        frame_nuevo = vista_frame_usuario.Frame_Usuario(usuario_nombre,usuario_destino,usuario_ip)
        frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
        frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
        frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
        frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
        posicion = (self.verticalLayout.insertWidget.count() - 1)
        self.verticalLayout.insertWidget(posicion,frame_nuevo)


    def Evento_Logout(self,dict_usuario):
        print("LOGOUT")
        usuario_ip = dict_usuario['IP']
        frame_usuario = self.Get_Frame_Usuario(usuario_ip)
        if (frame_usuario != None):
            self.verticalLayout.removeWidget(frame_usuario)
            frame_usuario.deleteLater()



    def Evento_Login_Rechazado(self):
        print("LOGIN RECHAZADO")
        self.obj_vista_login.Set_Mensaje_Informacion("Usuario o Contraseña Incorrecto !!!")

    def Evento_Login_Existente(self):
        print("LLOGIN EXISTENTE")
        self.obj_vista_login.Set_Mensaje_Informacion("El Usuario ya esta conectado !!!")


    def Evento_My_Token(self,token):
        print("MY TOKEN")

    def Evento_Desconectado(self):
        print("DESCONECTADO")
        self.obj_vista_login.Set_Mensaje_Informacion("Error de coneccion al Servidor !!!")


    #SIGNAL enviadas por el Wrapper provenientes del Cliente - COMUNICACION entre CLIENTES
    def Evento_Solicitud_Com(self,usuario_ip):
        print("SOLICITUD COM")
        frame_usuario = self.Mover_Frame_Usuario_Top(usuario_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Entrante()


    def Evento_Solicitud_Com_Aceptada(self,usuario_ip):
        print("SOLICITUD COm ACEPTADA")
        frame_usuario = self.Get_Frame_Usuario(usuario_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Aceptada()        

    def Evento_Solicitud_Com_Rechazada(self,usuario_ip):
        print("SOLICITUD COm RECHAZADA")
        frame_usuario = self.Get_Frame_Usuario(usuario_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Rechazada()        

    def Evento_Fin_Com(self,usuario_ip):
        print("FIN COM")
        frame_usuario = self.Get_Frame_Usuario(usuario_ip)
        if (frame_usuario != None):
            frame_usuario.Mensaje_Llamada_Fin()


    #********************************************************************
    #Rutinas llamadas por Eventos que atajan las SEÑALES del WRAPPER
    #********************************************************************
    def Agregar_Clientes_Ala_Lista(self,lista_usuarios):
        #print()
        #print("Lista Usuarios: ", lista_usuarios)
        #print()
        for usuario in lista_usuarios:
            print(usuario)
            usuario_destino = usuario['DESTINO']
            usuario_ip = usuario['IP']
            usuario_nombre = usuario['NOMBRE']
            
            frame_nuevo = vista_frame_usuario.Frame_Usuario(usuario_nombre,usuario_destino,usuario_ip)
            frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
            frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
            frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
            frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
            self.verticalLayout.insertWidget(0,frame_nuevo)



    def Mover_Frame_Usuario_Top(self,dir_ip):
        frame_usuario = self.Get_Frame_Usuario(dir_ip)
        if (frame_usuario != None):
            nombre_usuario = frame_usuario.nombre_usuario
            destino_usuario = frame_usuario.destino_usuario
            #Elimino Frame Usuario
            self.verticalLayout.removeWidget(frame_usuario)
            frame_usuario.deleteLater()
            #self.Eliminar_Frame_Usuario(dir_ip)
            #Agrego Frame Usuario
            frame_nuevo = vista_frame_usuario.Frame_Usuario(nombre_usuario,destino_usuario,dir_ip)
            frame_nuevo.Evento_Aceptar_Llamada.connect(self.Evento_Aceptar_Llamada)
            frame_nuevo.Evento_Cortar_Llamada.connect(self.Evento_Cortar_Llamada)
            frame_nuevo.Evento_Iniciar_Llamada.connect(self.Evento_Iniciar_Llamada)
            frame_nuevo.Evento_Rechazar_Llamada.connect(self.Evento_Rechazar_Llamada)
            self.verticalLayout.insertWidget(0,frame_nuevo)
            return(frame_nuevo)
        return(None)


    def Get_Frame_Usuario(self,dir_ip):
        for i in range(self.verticalLayout.count()):
            if (i <= self.verticalLayout.count()):
                item_layout = self.verticalLayout.itemAt(i)
                if item_layout is not None:
                    widget = item_layout.widget()
                    if widget is not None:
                        nombre_widget = widget.objectName()
                        if (nombre_widget.find("FRAME") != -1):
                            if (widget.Get_Usuario_IP() == dir_ip):
                                return(widget)
        return(None)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj_vista_principal = VistaPrincipal()
    obj_vista_principal.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     try:
#         obj_vista_principal = VistaPrincipal()
#         obj_vista_principal.MainWindow.show()
#         app.exec_()
#     except Exception:
#         traceback.print_exc()
