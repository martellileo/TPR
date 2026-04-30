from flask import Flask, render_template, request

app = Flask(__name__)

cadastros = []

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    mensagem = None
    
    if request.method == 'POST':
        novo_cadastro = {
            'nome': request.form.get('nome'),
            'endereco': request.form.get('endereco'),
            'cidade': request.form.get('cidade'),
            'uf': request.form.get('uf').upper(),
            'cep': request.form.get('cep')
        }
        cadastros.append(novo_cadastro)
        
        mensagem = "Cadastro realizado com sucesso!"
        return render_template('cadastro.html', mensagem=mensagem)
    
    return render_template('cadastro.html', mensagem=mensagem)

@app.route('/lista')
def lista():
    return render_template('lista.html', usuarios=cadastros)

if __name__ == '__main__':
    app.run(debug=True)