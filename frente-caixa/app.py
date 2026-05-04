from flask import Flask, render_template, redirect, url_for, request, jsonify
from routes.item_routes import item_bp
from flask import session
from routes.venda_routes import venda_bp
from database import Session
from modelo.Item import Item
from modelo.ItemVenda import ItemVenda
from modelo.Venda import Venda as VendaModel
import base64
from datetime import datetime

app = Flask(__name__)

app.secret_key = "segredo"  # necessário pra sessão

# Adicionar filtro para base64
@app.template_filter('b64encode')
def b64encode_filter(data):
    if data:
        return base64.b64encode(data).decode('utf-8')
    return None

# registrar rotas
app.register_blueprint(item_bp)
app.register_blueprint(venda_bp)

@app.route('/')
def home():
    db = Session()
    itens = db.query(Item).all()
    db.close()
    return render_template('loja.html', itens=itens)

@app.route('/admin')
def admin():
    db = Session()
    itens = db.query(Item).all()
    db.close()
    return render_template('itens.html', itens=itens)

@app.route('/novo-item', methods=['GET'])
def novo_item():
    return render_template('novo_item.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/finalizar-venda', methods=['POST'])
def finalizar_venda():
    data = request.json
    itens = data.get('itens', [])
    
    if not itens:
        return jsonify({'sucesso': False, 'mensagem': 'Carrinho vazio'})
    
    try:
        db = Session()
        
        # Calcular preço total
        preco_total = sum(item['preco'] * item['quantidade'] for item in itens)
        
        venda = VendaModel(
            data=datetime.now().date(),
            precoTotal=preco_total
        )
        db.add(venda)
        db.flush()  # Para pegar o ID gerado
        
        # Adicionar itens da venda
        for item in itens:
            item_venda = ItemVenda(
                idVenda=venda.idVenda,
                idItem=item['id'],
                quantidade=item['quantidade'],
                precoUnitario=item['preco']
            )
            db.add(item_venda)
            
            # Atualizar quantidade em estoque
            produto = db.query(Item).filter(Item.idItem == item['id']).first()
            if produto:
                produto.qtde -= item['quantidade']
        
        db.commit()
        id_venda = venda.idVenda
        db.close()
        
        return jsonify({'sucesso': True, 'idVenda': id_venda})
    except Exception as e:
        print(f"Erro ao finalizar venda: {e}")
        return jsonify({'sucesso': False, 'mensagem': str(e)})


if __name__ == '__main__':
    app.run(debug=True)