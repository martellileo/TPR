import produto

dados = []
contador_id = 1

def criar_produto():
    global contador_id
    p = produto.Produto()
    p.id = contador_id
    p.nome = input("Nome do produto: ")
    p.preco = float(input("Preço: "))
    p.quantidade = int(input("Quantidade: "))
    
    dados.append(p)
    contador_id += 1
    print("\nproduto cadastrado")

def listar_produtos():
    print("\n--- todos os produtos ---")
    if not dados:
        print("lista vazia")
    for p in dados:
        print(f"ID: {p.id} | nome: {p.nome} | preco {p.preco:.2f} | qntd: {p.quantidade}")

def procurar_produto():
    print("\n--- find id ---")
    try:
        id_busca = int(input("digite o id: "))
        for p in dados:
            if p.id == id_busca:
                print(f"ID: {p.id} | nome: {p.nome} | preco {p.preco:.2f} | qntd: {p.quantidade}")
                return
        print(f"\n {id_busca} nao encontrado.")
    except ValueError:
        print("\nid")

def atualizar_produto():
    try:
        id_busca = int(input("id para atualizar: "))
        for p in dados:
            if p.id == id_busca:
                print(f"{p.nome} (deixe em branco para nao alterar)")
                novo_nome = input(f"novo nome [{p.nome}]: ")
                novo_preco = input(f"novo preço [{p.preco}]: ")
                nova_qtd = input(f"nova qntd [{p.quantidade}]: ")

                if novo_nome: p.nome = novo_nome
                if novo_preco: p.preco = float(novo_preco)
                if nova_qtd: p.quantidade = int(nova_qtd)
                
                print("\natualizado")
                return
        print("\nid invalido")
    except ValueError:
        print("\nerro")

def deletar_produto():
    try:
        id_busca = int(input("id para deletar: "))
        for p in dados:
            if p.id == id_busca:
                dados.remove(p)
                print("\ndeletado")
                return
        print("\nid invalido")
    except ValueError:
        print("\nerro")

while True:
    print("\n    SISTEMA DE ESTOQUE    ")
    print("1. cadastrar produto")
    print("2. list all")
    print("3. find por id")
    print("4. atualizar produto")
    print("5. deletar produto")
    print("0. sair")
    
    opcao = input("\n: ")

    if opcao == '1':
        criar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        procurar_produto()
    elif opcao == '4':
        atualizar_produto()
    elif opcao == '5':
        deletar_produto()
    elif opcao == '0':
        print("end")
        break
    else:
        print("out of range")