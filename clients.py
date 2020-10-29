import var

class Clientes():

    def validarDni(dni):
        '''Codigo que controla si el dni es correcto'''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni == len([n for n in dni if n in numeros])) and tabla[int(dni) % 23] == dig_control

        except:
            print('Error en el módulo de validación del DNI')
            return None




    def validoDni():
        try:
            '''muestra mensaje de dni valido'''
            dni=var.ui.leDni.text()
            if Clientes.validarDni(dni):
                var.ui.lbValidar.setStyleSheet('QLabel{color:green;}')
                var.ui.lbValidar.setText('V')
                var.ui.leDni.setText(dni.upper())
            else:
                var.ui.lbValidar.setStyleSheet('QLabel{color:red;}')
                var.ui.lbValidar.setText('X')
                var.ui.leDni.setText(dni.upper())

        except:
            print('ERROR modulo validar dni')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print('Has elegido femenino')
            if var.ui.rbtMasc.isChecked():
                print('Has elegido Masculino')
        except Exception as error:
            print('Error: %s')