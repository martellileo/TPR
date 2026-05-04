from flask import Blueprint, request, render_template, redirect, url_for
from database import Session
from modelo.Item import Item
from contextlib import contextmanager
import base64

item_bp = Blueprint('item_bp', __name__)

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@item_bp.route('/item', methods=['POST'])
def criar_item():
    descricao = request.form.get("descricao")
    qtde = request.form.get("qtde")
    preco_venda = request.form.get("precoVenda")
    preco_custo = request.form.get("precoCusto")
    
    # Processar imagem se enviada
    imagem_binary = None
    if 'imagem' in request.files:
        arquivo = request.files['imagem']
        if arquivo and arquivo.filename:
            imagem_binary = arquivo.read()
    
    with get_db() as db:
        novo = Item(
            descricao=descricao,
            qtde=int(qtde),
            precoVenda=float(preco_venda),
            precoCusto=float(preco_custo),
            imagem=imagem_binary
        )
        
        db.add(novo)
        db.commit()
    
    return redirect(url_for('admin'))