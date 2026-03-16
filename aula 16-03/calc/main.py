import sys
from PyQt5 import QtWidgets, uic
import math


class Calculadora(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("calc.ui", self)

        self.expressao = ""
        self.numero_atual = ""
        self.saida = False

        botoes_numeros = [
            self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4,
            self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9
        ]

        for botao in botoes_numeros:
            botao.clicked.connect(self.pressionar_numero)

        self.btn_mais.clicked.connect(lambda: self.pressionar_operador('+'))
        self.btn_menos.clicked.connect(lambda: self.pressionar_operador('-'))
        self.btn_vezes.clicked.connect(lambda: self.pressionar_operador('*'))
        self.btn_div.clicked.connect(lambda: self.pressionar_operador('/'))

        self.btn_divisor.clicked.connect(self.inverso)
        self.btn_sqr.clicked.connect(self.quadrado)
        self.btn_raiz.clicked.connect(self.raiz)

        self.btn_backspace.clicked.connect(self.backspace)

        self.btn_resto.clicked.connect(self.resto)

        self.btn_ce.clicked.connect(self.clear_entry)

        self.btn_clear.clicked.connect(self.limpar)
        self.btn_igual.clicked.connect(self.calcular)


    def pressionar_numero(self):
        botao = self.sender()
        valor = botao.text()

        if self.saida:
            self.numero_atual = valor
            self.saida = False
        else:
            self.numero_atual += valor

        self.lcdNumber.display(float(self.numero_atual))


    def pressionar_operador(self, operador):
        if self.numero_atual != "":
            self.expressao += self.numero_atual + operador
            self.numero_atual = ""

        self.saida = False


    def limpar(self):
        self.expressao = ""
        self.numero_atual = ""
        self.saida = False
        self.lcdNumber.display(0)


    def inverso(self):
        try:
            valor = float(self.numero_atual)
            resultado = 1 / valor

            self.numero_atual = str(resultado)
            self.lcdNumber.display(resultado)

            self.saida = True
        except:
            self.lcdNumber.display(0)


    def quadrado(self):
        try:
            valor = float(self.numero_atual)
            resultado = math.pow(valor, 2)

            self.numero_atual = str(resultado)
            self.lcdNumber.display(resultado)

            self.saida = True
        except:
            self.lcdNumber.display(0)


    def raiz(self):
        try:
            valor = float(self.numero_atual)
            resultado = math.sqrt(valor)

            self.numero_atual = str(resultado)
            self.lcdNumber.display(resultado)

            self.saida = True
        except:
            self.lcdNumber.display(0)


    def backspace(self):
        if self.saida:
            return

        self.numero_atual = self.numero_atual[:-1]

        if self.numero_atual == "":
            self.lcdNumber.display(0)
        else:
            self.lcdNumber.display(float(self.numero_atual))


    def resto(self):
        try:
            valor = float(self.numero_atual)
            resultado = valor % 2

            self.numero_atual = str(resultado)
            self.lcdNumber.display(resultado)

            self.saida = True
        except:
            self.lcdNumber.display(0)


    def clear_entry(self):
        self.numero_atual = ""
        self.saida = False
        self.lcdNumber.display(0)


    def calcular(self):
        try:
            expressao_final = self.expressao + self.numero_atual
            resultado = eval(expressao_final)

            self.lcdNumber.display(resultado)

            self.expressao = ""
            self.numero_atual = str(resultado)
            self.saida = True

        except:
            self.lcdNumber.display(0)
            self.expressao = ""
            self.numero_atual = ""
            self.saida = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())