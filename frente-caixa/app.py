from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask import session
from contextlib import contextmanager
from database import Session
from modelo.Item import Item
from modelo.ItemVenda import ItemVenda
from modelo.Venda import Venda as VendaModel
import base64
from datetime import datetime

app = Flask(__name__)

@app.template_filter('b64encode')
def b64encode_filter(data):
    if data:
        return base64.b64encode(data).decode('utf-8')
    return None


@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.route('/')
def home():
    db = Session()
    tipo_filtro = request.args.get('tipo', '').strip()
    busca = request.args.get('busca', '').strip()
    
    query = db.query(Item)
    if tipo_filtro:
        query = query.filter(Item.tipo == tipo_filtro)
    if busca:
        query = query.filter(Item.descricao.ilike(f'%{busca}%'))
    
    itens = query.all()
    tipos = db.query(Item.tipo).filter(Item.tipo != None).distinct().all()
    tipos = [t[0] for t in tipos if t[0]]
    db.close()
    return render_template('loja.html', itens=itens, tipos=tipos, tipo_selecionado=tipo_filtro, busca_termo=busca)


@app.route('/admin')
def admin():
    return render_template('admin_painel.html')


@app.route('/admin/listar_itens')
def listar_itens():
    db = Session()
    tipo_filtro = request.args.get('tipo', '').strip()
    busca = request.args.get('busca', '').strip()
    
    query = db.query(Item)
    if tipo_filtro:
        query = query.filter(Item.tipo == tipo_filtro)
    if busca:
        query = query.filter(Item.descricao.ilike(f'%{busca}%'))
    
    itens = query.all()
    tipos = db.query(Item.tipo).filter(Item.tipo != None).distinct().all()
    tipos = [t[0] for t in tipos if t[0]]
    db.close()
    return render_template('itens.html', itens=itens, tipos=tipos, tipo_selecionado=tipo_filtro, busca_termo=busca)


@app.route('/admin/listar_vendas')
def listar_vendas():
    db = Session()
    try:
        id_filtro = request.args.get('id', '').strip()
        data_inicio = request.args.get('data_inicio', '').strip()
        data_fim = request.args.get('data_fim', '').strip()
        
        query = db.query(VendaModel)
        
        if id_filtro:
            query = query.filter(VendaModel.idVenda == int(id_filtro))
        
        if data_inicio:
            from datetime import datetime as dt
            data_inicio_obj = dt.strptime(data_inicio, '%Y-%m-%d').date()
            query = query.filter(VendaModel.data >= data_inicio_obj)
        
        if data_fim:
            from datetime import datetime as dt
            data_fim_obj = dt.strptime(data_fim, '%Y-%m-%d').date()
            query = query.filter(VendaModel.data <= data_fim_obj)
        
        vendas = query.order_by(VendaModel.idVenda.desc()).all()
        vendas_detalhadas = []

        for venda in vendas:
            itens_venda = (
                db.query(ItemVenda, Item)
                .outerjoin(Item, ItemVenda.idItem == Item.idItem)
                .filter(ItemVenda.idVenda == venda.idVenda)
                .all()
            )

            itens_formatados = []
            for item_venda, item in itens_venda:
                qtd = item_venda.quantidade or 0
                itens_formatados.append({
                    'idItem': item_venda.idItem,
                    'descricao': item.descricao if item else 'Item removido',
                    'quantidade': qtd,
                    'precoUnitario': item_venda.precoUnitario,
                    'subtotal': qtd * (item_venda.precoUnitario or 0)
                })

            vendas_detalhadas.append({
                'idVenda': venda.idVenda,
                'data': venda.data,
                'dataPagamento': venda.dataPagamento,
                'formaPagamento': venda.formaPagamento,
                'precoTotal': venda.precoTotal,
                'totalItens': len(itens_formatados),
                'itens': itens_formatados
            })

        return render_template('vendas.html', vendas=vendas_detalhadas, id_filtro=id_filtro, data_inicio=data_inicio, data_fim=data_fim)
    finally:
        db.close()


@app.route('/novo-item', methods=['GET'])
def novo_item():
    return render_template('novo_item.html')


@app.route('/editar-item/<int:id>', methods=['GET'])
def editar_item(id):
    db = Session()
    try:
        item = db.query(Item).filter(Item.idItem == id).first()
        if not item:
            return redirect(url_for('listar_itens'))
        return render_template('editar_item.html', item=item)
    finally:
        db.close()


