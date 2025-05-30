# ✅ Usando o MongoDB Compass (Interface Gráfica)
1. Abrir o MongoDB Compass
Se você já instalou o MongoDB Compass (uma interface gráfica do MongoDB), siga esses passos:

Abra o MongoDB Compass.

Na tela inicial, você verá uma caixa de conexão. Preencha os campos conforme necessário:

Connection String URI:
Se você estiver rodando o MongoDB localmente, use:

arduino
Copiar
Editar
mongodb://localhost:27017
Clique em "Connect".

2. Criando um Banco de Dados
Depois de conectado, siga estes passos para criar um banco de dados e coleções no Compass:

No painel esquerdo, clique em "Create Database".

Escolha um nome para seu banco de dados (por exemplo, meu_banco).

Adicione uma coleção (exemplo: usuarios).

Clique em "Create Database".

3. Inserindo Documentos
Agora, você pode adicionar documentos manualmente ou por meio de comandos no Compass:

Selecione a coleção usuarios que você criou.

Clique em "Insert Document" no canto superior direito.

Adicione o conteúdo do seu documento em formato JSON, por exemplo:

json
Copiar
Editar
{ "nome": "Ana", "idade": 30, "cidade": "São Paulo" }
Clique em "Insert" para adicionar o documento.

4. Consultar Dados
Para consultar os dados da coleção, basta clicar em "Find" no MongoDB Compass. Ele irá mostrar todos os documentos da coleção usuarios.

✅ Usando o Mongo Shell (Terminal)
Se você quiser usar o Mongo Shell diretamente no seu terminal (sem Python ou VS Code), siga estas etapas:

1. Abrir o Mongo Shell
No terminal, digite:

bash
Copiar
Editar
mongosh
Se você estiver no Windows, talvez precise usar o comando:

bash
Copiar
Editar
mongo
O Mongo Shell se conectará ao seu MongoDB local.

2. Selecionar o Banco de Dados
Use o comando use para criar ou acessar um banco de dados:

javascript
Copiar
Editar
use meu_banco
Isso criará (ou acessará) o banco de dados meu_banco.

3. Criar uma Coleção e Inserir Dados
Agora, insira um documento na coleção usuarios:

javascript
Copiar
Editar
db.usuarios.insertOne({ nome: "Ana", idade: 30, cidade: "São Paulo" })
Isso irá criar o documento. Para adicionar vários documentos:

javascript
Copiar
Editar
db.usuarios.insertMany([
    { nome: "Bruno", idade: 25, cidade: "Rio" },
    { nome: "Clara", idade: 29, cidade: "Belo Horizonte" }
])
4. Consultar Dados
Para ver todos os dados na coleção:

javascript
Copiar
Editar
db.usuarios.find()
Para buscar documentos com idade maior que 25:

javascript
Copiar
Editar
db.usuarios.find({ idade: { $gt: 25 } })
5. Atualizar Dados
Para atualizar o documento de "Ana", alterando a idade:

javascript
Copiar
Editar
db.usuarios.updateOne({ nome: "Ana" }, { $set: { idade: 31 } })
6. Deletar Dados
Para deletar um documento:

javascript
Copiar
Editar
db.usuarios.deleteOne({ nome: "Bruno" })
Ou para excluir todos os documentos com idade menor que 30:

javascript
Copiar
Editar
db.usuarios.deleteMany({ idade: { $lt: 30 } })
🎯 Resumo
Agora você pode usar tanto a interface gráfica (MongoDB Compass) quanto o Mongo Shell para interagir diretamente com seu banco de dados MongoDB!

Se precisar de mais algum exemplo ou ajuda para rodar mais comandos, é só avisar!
