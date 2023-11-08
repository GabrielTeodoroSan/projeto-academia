# API de Gerenciamento de Academia
===

## Explicando o uso da API:

Esta api centraliza as operações de controle de acesso em uma academia de condomínio. Outros serviços que consumirem esta api vão poder visualizar os horários disponíveis de uso da academia e marcarem seus horários de uso, a api retorna-ra um qr_code para cada horário reservado.

## Lista de endpoints: 

* /user/create/ -> Serve para criar um novo usuário (Haverá mudanças).
* /tickets/show/ -> Retorna os horários disponíveis na academia. 
* /tickets/mark/ -> Marca o horário desejado na academia.

## Como testar esta api: 

Primeiramente baixe o projeto em sua máquina, garantindo também que você possua o python 3.10.12

`git clone https://github.com/GabrielTeodoroSan/projeto-academia`

Agora crie um ambiente virtualizado:

(Windows)

```
pip install venv
py -m venv vevn
```

(Linux)

`apt-get install virtualenv; virtualenv venv`

Acesse o ambiente virtual e instale as dependências da aplicação.

`pip install -r requirements.txt`

Finalmente, rode a aplicação com o seguinte comando.

`uvicorn main:app --reload`

![Isso é um meme](./fabiogiga-dançando.gif.crdownload)