
def generarEnvioMensaje(comando, ipDestino, contenido):
    toRet= {"COMANDO":comando,
            "TO":ipDestino,
            "CONTENIDO":contenido}
    return toRet

def generarMensajeLogin(nombre,password,destino="FRANCO",hassh="224-2"):
    toRet={"COMANDO":"LOGIN",
            "NOMBRE":nombre,
            "PASSWORD":password,
            "DESTINO":destino,
            "HASH":hassh
            }
    return toRet

def generarMensajeLogout():
    return {"COMANDO":"LOGOUT"}

def generarMensajeSolicitudCom():
    return {"COMANDO":"SOLICITUD-COM"}

def generarMensajeSolicitudComAceptada():
    return {"COMANDO":"SOLICITUD-COM-ACEPTADA"}

def generarMensajeSolicitudComRechazada():
    return {"COMANDO":"SOLICITUD-COM-RECHAZADA"}

def generarMensajeFinCom():
    return {"COMANDO":"FIN-COM"}