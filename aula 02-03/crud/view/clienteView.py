from model.cliente import Cliente

class ClienteView:
    def menu_cliente(self):
        print("\n--- cliente ---")
        print("1. cadastrar  cliente")
        print("2. atualizar cliente")
        print("3. listar clientes")
        print("0. Voltar")
        return input("Escolha uma opção: ")
    
    def cadastrar(self): # verificar o codigo e/ou mudar pra auto increment
        print("\n-- cadastro --")
        c = Cliente()
        c.codcliente = int(input("codigo: "))
        c.nome = input("nome: ")
        c.endereco = input("endereco: ")
        c.cidade = input("cidade: ")
        c.uf = input("uf: ")
        c.cep = input("cep: ")
        return c
        
    def editar(self):
        print("\n-- atualizar produto --")
        c = Cliente()
        c.codcliente = int(input("informe codigo para alterar: "))
        c.nome = input("novo nome: ")
        c.endereco = input("novo endereco: ")
        c.cidade = input("nova cidade: ")
        c.uf = input("novo uf: ")
        c.cep = input("novo cep: ")
        return c

    def listar(self, clientes):
        print("\n-- list all --")
        if not clientes:
            print("lista vazia")
        else:
            for c in clientes:
                print(c)

    def mensagem(self, texto):
        print(texto)