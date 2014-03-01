class Frase:
    __largo = 0
    __frase = ""
    __isEOL = False
    __punteroDeFrase = 0
    
    def __init__(self):
        pass
    
    def crearFrase(self, inputText):
        self.__frase = inputText
        self.__largo = len(self.__frase)
        self.__isEOL = False
        self.__punteroDeFrase = 0

    def showFrase(self):
        return self.__frase
    
    def getLargo(self):
        return self.__largo

    def getChar(self, mode):
        char = '\0'
        if not self.__punteroDeFrase == len(self.__frase):
            if mode == 0:
                char = self.__frase[self.__punteroDeFrase]
            elif mode == 1:
                char = self.__frase[self.__punteroDeFrase]
                self.__punteroDeFrase +=1
            elif mode == 2:
                self.__punteroDeFrase -= 1  
            else:
                print "No se reconoce tipo de lectura."
        
        if char == '\0' or char == '\n':
            self.__isEOL = True
            
        return char

    def esFinDL(self):
        if self.__isEOL:
            return True
        else:
            return False
        
    
