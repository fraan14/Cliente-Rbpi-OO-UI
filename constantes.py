REPOSO = 0
LLAMADA_ENTRANTE = 1
LLAMADA_SALIENTE = 2
CORTE = 3
USUARIO_LOCAL = 4
USUARIO_REMOTO = 5
PTT_ON = 6
PTT_OFF = 7
PATH_IMAGENES = "imagenes"
PATH_UI = "ui"
SISTEMA = "WINDOWS"   #WINDOWS o LINUX
DIRECTORIO_APP = "Cliente_Audio_Sicos"


def Get_Path_Imagenes():
    if (SISTEMA == "WINDOWS"):
        return(PATH_IMAGENES + "\\")
    else:
        return("/home/linaro/" + DIRECTORIO_APP + "/"+ PATH_IMAGENES + "/")


def Get_Path_UI():
    if (SISTEMA == "WINDOWS"):
        return(PATH_UI + "\\")
    else:
        return("/home/linaro/" + DIRECTORIO_APP + "/"+ PATH_UI + "/")
