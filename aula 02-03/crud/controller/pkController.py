import os

class PKController:
    def __init__(self):
        self.arquivo_pk = 'dados/pk.csv'
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(self.arquivo_pk):
            with open(self.arquivo_pk, 'w', encoding='utf-8') as f:
                f.write("0;0;0")

    def get_proximo_id(self, tipo):

        with open(self.arquivo_pk, 'r', encoding='utf-8') as f:
            pks = f.read().strip().split(';')
        
        novo_id = int(pks[tipo]) + 1
        pks[tipo] = str(novo_id)
        
        with open(self.arquivo_pk, 'w', encoding='utf-8') as f:
            f.write(";".join(pks))
            
        return novo_id