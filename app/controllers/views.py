from app import app
from flask import render_template, request


@app.route("/buscar")
def buscar():
    nome_produto = request.args.get('nome') # pega o valor enviado pela URL (?nome=Fulano)
    produto = ['notbook','iphone','smarthphone','monitor','teclado']
    if nome_produto:
        return render_template('buscar.html', nome = produto)

    return render_template('buscar.html', nome = None)


    

@app.route("/mensagem", methods=['GET', 'POST'])
def mensagem():
    if request.method == 'POST':
        nome = request.form.get('nome')
        mensagem = request.form.get('mensagem')
        return render_template('mensagem.html', nome=nome, mensagem=mensagem)
    
    return render_template('mensagem.html', nome=None, mensagem=None)

