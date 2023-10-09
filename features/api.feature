#language:pt
Funcionalidade: Login via API
  Cenário: Login com Sucesso
  Dado que o usuário possui uma URL base "https://reqres.in"
  Quando o usuário faz uma solicitação POST para o endpoint "/api/login" e efetua o login 
    """
      {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
      }
    """
  Então a API retorna o status code "200"
  E a API retorna um token
      """
      {
        "token": "QpwL5tke4Pnpja7X4"
      }
      """

  Cenário: Login com usuário não cadastrado
  Dado que o usuário possui uma URL base "https://reqres.in"
  Quando o usuário faz uma solicitação POST para o endpoint "/api/login" e efetua o login 
    """
      {
        "email": "lucasnorte.qa@gmail.com",
        "password": "cityslicka"
      }
    """
  Então a API retorna o status code "400"
  E a API retorna uma mensagem
      """
      {
        "error": "user not found"
      }
      """

  Cenário: Login com senha inválida
  Dado que o usuário possui uma URL base "https://reqres.in"
  Quando o usuário faz uma solicitação POST para o endpoint "/api/login" e efetua o login 
    """
      {
        "email": "eve.holt@reqres.in",
        "password": "#####"
      }
    """
  Então a API retorna o status code "400"
  E a API retorna uma mensagem
      """
      {
        "error": "senha invalida"
      }
      """

