from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database= "agenda"
)

def cadastrarContato():
    campoNome= agenda.leNome.text()
    campoEmail= agenda.leEmail.text()
    campoTelefone= agenda.leTelefone.text()
    
    if agenda.rbResidencial.isChecked():
        tipoTelefone="Residencial"
    elif agenda.rbCelular.isChecked():
        tipoTelefone="Celular"
    else:
        tipoTelefone="Não Informado"
        
    cursor = banco.cursor()
    comando_SQL = "Insert into contatos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)"
    dados = (str(campoNome), str(campoEmail), str(campoTelefone), tipoTelefone)
    cursor.execute(comando_SQL,dados)
    banco.commit()

app = QtWidgets.QApplication([])
agenda=uic.loadUi('Aula 07 Agenda.ui')
agenda.btnCadastro.clicked.connect(cadastrarContato)

agenda.show()
app.exec()