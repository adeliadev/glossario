# Importa as classes e funções necessárias do módulo Flask
from flask import Flask, render_template, request, redirect, url_for

# Cria uma instância da classe Flask
app = Flask(__name__)

# Lista inicial de termos e definições no glossário
glossario = [
    {'termo': 'Termo1', 'definicao': 'Definição1'},
    {'termo': 'Termo2', 'definicao': 'Definição2'},
]

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o template 'index.html' passando o glossário como argumento
    return render_template('index.html', glossario=glossario)

# Rota para excluir um termo do glossário
@app.route('/excluir/<termo>', methods=['POST'])
def excluir(termo):
    # Itera sobre os itens do glossário
    for entry in glossario:
        # Verifica se o termo atual corresponde ao termo a ser excluído
        if entry['termo'] == termo:
            # Remove o termo do glossário
            glossario.remove(entry)
            break
    # Redireciona de volta à página inicial após a exclusão
    return redirect(url_for('index'))

# Rota para editar um termo do glossário
@app.route('/editar/<int:indice>', methods=['GET'])
def editar(indice):
    # Renderiza o template 'editar.html' passando o termo e a definição a serem editados
    return render_template('editar.html', termo=glossario[indice]['termo'], definicao=glossario[indice]['definicao'])

# Rota para atualizar um termo do glossário após a edição
@app.route('/atualizar/<termo>', methods=['POST'])
def atualizar(termo):
    # Itera sobre os itens do glossário
    for entry in glossario:
        # Verifica se o termo atual corresponde ao termo a ser atualizado
        if entry['termo'] == termo:
            # Atualiza o termo e a definição com os valores do formulário enviado
            entry['termo'] = request.form.get('termo')
            entry['definicao'] = request.form.get('definicao')
            break
    # Redireciona de volta à página inicial após a atualização
    return redirect(url_for('index'))

# Rota para adicionar um novo termo ao glossário
@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Obtém os valores do formulário para o novo termo e definição
    novo_termo = request.form.get('termo')
    nova_definicao = request.form.get('definicao')
    # Adiciona um novo item ao glossário
    glossario.append({'termo': novo_termo, 'definicao': nova_definicao})
    # Redireciona de volta à página inicial após a adição
    return redirect(url_for('index'))

# Executa a aplicação Flask se este script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
