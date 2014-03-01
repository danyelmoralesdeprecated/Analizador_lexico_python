class Iterador:
    __frase = ""
    __ruta = ""
    __generador = ""
    
    def __init__(self):
        pass

    def crear(self, path):
        self.__ruta = path
        self.__generador = self.procesar()
    
    def getFrase(self):
        self.__frase = self.__generador.next()
        return self.__frase 
        
    def procesar(self):
        ins = open(self.__ruta, "r" )
        
        for line in ins:
            yield line
        ins.close()
        
        yield ""
    
