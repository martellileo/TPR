from database import Session
from modelo.venda import Venda
from modelo.item_venda import ItemVenda
from modelo.produto import Produto


class VendaController:
    def lancar_venda(self, id_cliente, lista_produtos):
        with Session() as session:
            try:
                nova_venda = Venda(id_cliente=id_cliente)
                session.add(nova_venda)
                session.flush() 

                valor_total_acumulado = 0

                for item in lista_produtos:
                    prod = session.query(Produto).get(item['id_produto'])

                    if not prod or prod.qtde < item['quantidade']:
                        raise Exception(f"Estoque insuficiente ou produto {item['id_produto']} não encontrado.")

                    subtotal = prod.preco * item['quantidade']
                    valor_total_acumulado += subtotal

                    iv = ItemVenda(
                        id_venda=nova_venda.id_venda,
                        id_produto=prod.id_produto,
                        qtde=item['quantidade'],
                        preco=prod.preco
                    )

                    prod.qtde -= item['quantidade']
                    session.add(iv)

                nova_venda.valor_total = valor_total_acumulado
                session.commit()
                return nova_venda

            except Exception as e:
                session.rollback()
                print(f"Erro ao processar venda: {e}")
                return None