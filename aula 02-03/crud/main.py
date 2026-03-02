from controller.produtoController import ProdutoController
from controller.clienteController import ClienteController

from view.produtoView import ProdutoView
from view.clienteView import ClienteView

import os

def menu_principal():
    print("\n--- main ---")
    print("1. clientes")
    print("2. produtos")
    print("3. vendas")
    print("0. sair")
    return input("escolha uma opção: ")

def entrada(prod_controller, cli_controller):
    print("base carregada")
    prod_controller.carregar_csv()
    cli_controller.carregar_csv()

def saida(prod_controller, cli_controller):
    print("base salva")
    prod_controller.salvar_csv()
    cli_controller.salvar_csv()

def fluxo_produto(controller, view):
    while True:
        opcao = view.menu_produtos()

        if opcao == '1':
            novo_p = view.cadastrar()
            if novo_p:
                controller.cadastrar(novo_p)
                view.mensagem("produto adicionado")

        elif opcao == '2':
            p_editado = view.editar()
            if controller.atualizar(p_editado):
                view.mensagem("produto atualizado")
            else:
                view.mensagem("produto nao encontrado")

        elif opcao == '3':
            lista = controller.listar_todos()
            view.listar(lista)

        elif opcao == '0':
            break
        else:
            view.mensagem("out of range")

def fluxo_cliente(controller, view):
    while True:
        opcao = view.menu_cliente()

        if opcao == '1':
            novo_c = view.cadastrar()
            if novo_c:
                controller.cadastrar(novo_c)
                view.mensagem("cliente cadastrado")

        elif opcao == '2':
            c_editado = view.editar()
            if controller.atualizar(c_editado):
                view.mensagem("cliente atualizado")
            else:
                view.mensagem("cliente nao encontrado")

        elif opcao == '3':
            lista = controller.listar_todos()
            view.listar(lista)

        elif opcao == '0':
            break
        else:
            view.mensagem("out of range")

def main():
    if not os.path.exists('dados'):
        os.makedirs('dados')

    prod_controller = ProdutoController()
    prod_view = ProdutoView()
    cli_controller = ClienteController()
    cli_view = ClienteView()

    entrada(prod_controller, cli_controller)

    while True:
        escolha = menu_principal()

        if escolha == '1':
            fluxo_cliente(cli_controller, cli_view)
        elif escolha == '2':
            fluxo_produto(prod_controller, prod_view)
        elif escolha == '0':
            saida(prod_controller, cli_controller)
            break
        else:
            print("out of range")

if __name__ == "__main__":
    main()