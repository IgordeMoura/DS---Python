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

def consultarContatos():
    listarContatos.show()
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatosLidos = cursor.fetchall()
    
    listarContatos.tabelaContatos.setRowCount(len(contatosLidos))
    listarContatos.tabelaContatos.setColumnCount(5)
    
    for i in range(0, len(contatosLidos)):
        for f in range(0, 5):
            listarContatos.tabelaContatos.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][f])))

app = QtWidgets.QApplication([])
agenda=uic.loadUi('Aula 07 Agenda.ui')
listarContatos = uic.loadUi('Aula 08 Contatos.ui')

agenda.btnCadastro.clicked.connect(cadastrarContato)
agenda.btnConsultar.clicked.connect(consultarContatos)

# listarContatos.btnGerarPDF.clicked.connect('Gerar PDF')

agenda.show()
app.exec()