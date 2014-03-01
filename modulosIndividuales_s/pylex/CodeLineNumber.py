class CodeLineNumber:
    __codeLineNumber = 0
    
    def __init__(self):
        pass
    def incrementar(self):
        self.__codeLineNumber += 1

    def getCodeLineNumber(self):
        return self.__codeLineNumber
    
