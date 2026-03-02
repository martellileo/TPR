from controller.produtoController import ProdutoController
from controller.clienteController import ClienteController
from controller.vendaController import VendaController
from controller.itemVendaController import ItemVendaController
from controller.pkController import PKController

from view.produtoView import ProdutoView
from view.clienteView import ClienteView
from view.vendaView import VendaView

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)

def menu_principal():
    print(f"\n{' MENU PRINCIPAL ':=^30}")
    print(f"║ {'[1] Clientes':<26} ║")
    print(f"║ {'[2] Produtos':<26} ║")
    print(f"║ {'[3] Vendas':<26} ║")
    print(f"║ {'[0] Sair':<26} ║")
    print("="*30)
    return input("  > : ")

def entrada(prod_controller, cli_controller):
    limpar_tela()
    prod_controller.carregar_csv()
    cli_controller.carregar_csv()

def saida(prod_controller, cli_controller):
    limpar_tela()
    print("Salvando base de dados")
    prod_controller.salvar_csv()
    cli_controller.salvar_csv()

def fluxo_produto(controller, view, pk_controller):
    while True:
        opcao = view.menu_produtos()
        limpar_tela()

        if opcao == '1':
            novo_p = view.cadastrar()
            if novo_p:
                novo_p.codproduto = pk_controller.get_proximo_id(1)
                controller.cadastrar(novo_p)
                view.mensagem(f"Produto adicionado com ID: {novo_p.codproduto}")

        elif opcao == '2':
            p_editado = view.editar()
            if p_editado and controller.atualizar(p_editado):
                view.mensagem("Produto atualizado com sucesso")
            else:
                view.mensagem("Erro: Produto não encontrado")

        elif opcao == '3':
            lista = controller.listar_todos()
            view.listar(lista)

        elif opcao == '0':
            break
        else:
            view.mensagem("Opção inválida")

def fluxo_cliente(controller, view, pk_controller):
    while True:
        opcao = view.menu_cliente()
        limpar_tela()

        if opcao == '1':
            novo_c = view.cadastrar()
            if novo_c:
                novo_c.codcliente = pk_controller.get_proximo_id(0)
                controller.cadastrar(novo_c)
                view.mensagem(f"Cliente cadastrado com ID: {novo_c.codcliente}")

        elif opcao == '2':
            c_editado = view.editar()
            if c_editado and controller.atualizar(c_editado):
                view.mensagem("Cliente atualizado com sucesso")
            else:
                view.mensagem("Erro: Cliente não encontrado")

        elif opcao == '3':
            lista = controller.listar_todos()
            view.listar(lista)

        elif opcao == '0':
            break
        else:
            view.mensagem("Opção inválida")

def fluxo_venda(vend_controller, itemVenda_controller, produto_controller, cli_controller, pk_controller, view):
    while True:
        opcao = view.menu_vendas()
        limpar_tela()
        
        if opcao == '1':
            venda_obj = view.iniciar_venda()
            if venda_obj:
                if not cli_controller.buscar(venda_obj.codcliente):
                    print("Erro: Cliente não encontrado no sistema")
                    continue
                
                venda_obj.codvenda = pk_controller.get_proximo_id(2)
                total_venda = 0
                
                while True:
                    item = view.adicionar_item(venda_obj.codvenda)
                    if item:
                        prod = produto_controller.buscar(item.codproduto)
                        if prod:
                            item.valor = prod.preco
                            total_venda += (item.qntd * item.valor)
                            itemVenda_controller.cadastrar(item)
                            print(f"Item adicionado! Subtotal parcial: R$ {total_venda:.2f}")
                        else:
                            print("Erro: Produto não encontrado")
                    
                    if input("Deseja adicionar mais um item? (S/N): ").upper() != 'S':
                        break
                
                venda_obj.valor_total = total_venda
                vend_controller.cadastrar(venda_obj)
                print(f"Venda {venda_obj.codvenda} finalizada! Total Geral: R$ {total_venda:.2f}")

        elif opcao == '2':
            vendas = vend_controller.listar_vendas()
            view.listar_resumo(vendas)

        elif opcao == '3':
            try:
                entrada_id = input("Digite o ID da venda para detalhar: ")
                if entrada_id.isdigit():
                    id_venda = int(entrada_id)
                    venda = vend_controller.buscar_por_id(id_venda)
                    if venda:
                        itens = itemVenda_controller.listar_itens_da_venda(id_venda)
                        view.detalhar_venda(venda, itens)
                    else:
                        print("Erro: Venda não encontrada.")
                else:
                    print("Erro: Por favor, digite um número inteiro.")
            except Exception as e:
                print(f"Erro ao buscar venda: {e}")

        elif opcao == '0':
            break

def main():
    if not os.path.exists('dados'):
        os.makedirs('dados')

    # controllers
    prod_controller = ProdutoController()
    cli_controller = ClienteController()
    vend_controller = VendaController()
    item_controller = ItemVendaController()
    pk_controller = PKController()

    # views
    prod_view = ProdutoView()
    cli_view = ClienteView()
    vend_view = VendaView()

    # sobe dados pra ram
    entrada(prod_controller, cli_controller)

    while True:
        escolha = menu_principal()
        limpar_tela()

        if escolha == '1':
            fluxo_cliente(cli_controller, cli_view, pk_controller)
        elif escolha == '2':
            fluxo_produto(prod_controller, prod_view, pk_controller)
        elif escolha == '3':
            fluxo_venda(vend_controller, item_controller, prod_controller, cli_controller, pk_controller, vend_view)
        elif escolha == '0':
            # cadastra nos cvs
            saida(prod_controller, cli_controller)
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()