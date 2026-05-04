from flask import Blueprint, render_template, session, redirect, url_for
from database import Session
from modelo.Item import Item

venda_bp = Blueprint('venda_bp', __name__)

def get_db():
    return Session()


@venda_bp.route('/itens')
def ver_itens():
    db = get_db()
    itens = db.query(Item).all()
    db.close()
    return render_template('loja.html', itens=itens)


@venda_bp.route('/add-carrinho/<int:id>')
def add_carrinho(id):
    if 'carrinho' not in session:
        session['carrinho'] = []

    session['carrinho'].append(id)
    session.modified = True

    return redirect(url_for('venda_bp.ver_itens'))


@venda_bp.route('/carrinho')
def ver_carrinho():
    return render_template('carrinho.html')