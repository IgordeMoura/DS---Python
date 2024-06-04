from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda"
)

def cadastrarContato():
    campoNome = agenda.leNome.text()
    campoEmail = agenda.leEmail.text()
    campoTelefone = agenda.leTelefone.text()

    if agenda.rbResidencial.isChecked():
        tipoTelefone = "Residencial"
    elif agenda.rbCelular.isChecked():
        tipoTelefone = "Celular"
    else:
        tipoTelefone = "Não Informado"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO contatos (nome, email, telefone, tipoTelefone) VALUES (%s, %s, %s, %s)"
    dados = (str(campoNome), str(campoEmail), str(campoTelefone), tipoTelefone)
    cursor.execute(comando_SQL, dados)
    banco.commit()

def consultarContatos():
    listarContatos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatosLidos = cursor.fetchall()

    listarContatos.tabelaContatos.setRowCount(len(contatosLidos))
    listarContatos.tabelaContatos.setColumnCount(5)

    for i in range(len(contatosLidos)):
        for f in range(5):
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

    for i in range(len(contatos_lidos)):
        y += 50
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
    cursor.execute("DELETE FROM contatos WHERE id=%s", (valorId,))
    banco.commit()

def abrirAlteracao():
    EditContatos.show()

    linhaContato = listarContatos.tabelaContatos.currentRow()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    
    if linhaContato < 0 or linhaContato >= len(contatos_lidos):
        return  # Verifica se a linha selecionada é válida
    
    valorId, valorNome, valorEmail, valorTelefone, valorTipoTelefone = contatos_lidos[linhaContato]

    EditContatos.leID.setText(str(valorId))
    EditContatos.leNome.setText(valorNome)
    EditContatos.leEmail.setText(valorEmail)
    EditContatos.leTelefone.setText(valorTelefone)

    if valorTipoTelefone == 'Celular':
        EditContatos.rbCelular.setChecked(True)
    elif valorTipoTelefone == 'Residencial':
        EditContatos.rbResidencial.setChecked(True)
    else:
        EditContatos.rbNaoInformado.setChecked(True)

def alterarContato():
    campoId = EditContatos.leID.text()
    campoNome = EditContatos.leNome.text()
    campoEmail = EditContatos.leEmail.text()
    campoTelefone = EditContatos.leTelefone.text()

    if EditContatos.rbResidencial.isChecked():
        tipoTelefone = "Residencial"
    elif EditContatos.rbCelular.isChecked():
        tipoTelefone = "Celular"
    else:
        tipoTelefone = "Não Informado"

    cursor = banco.cursor()
    comando_SQL = "UPDATE contatos SET nome=%s, email=%s, telefone=%s, tipoTelefone=%s WHERE id=%s"
    dados = (campoNome, campoEmail, campoTelefone, tipoTelefone, campoId)
    cursor.execute(comando_SQL, dados)
    banco.commit()

app = QtWidgets.QApplication([])
agenda = uic.loadUi('Aula 07 Agenda.ui')
listarContatos = uic.loadUi('Aula 08 Contatos.ui')
EditContatos = uic.loadUi('Aula 11 Alterar.ui')

agenda.btnCadastro.clicked.connect(cadastrarContato)
agenda.btnConsultar.clicked.connect(consultarContatos)

listarContatos.btnGerarPDF.clicked.connect(gerarPDF)
listarContatos.btnDeleteContato.clicked.connect(excluirContato)
listarContatos.btnAlterContato.clicked.connect(abrirAlteracao)

EditContatos.btnSalvar.clicked.connect(alterarContato)

agenda.show()
app.exec()
