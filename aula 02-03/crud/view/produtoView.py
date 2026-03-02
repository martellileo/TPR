from model.produto import Produto

class ProdutoView:
    def menu_produtos(self):
        print(f"\n{' GESTÃO DE PRODUTOS ':=^30}")
        print(f"║ {'[1] Cadastrar':<26} ║")
        print(f"║ {'[2] Atualizar':<26} ║")
        print(f"║ {'[3] Listar':<26} ║")
        print(f"║ {'[0] Voltar':<26} ║")
        print("="*30)
        return input("  > : ")

    def cadastrar(self):
        print(f"\n{' NOVO PRODUTO ':-^30}")
        p = Produto()
        p.nome = input("  Nome do Produto: ")
        try:
            p.preco = float(input("  Preço: "))
            return p
        except ValueError:
            print("Erro: Preço incorreto!")
            return None
        
    def editar(self):
        print(f"\n{' ATUALIZAR PRODUTO ':-^30}")
        p = Produto()
        try:
            p.codproduto = int(input("  Informe o ID do Produto: "))
            p.nome = input("  Novo Nome: ")
            p.preco = float(input("  Novo Preço: "))
            return p
        except ValueError:
            print("Erro: Valores incorreto.")
            return None

    def listar(self, produtos):
        print(f"\n{' LISTA DE PRODUTOS ':=^45}")
        if not produtos:
            print(f"{'A lista está vazia':^45}")
        else:
            print(f"{'ID':<5} | {'NOME DO PRODUTO':<25} | {'PREÇO':>10}")
            print("-" * 45)
            for p in produtos:
                print(f"{p.codproduto:<5} | {p.nome[:25]:<25} | R${p.preco:>8.2f}")
        print("=" * 45)

    def mensagem(self, texto):
        print(f"\n🔔 {texto}")