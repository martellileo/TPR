import os
from database import init_db
from controle.cliente_controller import ClienteController
from controle.produto_controller import ProdutoController
from controle.venda_controller import VendaController

init_db()
ctrl_cli = ClienteController()
ctrl_prod = ProdutoController()
ctrl_venda = VendaController()


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 50)


def menu_principal():
    while True:
        limpar_tela()
        print("==============================")
        print("SISTEMA DE VENDAS")
        print("==============================")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Cadastrar Produto")
        print("4. Listar Produtos")
        print("5. Realizar Venda")
        print("0. Sair")
        print("==============================")

        opcao = input("Opção: ")

        if opcao == '1':
            limpar_tela()
            print("--- NOVO CLIENTE ---")
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cidade = input("Cidade: ")
            uf = input("UF: ")
            cep = input("CEP: ")
            ctrl_cli.cadastrar(nome, endereco, cidade, uf, cep)
            print("\nCliente cadastrado com sucesso.")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == '2':
            limpar_tela()
            print("--- LISTA DE CLIENTES ---")
            clientes = ctrl_cli.listar_todos()
            for c in clientes:
                print(f"ID: {c.id_cliente} | Nome: {c.nome} | Cidade: {c.cidade}-{c.uf}")

        elif opcao == '3':
            limpar_tela()
            print("--- NOVO PRODUTO ---")
            nome = input("Nome do Produto: ")
            qtde = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            ctrl_prod.cadastrar(nome, qtde, preco)
            print("\nProduto cadastrado com sucesso.")

        elif opcao == '4':
            limpar_tela()
            print("--- LISTA DE PRODUTOS ---")
            produtos = ctrl_prod.listar_todos()
            for p in produtos:
                print(f"ID: {p.id_produto} | {p.nome} | Estoque: {p.qtde} | Preço: R${p.preco:.2f}")

        elif opcao == '5':
            limpar_tela()
            print("--- NOVA VENDA ---")
            id_cli = int(input("ID do Cliente: "))

            carrinho = []
            while True:
                id_prod = int(input("ID do Produto (0 para finalizar): "))
                if id_prod == 0:
                    break
                qtd = int(input("Quantidade: "))
                carrinho.append({'id_produto': id_prod, 'quantidade': qtd})

            if carrinho:
                venda = ctrl_venda.lancar_venda(id_cli, carrinho)
                if venda:
                    print(f"\nVenda {venda.id_venda} concluída. Total: R$ {venda.valor_total:.2f}")
                else:
                    print("\nErro ao realizar venda. Verifique estoque e IDs.")
            else:
                print("\nVenda cancelada.")


        elif opcao == '0':
            limpar_tela()
            print("Sistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu_principal()