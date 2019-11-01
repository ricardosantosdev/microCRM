# microCRM
PoC de um CRM criado com Django.

## Instalação

1. Clone o repositório para a sua máquina com o comando:

`git clone https://github.com/ricardosantosdev/microCRM.git`

2. Instale as dependências necessárias:

`pip install -r requirements.txt`

3. Rode o comando para criar as tabelas do banco de dados:

`python manage.py makemigrations`

4. Crie as tabelas:

` python manage.py migrate`

5. E finalmente rode a aplicação:

`python manage.py runserver`

## Notas

Esse modo de instalação serve para testar a aplicação localmente, se por qualquer motivo você precisar da informação de outras formas de deploy dessa aplicação abra uma issue e eu ficarei feliz em ajudar.

## Contribuindo

Como essa aplicação tem fins didáticos a issue [#1](https://github.com/ricardosantosdev/microCRM/issues/1) é para incentivar os estudos, todos os PR serão aceitos.