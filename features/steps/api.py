import httpx
from behave import step
from features.services.login_endpoint import LoginEndpoint

# Fluxo Base
@step("que o usuario possui dados validos")
def step_impl(context):
    context.payload = '{"email": "eve.holt@reqres.in", "password": "cityslicka"}'

@step('o usuario faz um POST para o login')
def step_when_post_login(context):
    login = LoginEndpoint()
    context.response = login.send_request(context.payload)

@step('a API retorna o status code "{status_code}"')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)

@step('a API retorna um token "{expected_token}"')
def step_then_check_token(context, expected_token):
    response_data = context.response.json()
    assert "token" in response_data, "Token não encontrado na resposta"
    returned_token = response_data.get("token")
    assert returned_token == expected_token, f"Token esperado: {expected_token}, Token retornado: {returned_token}"


# Fluxo de Excecao
@step("que o usuario nao esta cadastrado")
def step_impl(context):
    context.payload = '{"email": "lucasnorte.qa@gmail.com", "password": "cityslicka"}'

@step('a API retorna uma mensagem "{expected_message}"')
def step_then_check_message(context, expected_message):
    response_data = context.response.json()
    assert "error" in response_data, "Menssagem não encontrada na resposta"
    returned_message = response_data.get("error")
    assert returned_message == expected_message, f"Mensagem esperada: {expected_message}, Mensagem retornada: {returned_message}"


# Fluxo de Excecao
@step("que o usuario nao lembra da senha")
def step_impl(context):
    context.payload = '{"email": "eve.holt@reqres.in", "password": "#####"}'
