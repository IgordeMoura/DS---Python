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

def gerarPDF():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    
    y = 0 
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Lista de Contatos")
    
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "NOME")
    pdf.drawString(210, 750, "EMAIL")
    pdf.drawString(370, 750, "TELEFONE")
    pdf.drawString(470, 750, "TIPO DE CONTATO")
    
    for i in range(0, len (contatos_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(contatos_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(contatos_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(contatos_lidos[i][2]))
        pdf.drawString(370, 750 - y, str(contatos_lidos[i][3]))
        pdf.drawString(470, 750 - y, str(contatos_lidos[i][4]))
        
    pdf.save()
    print("PDF gerado com sucesso!")

def excluirContato():
    linhaContato = listarContatos.tabelaContatos.currentRow()
    listarContatos.tabelaContatos.removeRow(linhaContato)
    
    cursor = banco.cursor()
    comando_SQL = "SELECT id FROM contatos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato][0]
    cursor.execute("DELETE FROM contatos WHERE id=" + str(valorId))
    banco.commit()

app = QtWidgets.QApplication([])
agenda=uic.loadUi('Aula 07 Agenda.ui')
listarContatos = uic.loadUi('Aula 08 Contatos.ui')

agenda.btnCadastro.clicked.connect(cadastrarContato)
agenda.btnConsultar.clicked.connect(consultarContatos)

listarContatos.btnGerarPDF.clicked.connect(gerarPDF)
listarContatos.btnDeleteContato.clicked.connect(excluirContato)

agenda.show()
app.exec()