class Token:
    __lexema = ""
    __token  = ""
    __codeLineNumber = None
    
    def __init__(self):
        pass
        
    def crear(self, token, lexema, objLineNumber):
        self.__lexema = lexema
        self.__token = token
        self.__codeLineNumber = objLineNumber
        
    def getToken(self):
        return self.__token

    def getLexema(self):
        return self.__lexema

    def lineNumber(self):
        return self.__codeLineNumber
