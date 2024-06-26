from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

#Comando SQL
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database = "avaliacao"
)

def avaliacaofuncao():

    if avaliacao.rb_vermelho.isChecked():
        resultado = "vermelho"
    elif avaliacao.rb_amarelo.isChecked():
        resultado = "amarelo"
    elif avaliacao.rb_verde.isChecked():
        resultado = "verde"
    else:
        resultado = "Não Informado"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tbl_leds (led, criado_em) VALUES (%s, now())"
    
    dados = ( [resultado])
    cursor.execute(comando_SQL, dados)
    banco.commit()

app =  QtWidgets.QApplication([])
avaliacao = uic.loadUi('avaliacao_tela.ui')
avaliacao.btn_enviar.clicked.connect(avaliacaofuncao)

avaliacao.show()
app.exec()