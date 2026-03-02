from model.venda import Venda
from model.itemVenda import ItemVenda

class VendaView:
    def menu_vendas(self):
        print(f"\n{' GESTÃO DE VENDAS ':=^30}")
        print(f"║ {'[1] Nova Venda':<26} ║")
        print(f"║ {'[2] Listar Vendas':<26} ║")
        print(f"║ {'[3] Detalhar Venda':<26} ║")
        print(f"║ {'[0] Voltar':<26} ║")
        print("="*30)
        return input("  > : ")

    def iniciar_venda(self):
        print(f"\n{' ABERTURA DE PEDIDO ':-^40}")
        v = Venda()
        try:
            v.codcliente = int(input("  Código do Cliente: "))
            v.data = input("  Data (DD/MM/AAAA): ")
            return v
        except ValueError:
            print("\nErro: Código do cliente incorreto.")
            return None

    def adicionar_item(self, codvenda):
        it = ItemVenda()
        try:
            print(f"\n  {' Inserir Produto ':.^30}")
            it.codvenda = codvenda
            it.codproduto = int(input("  ID Produto: "))
            it.qntd = int(input("  Quantidade: "))
            return it
        except ValueError:
            print("\nErro: Entrada inválida para produto ou quantidade!")
            return None

    def listar_resumo(self, vendas):
        print(f"\n{' HISTÓRICO DE VENDAS ':=^60}")
        if not vendas:
            print(f"{'Nenhuma venda registrada':^60}")
        else:
            print(f"{'ID':<6} | {'CLIENTE':<10} | {'DATA':<12} | {'TOTAL':>15}")
            print("-" * 60)
            for v in vendas:
                print(f"{v.codvenda:<6} | {v.codcliente:<10} | {v.data:<12} | R${v.valor_total:>13.2f}")
        print("=" * 60)

    def detalhar_venda(self, venda, itens):
        print(f"\n{' COMPROVANTE DE VENDA ':=^45}")
        print(f"  VENDA Nº: {venda.codvenda:<10} DATA: {venda.data}")
        print(f"  CLIENTE:  {venda.codcliente}")
        print("-" * 45)
        print(f"{'PROD':<8} | {'QNT':<5} | {'V. UNIT':>10} | {'SUBTOTAL':>12}")
        print("-" * 45)
        
        for it in itens:
            sub = it.qntd * it.valor
            print(f"{it.codproduto:<8} | {it.qntd:<5} | {it.valor:>10.2f} | {sub:>12.2f}")
            
        print("-" * 45)
        print(f"{'TOTAL GERAL:':<30} R${venda.valor_total:>10.2f}")
        print("=" * 45)