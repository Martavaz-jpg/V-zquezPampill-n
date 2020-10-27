import sys

class Eventos():
    def Salir(self):
        ''' Modulo para cerrar el programa'''
        try:
            sys.exit()
        except Exception as error:
            print('Error % ' %str(error))