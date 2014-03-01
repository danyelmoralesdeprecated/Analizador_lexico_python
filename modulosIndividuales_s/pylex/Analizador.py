from MsgHandler import *
from Token import *
from Biblioteca import *
from CodeLineNumber import *

class Analizador:
    __frase = None
    __token = Token()
    __msgHandler = MsgHandler()
    __biblioteca = Biblioteca()
    __codeLineNumber = CodeLineNumber()
    __error   = None
    __buffer  = None
    __simbolo = None
    __estado  = None

    def __init__(self, fileName):
        self.__msgHandler.setFileName(fileName)
        
    def crearAnalizador(self, frase):
        self.__frase = frase
        self.__error = False
        self.__buffer = ""
        self.__simbolo = ''
        self.__estado = 0
        self.__codeLineNumber.incrementar()
    
    def generarToken(self):
        self.__buffer = ""
        self.__estado = 0
        isToken = False
        isEOL = False
        self.__error = False
        
        while not (isToken or isEOL or self.__error):
            x = self.__frase.getChar(1)
            y = self.__frase.getChar(0)

            newChar = self.__biblioteca.clasificaChar(x)
            proximoChar = self.__biblioteca.clasificaChar(y)
            
            if self.__biblioteca.guardarChar(x, self.__estado):
                self.__buffer += x

            if  newChar == "fin":
                isEOL = True
  
            isToken = self.analizar(newChar, proximoChar)

        if self.__error:
            self.generarToken()
        
        return self.__token, self.__msgHandler
    
    def analizar(self, char, proximoChar):
        if self.__estado == 0:
            if char == "letra":
                self.__estado = 1
                if self.__reconocer(char, proximoChar, 2):
                    self.__tokenizar("t5")
                    return True
            
            elif char == "operador":
                self.__estado = 0
                self.__tokenizar("t3")
                return True
            
            elif char == "digito":
                self.__estado = 2
                if self.__reconocer(char, proximoChar, 1):
                    self.__tokenizar("t4")
                    return True
                
            elif char == "delimitador":
                self.__estado = 0
                self.__tokenizar("t2")
                return True
            
            elif char == "cadDel":
                self.__estado = 3
                if proximoChar == "fin":
                    self.error()
                    
            elif char == "espacio":
                self.estado = 0
                
            elif char == "fin":
                self.__tokenizar("t6")
            else:
                self.error()
                
        elif self.__estado == 1:
            if char == "letra" or char == "digito" or \
               self.__biblioteca.esCaracterEspecialAceptado(char):
                self.__estado = 1
                if self.__reconocer(char, proximoChar,2):
                    if self.__biblioteca.esReservado(self.__buffer):
                        self.__tokenizar("t1")
                    else:
                        self.__tokenizar("t5")
                    return True    
            else:
                self.error()
                
        elif self.__estado == 2:
            self.__estado = 2

            if char == '.':
                if not proximoChar == "digito":
                    self.error()
            else:
                if self.__reconocer(char, proximoChar,0):
                    self.__tokenizar("t4")
                    return True
                
        elif self.__estado == 3:
            self.__estado = 3
            
            if self.__reconocer(char, proximoChar, 3):
                self.__tokenizar("t4")
                return True
            elif proximoChar == "fin":
                self.error()
        else:
            pass

    def __reconocer(self, char, proxChar, mode):
        if mode == 0:
            if char == proxChar:
                return False
            else:
                return True
            
        elif mode == 1:
            if proxChar == ".":
                return False
            
        elif mode == 2:
            if self.__biblioteca.esCaracterEspecialAceptado(proxChar) \
               or proxChar == "digito" or proxChar == "letra":
                return False

        elif mode == 3:
            if char == "cadDel":
                return True
            else:
                return False
            
        return self.__reconocer(char, proxChar,0)

    def __tokenizar(self, item):
        self.__token.crear(
            self.__biblioteca.recorrerTablaDeTokens(item),
            self.__buffer,
            self.__codeLineNumber
            )

    def error(self):
        self.__error = True
        self.__msgHandler.generarMsgHandler("Error","01",self.__buffer, self.__codeLineNumber)
