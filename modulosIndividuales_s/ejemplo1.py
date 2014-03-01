import sys
sys.path.append("pylex/")
from ALexico import ALexico

class ejemplo1:
       analizadorLexico1 = ALexico()
       
       def __init__(self):
              self.actions()
              
       def actions(self):
              isCorrect = False
              while (not isCorrect):
                     print("A) - Desde Archivo\nB) - Desde consola")
                     opc = raw_input("> ").upper()
                     
                     if (opc == 'A' or opc == 'B'):
                            self.readText(opc)
                            isCorrect = True
                     else:
                            print("Incorrect option.\n")

              self.simular()
              print self.analizadorLexico1.showMessages()
              
       def readText(self, opc):
              inText = raw_input("input>")
              if (opc == 'A'):
                     opc = 1
              elif (opc == 'B'):
                     opc = 0
              self.analizadorLexico1.leerCodigoFuente(opc, inText)
              
       def simular(self):
              isEndOfLine = False;
              while(not isEndOfLine):
                     token = self.analizadorLexico1.getToken()
                     if token == "":
                            isEndOfLine = True
                     else:
                            print "*********************************************"
                            print "Token: " + str(token)
                            print "  Lexema: " + str(self.analizadorLexico1.getValLex())
              
if __name__ == '__main__':
       objMain = ejemplo1()
