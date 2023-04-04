Para clonar o repositório e configurar o ambiente virtual, siga os passos abaixo:

1. Clone o repositório utilizando a chave SSH:

git clone git@github.com:BiblioteKa-M5-group18/Biblioteka-M5.git

2. Acesse o diretório do projeto:

cd Biblioteka-M5

3. Crie um ambiente virtual com Python e ative-o:

python -m venv venv

source venv/bin/activate

4. Instale as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt

5. Execute as migrações do banco de dados:

python manage.py migrate
