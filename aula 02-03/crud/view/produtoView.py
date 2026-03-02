from model.produto import Produto

class ProdutoView:
    def menu_produtos(self):
        print("\n--- produto ---")
        print("1. cadastro produto")
        print("2. atualizar produto")
        print("3. listar produtos")
        print("0. voltar")
        return input("Escolha uma opção: ")

    def cadastrar(self):
        print("\n-- cadastro --")
        p = Produto()
        p.codproduto = int(input("codigo: "))
        p.nome = input("nome: ")
        p.preco = float(input("preco: "))
        return p
        
    def editar(self):
        print("\n-- atualizar produto --")
        p = Produto()
        p.codproduto = int(input("informe codigo para alterar: "))
        p.nome = input("novo nome: ")
        p.preco = float(input("novo preco: "))
        return p

    def listar(self, produtos):
        print("\n-- list all --")
        if not produtos:
            print("lista vazia")
        else:
            for p in produtos:
                print(p)

    def mensagem(self, texto):
        print(texto)