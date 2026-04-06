import sys
import random
from PyQt5 import QtWidgets, QtCore, uic

class Bingo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("bingoHud.ui", self)

        self.disponiveis = list(range(1, 76))
        random.shuffle(self.disponiveis)
        self.sorteadas = set()
        
        self.jogadores = self.carregar_dados_jogadores("CARTELAS.txt")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.sorteio)
        
        self.btn_sortear.clicked.connect(self.iniciar_bingo)
        
        if hasattr(self, 'txt_cartelas'):
            self.atualizar_placar()

    def carregar_dados_jogadores(self, arquivo):
        dict_jogadores = {}
        try:
            with open(arquivo, 'r') as f:
                for linha in f:
                    if ';' in linha:
                        nome, nums = linha.strip().split(';')
                        dict_jogadores[nome] = set(int(n) for n in nums.split(','))
        except FileNotFoundError:
            print(f"Aviso: Arquivo {arquivo} não encontrado.")
            
        return dict_jogadores

    def iniciar_bingo(self):
        self.btn_sortear.setEnabled(False)
        self.timer.start(1000) 

    def sorteio(self):
        if not self.disponiveis:
            self.timer.stop()
            return

        numero = self.disponiveis.pop(0)
        self.sorteadas.add(numero)

        self.label_num.setText(str(numero))

        pedra_alterar = self.findChild(QtWidgets.QWidget, f"pedra_{numero}")
        if pedra_alterar:
            pedra_alterar.setStyleSheet("""
                background-color: #27ae60; 
                color: white; 
            """)

        if hasattr(self, 'txt_cartelas'):
            self.atualizar_placar()

        venceu = [n for n, c in self.jogadores.items() if c.issubset(self.sorteadas)]
        if venceu:
            self.timer.stop()
            msg = f"Ganhador(es): {', '.join(venceu)}"
            QtWidgets.QMessageBox.information(self, "BINGO!", msg)

    def atualizar_placar(self):
        texto = ""
        
        for nome, numeros_cartela in self.jogadores.items():
            texto += f"<b>{nome}:</b><br>"
            
            items_formatados = []
            for n in sorted(list(numeros_cartela)):
                if n in self.sorteadas:
                    items_formatados.append(f"<span style='color: green;'>{n}</span>")
                else:
                    items_formatados.append(str(n))
            
            texto += ", ".join(items_formatados)
            texto += "<br><br>"

        self.txt_cartelas.setHtml(texto)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Bingo()
    window.show()
    sys.exit(app.exec_())