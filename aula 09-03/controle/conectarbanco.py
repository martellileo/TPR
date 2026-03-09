import mysql.connector
from mysql.connector import Error

class Banco:
    def __init__(self):
        self.servidor = ""
        self.usuario = ""
        self.senha = ""
        self.banco = ""
        self.porta = 0
        self.con = None
        self.ponteiro = None

    def configura(self, ho, se, us, db, po):
        self.servidor = ho
        self.senha = se
        self.usuario = us
        self.banco = db
        self.porta = po

    def abrirConexao(self):
        try:
            if self.con is None or not self.con.is_connected():
                self.con = mysql.connector.connect(
                    host=self.servidor,
                    user=self.usuario,
                    password=self.senha,
                    database=self.banco,
                    port=self.porta
                )
                self.ponteiro = self.con.cursor()
        except Error as e:
            print(f"Erro ao abrir conexão com MySQL: {e}")
            self.con = None
            self.ponteiro = None
            raise

    def fecharConexao(self):
        try:
            if self.ponteiro is not None:
               self.ponteiro.close()
               self.ponteiro = None

            if self.con is not None and self.con.is_connected():
               self.con.close()
               self.con = None
        except Error as e:
            print(f"Erro ao fechar conexão: {e}")

    def testarConexao(self):
        try:
            self.abrirConexao()
            print("Conexão realizada com sucesso.")
            return True
        except Error as e:
            print(f"Falha ao conectar: {e}")
            return False
        finally:
            self.fecharConexao()

    def selectQuery(self, sql, dados=None):
        try:
            self.abrirConexao()
            if dados is not None:
                self.ponteiro.execute(sql, dados)
            else:
                self.ponteiro.execute(sql)
            return self.ponteiro.fetchall()
        except Error as e:
            print(f"Erro no select: {e}")
            raise

    def selectOne(self, sql, dados=None):
        try:
            self.abrirConexao()
            if dados is not None:
                self.ponteiro.execute(sql, dados)
            else:
                self.ponteiro.execute(sql)
            return self.ponteiro.fetchone()
        except Error as e:
            print(f"Erro no selectOne: {e}")
            raise

    def execute(self, sql, dados=None):
        try:
            self.abrirConexao()
            if dados is not None:
                self.ponteiro.execute(sql, dados)
            else:
                self.ponteiro.execute(sql)
        except Error as e:
            print(f"Erro ao executar comando: {e}")
            raise

    def executeMany(self, sql, lista_dados):
        try:
            self.abrirConexao()
            self.ponteiro.executemany(sql, lista_dados)
        except Error as e:
            print(f"Erro ao executar vários comandos: {e}")
            raise

    def gravar(self):
        try:
            if self.con is not None and self.con.is_connected():
                self.con.commit()
        except Error as e:
            print(f"Erro ao gravar transação: {e}")
            raise

    def descarte(self):
        try:
            if self.con is not None and self.con.is_connected():
                self.con.rollback()
        except Error as e:
            print(f"Erro ao desfazer transação: {e}")
            raise

    def mostraResultado(self, entrada):
        for i in entrada:
            print(i)