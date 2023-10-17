import httpx
from behave import given, when, then

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

@then('a API retorna um token "{expected_token}"')
def step_then_check_token(context, expected_token):
    response_data = context.response.json()
    assert "token" in response_data, "Token não encontrado na resposta"
    returned_token = response_data.get("token")
    
    assert returned_token == expected_token, f"Token esperado: {expected_token}, Token retornado: {returned_token}"

@then('a API retorna uma mensagem "{expected_message}"')
def step_then_check_message(context, expected_message):
    response_data = context.response.json()
    assert "error" in response_data, "Menssagem não encontrada na resposta"
    returned_message = response_data.get("error")
    
    assert returned_message == expected_message, f"Mensagem esperada: {expected_message}, Mensagem retornada: {returned_message}"