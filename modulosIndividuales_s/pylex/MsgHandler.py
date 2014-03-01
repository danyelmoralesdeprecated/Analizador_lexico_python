class MsgHandler:
    __fileName = ""
    __codeLineNumber = None
    
    __errors = 0
    __warnings = 0
    __informational = 0
    __flag = False
    
    __msgs = []
    __errorList = {'01':'Token no admitido'}
    __warningList = {}
    __informationalList = {}    
    
    
    def __init__(self):
        pass
    
    def setFileName(self, fileName):
        self.__fileName = fileName

    def generarMsgHandler(self, tipo, codigo, lexema, cLN):
        if tipo == "Error":
            self.__errors += 1
            contenido = self.__errorList[codigo]
        elif tipo == "Warning":
            self.__warnings += 1
            contenido = self.__warningList[codigo]
        elif tipo == "Informational":
            self.__informational += 1
            contenido = self.__informationalList[codigo]
        else:
            contenido = "Mensaje desconocido"
            
        entrada = lexema
        numeroDeLinea = cLN.getCodeLineNumber()
        nombreArchivo = self.__fileName

        mensaje = "[%s] %s: '%s' "\
                  "en la linea '%d' "\
                  "de '%s'." % (tipo, contenido, entrada, numeroDeLinea, nombreArchivo)
        
        self.__addMsg(mensaje)
        self.__flag = True

    def __addMsg(self, mensaje):
        self.__msgs.append(mensaje)
        
    def getMsg(self):
        if not self.__flag:
            msg = "Proceso terminado con exito!"
            self.__addMsg(msg)

        
        return self.__msgs
