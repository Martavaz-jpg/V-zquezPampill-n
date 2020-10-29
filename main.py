from ventana import *
import sys,var,events,clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui= Ui_venPrincipal()
        var.ui.setupUi(self)
        '''coleccion de datos'''
        var.rbtsex=(var.ui.rbtFem,var.ui.rbtMasc)
        '''
        Conexion de eventos con objetos
        estamos conectando el codigo con la interfaz gráfica
        '''
        var.ui.bnCerrar.clicked.connect(events.Eventos.Salir)
        var.ui.leDni.editingFinished.connect(clients.Clientes.validoDni)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window =  Main()
    window.show()
    sys.exit(app.exec())