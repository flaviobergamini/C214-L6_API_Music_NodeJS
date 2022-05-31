# C214-L6_API_Music_NodeJS

<h1 align="center">Exercício de C214-L6 - API de Músicas em NodeJS</h1>

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW37ZpcD40st4W7b50uneItqSvLJ8XVdNtCAqw0wW9SOlkTWYAJfn09D7u3sL3fMGdNro&usqp=CAU">
</p>
Imagem retirada do site Mira Flores: http://www.aemiraflores.edu.pt/joomla2/  

### :books: Descrição

<p>Projeto de C214-L6, laboratório da disciplina de Engenharia de Software.</p>
<p>Projeto de uma API de Músicas com quatro endpoints para adicionar e buscar, atualizar e deletar informações no banco de dados.</p>
<p>Nesse repositório existe um cliente simples construído com Python, ele realiza o CRUD na API e pode ser usado tanto como aplicação de exemplo, quanto para testes de endpoits como alternativa ao Postman, Insomnia ou outro software cliente HTTP.</p>

#### Projeto
- Essa API foi desenvolvida em JavaScript usando o framework NodeJS. O banco de dados no qual ela se comunica é o MongoDB Atlas. 

### :computer: Funcionalidades dos Projetos
#### Funcionalidades
- Adiciona nova música na coleção do banco de dados MongoDB; 
- Lista todas as músicas cadastradas no banco de dados;
- Atualiza o nome de uma música baseada pelo nome da banda;
- Exclui uma música baseado pelo nome da banda.

### :hammer_and_wrench: Instalação e Execução
#### Preparação do ambiente no computador para executar a API
- [Git](https://git-scm.com/)
- [NodeJS](https://nodejs.org/en/)
- [Python](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Postman](https://www.postman.com/downloads/)
- [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=rlsavisitor&utm_source=google&utm_campaign=gs_americas_rlsamultirest_search_core_brand_atlas_desktop_rlsa&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=14412646314&adgroup=131761122132&gclid=Cj0KCQjw8_qRBhCXARIsAE2AtRYhQ9pEkjwdAhEn_dJbdPPKRTUtw5NzNf6zzq49qGy7K2n7S6ggQOQaAnhAEALw_wcB)


Observação: Você pode usar a IDE e o criente HTTP de sua preferência, o Visual Studio Code, o Postman ou o cliente Python são apenas sugestões.

Clone o repositório em seu computador para poder acessar o projeto:
```
git clone https://github.com/flaviobergamini/C214-L6_API_Music_NodeJS.git
```
Para acessar o repositório clonado usando o terminal, digite: 
```
cd C214-L6_API_Music_NodeJS
```
Para acessar os arquivos de código pelo terminal, digite:
```
cd API
```

#### Instalando as dependências
Na pasta API, instale as dependências do NodeJS usando o comando:
```
npm install
```
#### Iniciando Projeto
Após as instalações das dependências do projeto serem concluídas, inicie o projeto usando o comando:
```
npm start
```
#### Rotas
Dentro do Postman, ou outro cliente HTTP, utilize a URL:
```
http://localhost:6000
```
Se tiver conflito de portas em seu computador, vá até o arquivo "server.js" e altere o valor atribuído a constante "port".

A rota existente na API é: /music

* Método GET: /list, lista todas as músicas cadastradas no banco, acesse:
```
http://localhost:6000/music/list/
```
* Método POST: /create, realiza o cadastro das músicas no banco de dados MongoDB Atlas, acesse:
```
http://localhost:6000/music/create/
```
O envio das informações é feito por meio da Body em um objeto JSON contendo os seguintes campos e dados de exemplo:
```
{
    "name": "Moonlight Sonata",
    "band": "Ludwig Van Beethoven"
}
```
* Método PUT: /update, realiza a atualização do nome da música no banco de dados MongoDB Atlas com base no nome da banda:
```
http://localhost:6000/music/update/
```
O envio das informações é feito por meio da Body em um objeto JSON contendo os seguintes campos e dados de exemplo:
```
{
    "name": "Für Elise",
    "band": "Ludwig Van Beethoven"
}
```
* Método DELETE: /delete, realiza a exclusão da música no banco de dados MongoDB Atlas com base no nome da banda:
```
http://localhost:6000/music/delete/
```
O envio das informações é feito por meio da Body em um objeto JSON contendo os seguintes campos e dados de exemplo:
```
{
    "band": "Black Sabbath"
}
```

## Preparação do ambiente no computador para executar o cliente Python
Após a instalação do interpretador Python em seu computador, abra um terminal de linha de comando dentro da pasta "Client". Ao executar o comando para listar os arquivos, deverá encontrar o arquivo main.py e requirements.txt.

* Criando ambiente virtual para instalar as dependências do Python de maneira isolada:
```
python -m venv venv
```
* Iniciando ambiente virtual no Windows:
```
venv\Scripts\activate
```
* Iniciando ambiente virtual no Linux ou MAC:
```
source venv\bin\activate
```
* Instalando as dependências no ambiente virtual:
```
pip install -r requirements.txt
```
* Iniciando cliente Python (É necessário estar com a API NodeJS ativada):
```
python main.py
```
## :question: Dúvidas
Envie um email ao desenvolvedor: flaviohenrique@gec.inatel.br

## :gear: Autor

* **Flávio Henrique Madureira Bergamini** - [Flávio](https://github.com/flaviobergamini)

Sob a orientação da monitora:
* **Rafaela de Moraes Papale** - [Rafaela](https://github.com/RafaelaPapale)





