from PyQt5 import uic, QtWidgets

def main ():
    for i in range (100):
        print("Etec")

app = QtWidgets.QApplication([])
agenda=uic.loadUi('Aula 07 Agenda.ui')
agenda.btnCadastro.clicked.connect(main)

agenda.show()
app.exec()