import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

#construiremos codigo orientado a objeto utilizando atributos e superClasses
class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

#definição dos atributos de dimensão da janela principal
        self.topo = 100
        self.esquerda = 400
        self.largura = 600 
        self.altura = 600
        self.titulo = "SCPP - SISTEMA DE CADASTRO e PESQUISA DE PRODUTOS"

        self.caixaTexto = QLineEdit(self)
        self.caixaTexto.move(400,20) #posição na tela
        self.caixaTexto.resize(150,20) #largura x Altura

        #vamos criar objeto botão que sera instancia do QPushButton
        self.botao1 = QPushButton('Buscofem', self)
        #passar posição do botão, 1o parametro margEsq e 2o distancia topo
        self.botao1.move(510,350)
        #1o parametro largura x altura 
        self.botao1.resize(70,30)
        self.botao1.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao1.clicked.connect(self.botao1_click)

        #vamos criar objeto botão que sera instancia do QPushButton
        self.botao2 = QPushButton('Dipirona', self)
        #passar posição do botão, 1o parametro margEsq e 2o distancia topo
        self.botao2.move(430,350)
        #1o parametro largura x altura 
        self.botao2.resize(70,30)
        self.botao2.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao2.clicked.connect(self.botao2_click)

        #vamos criar objeto botão que sera instancia do QPushButton
        self.botao3 = QPushButton('Neosaldina', self)
        #passar posição do botão, 1o parametro margEsq e 2o distancia topo
        self.botao3.move(350,350)
        #1o parametro largura x altura 
        self.botao3.resize(70,30)
        self.botao3.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao3.clicked.connect(self.botao3_click)

        #vamos criar objeto botão que sera instancia do QPushButton
        self.botao4 = QPushButton('Plasil', self)
        #passar posição do botão, 1o parametro margEsq e 2o distancia topo
        self.botao4.move(270,350)
        #1o parametro largura x altura 
        self.botao4.resize(70,30)
        self.botao4.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao4.clicked.connect(self.botao4_click)

        self.botaoEnviarBusca = QPushButton('Buscar', self)
        #passar posição do botão, 1o parametro margEsq e 2o distancia topo
        self.botaoEnviarBusca.move(552,15)
        #1o parametro largura x altura 
        self.botaoEnviarBusca.resize(40,25)
        self.botaoEnviarBusca.setStyleSheet('QPushButton {background-color: black; color:white;font: bold; font-size: 10px}')
        self.botaoEnviarBusca.clicked.connect(self.mostraTextoBusca)

        self.label_1 = QLabel(self)
        self.label_1.setText ('Clique em um dos botões: ')
        self.label_1.move(100,100)
        self.label_1.setStyleSheet('QLabel{background-color: black; color: blue; font-size: 20px; font: bold}')
        self.label_1.resize(250,30)

        self.labelBusca = QLabel(self)
        self.labelBusca.setText('Busque por nome do Remédio')
        self.labelBusca.move(250, 15)
        self.labelBusca.resize(150,30)
        self.labelBusca.setStyleSheet('QLabel{background-color: None; color: blue; font-size: 10px; font: bold}')

        self.labelBuscaDigitou = QLabel(self)
        self.labelBuscaDigitou.setText('Digitou: ')
        self.labelBuscaDigitou.move(400, 40) 
        self.labelBuscaDigitou.resize(100,30)
        self.labelBuscaDigitou.setStyleSheet('QLabel{background-color: None; color: blue; font-size: 10px; font: bold}')     

        self.remedio = QLabel(self)
        self.remedio.move(200,100)
        self.remedio.resize(500, 250) #esquerda x altura
        
        #chama a função
        self.CarregarJanela()  


    #vamos usar uma classe que ja existe por herança do QMainWindow
    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    #função que determinará ação ao clicar
    def botao1_click(self):
        print ('O botão 1 foi clicado')
        self.label_1.setText ('Buscofem - R$ 19,90')
        self.label_1.move(150,100) #esquerda x altura
        self.label_1.setStyleSheet('QLabel{background-color: white; color: blue; font-size: 20px; font: bold}')
        self.label_1.resize(300,30)
        self.remedio.setPixmap(QtGui.QPixmap('resources.buscofen.jpg'))
        self.botao1.setStyleSheet('QPushButton {background-color: #FFFF00; color:black;font: bold}')
        self.botao2.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao3.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao4.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')

    #função que determinará ação ao clicar
    def botao2_click(self):
        print ('O botão 2 foi clicado')
        self.label_1.setText ('Dipirona - R$ 25,20')
        self.label_1.move(150,100) #esquerda x altura
        self.label_1.setStyleSheet('QLabel{background-color: white; color: blue; font-size: 20px; font: bold}')
        self.label_1.resize(300,30)
        self.remedio.setPixmap(QtGui.QPixmap('resources\dipirona.jpg'))
        self.botao1.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao2.setStyleSheet('QPushButton {background-color: #FFFF00; color:black;font: bold}')
        self.botao3.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao4.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
    
    #função que determinará ação ao clicar
    def botao3_click(self):
        print ('O botão 2 foi clicado')
        self.label_1.setText ('Neosaldina - R$ 12,50')
        self.label_1.move(150,100) #esquerda x altura
        self.label_1.setStyleSheet('QLabel{background-color: white; color: blue; font-size: 20px; font: bold}')
        self.label_1.resize(300,30)
        self.remedio.setPixmap(QtGui.QPixmap('resources\plasil2.jpg'))
        self.botao1.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao2.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao3.setStyleSheet('QPushButton {background-color: #FFFF00; color:black;font: bold}')
        self.botao4.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')

    def botao4_click(self):
        print ('O botão 2 foi clicado')
        self.label_1.setText ('Plasil - R$ 17,90')
        self.label_1.move(150,100) #esquerda x altura
        self.label_1.setStyleSheet('QLabel{background-color: white; color: blue; font-size: 20px; font: bold}')
        self.label_1.resize(300,30)
        self.remedio.setPixmap(QtGui.QPixmap('resources\plasil.jpg'))
        self.botao1.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao2.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao3.setStyleSheet('QPushButton {background-color: #0000CD; color:#B0C4DE;font: bold}')
        self.botao4.setStyleSheet('QPushButton {background-color: #FFFF00; color:black;font: bold}')



#função que ira buscar o texto digitado na busca
    def mostraTextoBusca(self):
        conteudoTextoBusca = self.caixaTexto.text() #busca o que foi digitado na busca
        self.labelBuscaDigitou.setText("Digitou: "+conteudoTextoBusca)
        self.labelBuscaDigitou.move(400, 40) 
        self.labelBuscaDigitou.resize(150,30)
        self.labelBuscaDigitou.setStyleSheet('QLabel {background-color: None; color:Blue;font: bold}')


#criando objetos para manipulação da janela
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())


#para criação da janela
#bibliotecas, class Janela, construtor, superclasse, atributos da janela, classeCarregar janela e o self.CarregarJanela

#inclusão do botão
