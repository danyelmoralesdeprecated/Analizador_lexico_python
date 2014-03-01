class Biblioteca:
    __reserved = ['int','float','decimal','cat','end', 'maulla'] 
    __delims = [';', ',', '[', ']']
    __operador = ['-', '+', '/', '*', '=']
    __idCaracterEspecial = ['_', '@']
    __tokenValido = {'t1':"resrv",
                     't2':"delim",
                     't3':"opera",
                     't4':"const",
                     't5':"id",
                     't6':""}

    def __init__(self):
        pass
    
    def guardarChar(self, newChar, estado):
        if estado == 3 and newChar == ' ':
            return True
        elif not (newChar == ' ' or newChar == '\0'):
            return True
        else:
            return False
        
    def esChar(self, char):
        if char.isalpha() and (char != '\'' or char != '\"'):
            return True
        else:
            return False
        
    def esReservado(self, sch):
        for reservado in self.__reserved:
            if sch == reservado:
                return True
                break
        return False
    
    def esDelim(self, sch):
        for delimitador in self.__delims:
            if sch == delimitador:
                return True
                break
        return False
        
    def esOperador(self, sch):
        for operador in self.__operador:
            if sch == operador:
                return True
                break
        return False
    
    def esCaracterEspecialAceptado(self, sch):
        for caracterEspecial in self.__idCaracterEspecial:
            if sch == caracterEspecial:
                return True
                break
        return False
    
    def clasificaChar(self, char):
        if self.esChar(char):
            return "letra"
                
        elif self.esOperador(char):
            return "operador"

        elif char.isdigit():
            return "digito"
        
        elif self.esDelim(char):
            return "delimitador"
            
        elif char == '\"' or char == '\'':
            return "cadDel"

        elif char == ' ':
            return "espacio"
        
        elif char == '\0' or char == '\n':
            return "fin"
        else:
            return char
        
    def recorrerTablaDeTokens(self, item):
        return self.__tokenValido[item]
    
