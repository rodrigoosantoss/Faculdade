import pymysql
from PyQt5 import uic, QtWidgets
from pymysql import err


banco = pymysql.connect(host='localhost',
                        database='DB_RODRIGO_FACUL',
                        user='root',
                        passwd='')



def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    print('O btn - enviar - foi clicado')
    print('')

    print("Codigo:", linha1)
    print("Descricao:", linha2)
    print("Preco", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO AlgoProg2_produtos (codigo,descricao,preco) VALUES (%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3))
    cursor.execute(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
