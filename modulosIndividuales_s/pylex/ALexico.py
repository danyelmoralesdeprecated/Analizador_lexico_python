from Frase import *
from MsgHandler import *
from Analizador import *
from Iterador import *

class ALexico:
    __token = None
    __frase = Frase()
    __msgHandler = None
    __analizador = None
    __iterador = Iterador()
    __tipoDeLectura = 0
    
    def __init__(self):
        pass

    def leerCodigoFuente(self, tipo, texto):
        self.__tipoDeLectura = tipo
        if  tipo == 0:
            self.__analizador = Analizador("CONSOLE LINE")
            self.__setFrase(texto)
        elif tipo == 1:
            self.__analizador = Analizador("texto")
            self.__setPath(texto)
        else:
            print "Error"
            
    def getToken(self):
        if self.__tipoDeLectura == 1 and self.__frase.esFinDL():
            r = self.__leerLineaArchivo()
            if r == "EOF":
                return ""
            
        (self.__token, self.__msgHandler) = self.__analizador.generarToken()
        return self.__token.getToken()
    
    def getValLex(self):
        return self.__token.getLexema()
    
    def __setFrase(self, inputText):
        self.__frase.crearFrase(inputText)
        self.__analizador.crearAnalizador(self.__frase)
        
    def __setPath(self, path):
        self.__iterador.crear(path)
        self.__leerLineaArchivo()
        
    def __leerLineaArchivo(self):
        f = self.__iterador.getFrase()
        if f == "":
            return "EOF"
        else:
            self.__setFrase(f)

    def showMessages(self):
        return self.__msgHandler.getMsg()
        

if __name__ == '__main__':
       print "[+][About]: \n\tCreado por: Daniel Noe Vera Morales. \
                                \n\tEn Yucatan, Mexico.\
                                 \n\tEl 3 de Noviembre de 2013"

