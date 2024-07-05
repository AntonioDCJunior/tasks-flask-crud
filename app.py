#Este arquivo é necessário para criar a plicação flask

from flask import Flask

#a variavel __name__ significa que é o nome do arquivo
#esse name tem o mesmo valor do "main" (__name__=="__main__")
app = Flask(__name__)

#criando rota (endpoint), que serve para comunicar com outros clientes
@app.route("/")
#após definir a rota, deve-se criar o que será executado a partir dela
#nesse caso cria-se uma função
def hello_world():
    return "Hello World"

@app.route("/about")
def sobre():
    return "Página Sobre"

#é necessário realizar a comparação se o "name" é igual a "main"
#para garantir que após a execução manual, o servidor irá subir
#essa forma é utilizada APENAS para desenvolvimento LOCAL
#ao usar em ambiente de produção para outros cliente utilizar a implementação é de outra maneira

if __name__ == "__main__":
    #é necessária a propriedaded "debug" para que sejam verificadas as informações 
    #que serão exibidas no servidor web, para ajudar a entender o que está acontecendo
    app.run(debug=True)