@app.route('/item/<int:id>', methods=['POST'])
def atualizar_item(id):
    descricao = request.form.get("descricao")
    tipo = request.form.get("tipo")
    qtde = request.form.get("qtde")
    preco_venda = request.form.get("precoVenda")
    preco_custo = request.form.get("precoCusto")
    
    with get_db() as db:
        item = db.query(Item).filter(Item.idItem == id).first()
        if item:
            item.descricao = descricao
            item.tipo = tipo
            item.qtde = int(qtde)
            item.precoVenda = float(preco_venda)
            item.precoCusto = float(preco_custo)
            
            if 'imagem' in request.files:
                arquivo = request.files['imagem']
                if arquivo and arquivo.filename:
                    item.imagem = arquivo.read()
            
            db.commit()
    
    return redirect(url_for('listar_itens'))


@app.route('/remover-item/<int:id>', methods=['POST'])
def remover_item(id):
    with get_db() as db:
        item = db.query(Item).filter(Item.idItem == id).first()
        if item:
            db.delete(item)
            db.commit()
    
    return redirect(url_for('listar_itens'))


@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')


@app.route('/itens')
def ver_itens():
    db = Session()
    tipo_filtro = request.args.get('tipo', '').strip()
    busca = request.args.get('busca', '').strip()
    
    query = db.query(Item)
    if tipo_filtro:
        query = query.filter(Item.tipo == tipo_filtro)
    if busca:
        query = query.filter(Item.descricao.ilike(f'%{busca}%'))
    
    itens = query.all()
    tipos = db.query(Item.tipo).filter(Item.tipo != None).distinct().all()
    tipos = [t[0] for t in tipos if t[0]]
    db.close()
    return render_template('loja.html', itens=itens, tipos=tipos, tipo_selecionado=tipo_filtro, busca_termo=busca)


@app.route('/add-carrinho/<int:id>')
def add_carrinho(id):
    if 'carrinho' not in session:
        session['carrinho'] = []

    session['carrinho'].append(id)
    session.modified = True

    return redirect(url_for('ver_itens'))


@app.route('/item', methods=['POST'])
def criar_item():
    descricao = request.form.get("descricao")
    tipo = request.form.get("tipo")
    qtde = request.form.get("qtde")
    preco_venda = request.form.get("precoVenda")
    preco_custo = request.form.get("precoCusto")
    imagem_binary = None
    if 'imagem' in request.files:
        arquivo = request.files['imagem']
        if arquivo and arquivo.filename:
            imagem_binary = arquivo.read()

    with get_db() as db:
        novo = Item(
            descricao=descricao,
            tipo=tipo,
            qtde=int(qtde),
            precoVenda=float(preco_venda),
            precoCusto=float(preco_custo),
            imagem=imagem_binary
        )

        db.add(novo)
        db.commit()

    return redirect(url_for('listar_itens'))


@app.route('/finalizar-venda', methods=['POST'])
def finalizar_venda():
    data = request.json or {}
    itens = data.get('itens', [])
    forma_pagamento = (data.get('formaPagamento') or 'dinheiro').strip()
    
    if not itens:
        return jsonify({'sucesso': False, 'mensagem': 'Carrinho vazio'})
    
    db = Session()
    try:
        
        preco_total = sum(item['preco'] * item['quantidade'] for item in itens)
        
        venda = VendaModel(
            data=datetime.now().date(),
            precoTotal=preco_total,
            formaPagamento=forma_pagamento,
            dataPagamento=datetime.now().date()
        )
        db.add(venda)
        db.flush()
        
        for item in itens:
            item_venda = ItemVenda(
                idVenda=venda.idVenda,
                idItem=item['id'],
                quantidade=item['quantidade'],
                precoUnitario=item['preco']
            )
            db.add(item_venda)
            
            produto = db.query(Item).filter(Item.idItem == item['id']).first()
            if produto:
                produto.qtde -= item['quantidade']
        
        db.commit()
        id_venda = venda.idVenda
        
        return jsonify({'sucesso': True, 'idVenda': id_venda})
    except Exception as e:
        db.rollback()
        print(f"Erro ao finalizar venda: {e}")
        return jsonify({'sucesso': False, 'mensagem': str(e)})
    finally:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)