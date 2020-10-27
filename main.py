from untitled import *
import sys,var,events

class Main(QTwidgets.QMainWindows):
    def __init__(self):
        super(Main, self).__init__()
        var.ui= Ui_MainWindows()
        var.ui.setupUi()
'''Conexion de eventos con objetos'''
        var.ui.bnCerrar.cliced.connect(events.eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())