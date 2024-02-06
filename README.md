# API para Cotação de Frete
Criação de uma API para cotar o valor do frete com transportadoras parceiras

## O Desafio
O KaBuM necessita realizar cotações de fretes em suas transportadoras parceiras e você, como desenvolvedor back-end, deve desenvolver uma API REST que será utilizada pelo site para a consulta de opções de transportes dos produtos.
- [ ] O candidato terá que ser capaz de construir uma API REST.
- [ ] O teste está baseado em uma consulta dos valores de frete para cada transportadora existente conforme as especificações das dimensões e peso do produto.
- [ ] Cada transportadora terá seus requisitos e o retorno deverá ser conforme o exemplo “output”, uma listagem com as transportadoras e seus valores de frete. Se o produto não estiver de acordo com tal transportadora, ela não deverá ser retornada.
- [ ] A requisição deverá ser via POST e as informações do produto deverão ser enviadas body da requisição, como JSON.
```JSON
{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}
```
- A medida da dimensão é centímetro (cm) e a medida do peso é gramas (g).
- Caso nenhuma transportadora atenda o produto, deverá ser retornada uma lista vazia.

### Validações
Ao receber uma requisição, a API deve realizar as seguintes validações para retornar ou não a opção do frete:
- Validação de altura máxima e mínima para cada opção de frete
- Validação de largura máxima e mínima para cada opção de frete
- Validação se o peso do produto é maior que 0.
Caso alguma validação não seja satisfeita, a opção do frete não deve ser retornada!

### Cálculo do valor do frete
- Caso todas as validações do payload recebido sejam válidas, o cálculo do valor do frete muda de transportadora para transportadora.
- Disponibilizamos logo abaixo uma constante para calcular esse valor.
- Para isso, utilize a fórmula abaixo e calcule o valor do frete:
```
(Peso x constante_frete) / 10
````

### Opções de Frete
**1. Entrega Ninja:**
- Constante para cálculo do frete: 0.3
- Altura mínima: 10 cm
- Altura máxima: 200 cm
- Largura mínima: 6 cm
- Largura máxima: 140 cm
- Prazo para entrega: 6 dias

**2. Entrega KaBuM:**
- Constante para cálculo do frete: 0.2
- Altura mínima: 5 cm
- Altura máxima: 140 cm
- Largura mínima: 13 cm
- Largura máxima: 125 cm
- Prazo para entrega: 4 dias

## Exemplos
### Input
```JSON
{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}
```
### Output
```JSON
[
	{
        "nome":"Entrega Ninja",
    	  "valor_frete": 12.00,
    	  "prazo_dias": 6
	},
	{
    	  "nome":"Entrega KaBuM",
    	  "valor_frete": 8.00,
    	  "prazo_dias": 4
	}
]
```
-------

### Input
```JSON
{
    "dimensao": {
                    "altura":152,
                    "largura":50
                },
    "peso":850
}
```
### Output
```JSON
[
	{
        "nome":"Entrega Ninja",
        "valor_frete": 25.50,
    	"prazo_dias": 6
	}
]
```
-------

### Input
```JSON
{
    "dimensao": {
                    "altura":230,
                    "largura":162
                },
    "peso":5600
}
```
### Output
```JSON
[]
```
# Execução do Desafio


### Configuração de Ambiente e Requisitos
1. Python 3 - `$ brew install python@3.12`
2. Gerenciador de Pacoter PIP -  `$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` e depois execute o arquivo baixado `$ python3 get-pip.py`.

### Dependências Iniciais
Para instalar as dependências do projetos, utiliza-se um ambiente virtual dentro do diretório que ficará o projeto.
````
python3 -m venv .venv
````
Para ativar a virtualenv
````
# Mac e Linux
source .venv/bin/activate

# Windows Power Shell
.\venv\Scripts\activate.ps1
````
Cria-se um arquivo `requirements-dev.txt` com as ferramentas de produtividade abaixo para ser instaladas em nosso ambiente:
````
ipython         # terminal
ipdb            # debugger
sdb             # debugger remoto
pip-tools       # lock de dependencias
pytest          # execução de testes
pytest-order    # ordenação de testes
httpx           # requests async para testes
black           # auto formatação
flake8          # linter
````
E para instalar as dependências iniciais acima devemos rodar o gerenciador **pip**
````
pip install --upgrade pip
pip install -r requirements-dev.txt
````
### Estrutura de Arquivos e Pastas
Script para criar arquivos do projeto
````
# Arquivos na raiz
touch setup.py
touch {settings,.secrets}.toml
touch {requirements,MANIFEST}.in
touch Dockerfile.dev docker-compose.yaml

# Aplicação
mkdir -p shippingPriceAPI/{models,routes}
touch shippingPriceAPI/default.toml
touch shippingPriceAPI/{__init__,cli,app,config}.py
touch shippingPriceAPI/models/{__init__,post}.py
touch shippingPriceAPI/routes/{__init__,post}.py

# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py
````
Para visualizar a estrutura no terminal pode utilizar o comando tree (`$ brew install tree`)
````
❯ tree -a --filesfirst -L 3 -I docs -I .venv -I .git
.
├── docker-compose.yaml        # Orquestração de containers
├── Dockerfile.dev             # Imagem principal
├── MANIFEST.in                # Arquivos incluidos na aplicação
├── requirements-dev.txt       # Dependencias de ambiente dev
├── requirements.in            # Dependencias de produção
├── .secrets.toml              # Senhas locais
├── settings.toml              # Configurações locais
├── setup.py                   # Instalação do projeto
├── test.sh                    # Pipeline de CI em ambiente dev
├── shippingPriceAPI
│   ├── __init__.py
│   ├── app.py                 # FastAPI app
│   ├── cli.py                 # Aplicação CLI `$ shippingPriceAPI adduser` etc
│   ├── config.py              # Inicialização da config
│   ├── default.toml           # Config default
│   ├── models
│   │   ├── __init__.py
│   │   └──post.py             # ORM e Serializers de posts
│   └── routes
│       ├── __init__.py
│       └──post.py             # CRUD de posts e likes
└── tests
    ├── conftest.py            # Config do Pytest
    ├── __init__.py
    └── test_api.py            # Tests da API
````
###  Adicionando as dependencias
No arquivo `requirements.in` adicionamos as depedências que iremos usar sem setar as suas versões, pois será sobrescrita com as versões atuais quando compilar.
```
fastapi                      # Framework pra desenvolver API
uvicorn                      # Servidor Web que funciona no protocolo ASGI
typer                        # Permite utilizar linhas de comando para administrar o projeto
dynaconf                     # Gerencia as configurações e facilitar o uso de cloud e containers
jinja2                       # Biblioteca para fazer templates
rich                         # Criar tabela no terminal
```
Com isso iremos compilar esse arquivo no qual gerará o arquivo `requirements.txt` com os locks das versões pinadas garantidas.
````
pip-compile requirements.in
````
### API Base
Vamos editar o arquivo `shippingPriceAPI/app.py`
```py
from fastapi import FastAPI;

