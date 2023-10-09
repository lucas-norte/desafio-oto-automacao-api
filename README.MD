# Desafio Oto Automação API 

### Este é um projeto Python e foi criado conforme requisito abaixo, utilizando os seguintes recursos:

<!--ts-->
   * [Behave;](#https://behave.readthedocs.io/en/latest/)
   * [HTTPX;](#https://www.python-httpx.org/)
* [API utilizada](#https://reqres.in/)
    - https://reqres.in/
<!--te-->

### Avisos Importantes: 

Para utilizar localmente

<!--ts-->
   * Precisar instalar o Behave

 ```bash
pip install behave
```
   
   * Precisa instalar o HTTPX

 ```bash
pip install httpx
```

Após instalações bem sucedidas, basta rodar o comando ```behave``` dentro do projeto:

<!--te-->

### Planejamento de Testes 

 ```gherkin
Funcionalidade: Login via API

    Cenario: Login com SUCESSO
    Cenario: Login com usuario nao cadastrado
    Cenario: Login com senham invalida
```
