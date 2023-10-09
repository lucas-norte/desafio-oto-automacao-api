import httpx
from behave import given, when, then

token = None
message = None

@given('que o usuário possui uma URL base "{base_url}"')
def step_given_base_url(context, base_url):
    context.base_url = base_url

@when('o usuário faz uma solicitação POST para o endpoint "{endpoint}" e efetua o login')
def step_when_post_login(context, endpoint):
    url = context.base_url + endpoint
    data = context.text
    headers = {"Content-Type": "application/json"}

    with httpx.Client() as client:
        response = client.post(url, data=data, headers=headers)
        context.response = response

@then('a API retorna o status code "{status_code}"')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)

@then('a API retorna um token')
def step_then_check_token(context):
    global token
    response_data = context.response.json()
    assert "token" in response_data, "Token não encontrado na resposta"
    token = response_data["token"]

@then('a API retorna uma mensagem')
def step_then_check_token(context):
    global message
    response_data = context.response.json()
    assert "error" in response_data, "Menssagem não encontrada na resposta"
    message = response_data["error"]
