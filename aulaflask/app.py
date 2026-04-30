from flask import Flask, render_template, request

# nao pode esquecer isso
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('olamundo.html')

@app.route('/tabuada', methods=['POST'])
def mostra_tabuada():
    numero = int(request.form['numero'])
    
    if 'bt01' in request.form:
        return render_template('tabuada.html', numero=numero)
    elif 'bt02' in request.form:
        return render_template('responder.html', numero=numero)
    return "opcao invalida"


@app.route('/respostas', methods=['POST'])
def conferir():
    numero = int(request.form['numero'])
    acertos = 0
    erros = 0
    
    # 1. A lista precisa ficar FORA do loop para não ser apagada toda vez
    respostas_detalhadas = [] 
    
    for i in range(1, 11):
        nome_entrada = f'entrada{i}'
        resposta_usuario = request.form.get(nome_entrada, '')
        resposta_correta = numero * i
        
        # 2. Vamos descobrir se a pessoa acertou ou não
        try:
            if int(resposta_usuario) == resposta_correta:
                acertos += 1
                status = 'acertou'
            else:
                erros += 1
                status = 'errou'
        except ValueError:
            erros += 1
            status = 'errou'
            
        # 3. Adicionamos TODAS as linhas na lista, independente se acertou ou errou
        respostas_detalhadas.append({
            'operacao': f'{numero} x {i}',
            'digitado': resposta_usuario if resposta_usuario else '(vazio)',
            'correto': resposta_correta,
            'status': status
        })
            
    # 4. Enviamos os totais e a lista detalhada para o HTML
    return render_template('respostas.html', acerto=acertos, erro=erros, detalhes=respostas_detalhadas)

if __name__ == '__main__':
    app.run()