app = FastAPI(
    title="Shipping Price API",
    version="0.2.0",
    description="API to check delivery prices and compare shipping companies",
)
```
### Tornando a aplicação instalável
`MANIFEST.in` pega tudo que está no diretório e transforma em pacote.
```
graft shippingPriceAPI
```
`setup.py`
````py
import io
import os
from setuptools import find_packages, setup

def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="shippingPriceAPI",
    version="0.2.0",
    description="API to check delivery prices and compare shipping companies",
    url="shippingPriceAPI.io",
    python_requires=">=3.8",
    long_description="Shipping Price API developed with FastAPI Framework for Python to check delivery prices and compare shipping companies",
    long_description_content_type="text/markdown",
    author="Otthon Leao",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["shippingPriceAPI = shippingPriceAPI.cli:main"]
    }
)
````
### Instalação
O objetivo é instalar a aplicação dentro do container, porém é recomendável que instale também no ambiente local pois desta maneira auto complete do editor irá funcionar.
````
pip install -e .
`````
Para verificar se o entry_point está funcionando como um comando no terminal pode verificar no VSCode > Preferencias > Python: Select Interpreter

### Docker
No `dockerfile.dev` vamos escrever a imagem do container do projeto que será inicializado.
````docker
# Build the app image
FROM python:3.10

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV APP_HOME=/home/app/api
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# install
COPY . $APP_HOME
RUN pip install -r requirements-dev.txt
RUN pip install -e .

RUN chown -R app:app $APP_HOME
USER app

CMD ["uvicorn","shippingPriceAPI.app:app","--host=0.0.0.0","--port=8000","--reload"]

````
No terminal buildamos o container, no mesmo caminho do arquivo `Dockerfile.dev` e depois executamos:
```
$ docker build -f Dockerfile.dev -t shippingprice:latest .
$ docker run --rm -it -v $(pwd):/home/app/api -p 8000:8000 shippingprice
```
Após iniciar o container acesse: http://0.0.0.0:8000/docs ou http://0.0.0.0:8000/redoc para te acesso a documentação
