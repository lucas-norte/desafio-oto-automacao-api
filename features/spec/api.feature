#language:pt
Funcionalidade: Login via API

  Cenario: Login com Sucesso
    Dado que o usuario possui dados validos
    Quando o usuario faz um POST para o login
    Então a API retorna o status code "200"
    E a API retorna um token "QpwL5tke4Pnpja7X4"

  Cenario: Login com usuario nao cadastrado
    Dado que o usuario nao esta cadastrado
    Quando o usuario faz um POST para o login
    Entao a API retorna o status code "400"
    E a API retorna uma mensagem "user not found"

  Cenario: Login com senha invalida
    Dado que o usuario nao lembra da senha
    Quando o usuario faz um POST para o login
    Entao a API retorna o status code "400"
    E a API retorna uma mensagem "senha invalida"
