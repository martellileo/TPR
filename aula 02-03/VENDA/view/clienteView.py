from model.cliente import Cliente

class ClienteView:
    def menu_cliente(self):
        print(f"\n{' GESTÃO DE CLIENTES ':=^30}")
        print(f"║ {'[1] Cadastrar':<26} ║")
        print(f"║ {'[2] Atualizar':<26} ║")
        print(f"║ {'[3] Listar':<26} ║")
        print(f"║ {'[0] Voltar':<26} ║")
        print("="*30)
        return input("  > : ")
    
    def cadastrar(self):
        print(f"\n{' NOVO CADASTRO ':-^30}")
        c = Cliente()
        c.nome = input("  Nome: ")
        c.endereco = input("  Endereço: ")
        c.cidade = input("  Cidade: ")
        c.uf = input("  UF: ")
        c.cep = input("  CEP: ")
        return c
        
    def editar(self):
        print(f"\n{' ATUALIZAR CLIENTE ':-^30}")
        c = Cliente()
        try:
            c.codcliente = int(input("  Informe o ID do Cliente: "))
            c.nome = input("  Novo Nome: ")
            c.endereco = input("  Novo Endereço: ")
            c.cidade = input("  Nova Cidade: ")
            c.uf = input("  Novo UF: ")
            c.cep = input("  Novo CEP: ")
            return c
        except ValueError:
            print("Erro: ID incorreto.")
            return None

    def listar(self, clientes):
        print(f"\n{' LISTA DE CLIENTES ':=^60}")
        if not clientes:
            print(f"{'A lista está vazia':^60}")
        else:
            print(f"{'ID':<4} | {'NOME':<20} | {'CIDADE/UF':<20} | {'CEP':<10}")
            print("-" * 60)
            for c in clientes:
                cidade_uf = f"{c.cidade}/{c.uf}"
                print(f"{c.codcliente:<4} | {c.nome[:20]:<20} | {cidade_uf[:20]:<20} | {c.cep:<10}")
        print("=" * 60)

    def mensagem(self, texto):
        print(f"\n🔔 {texto}")