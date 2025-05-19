from pymongo import MongoClient

# Conectar ao MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")

# Criar ou acessar o banco de dados e a coleção
db = client["meu_banco"]
colecao = db["usuarios"]

# Inserir documentos
usuario_unico = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}
colecao.insert_one(usuario_unico)

usuarios = [
    {"nome": "Bruno", "idade": 25, "cidade": "Rio"},
    {"nome": "Clara", "idade": 29, "cidade": "Belo Horizonte"},
    {"nome": "Daniel", "idade": 35, "cidade": "Curitiba"}
]
colecao.insert_many(usuarios)

# Consultar documentos
print("\n📄 Todos os documentos:")
for user in colecao.find():
    print(user)

print("\n🔍 Buscar um documento (nome: Ana):")
print(colecao.find_one({"nome": "Ana"}))

print("\n🧮 Buscar usuários com idade > 28:")
for user in colecao.find({"idade": {"$gt": 28}}):
    print(user)

# Atualizar documentos
colecao.update_one(
    {"nome": "Ana"},
    {"$set": {"idade": 31}}
)

colecao.update_many(
    {"cidade": "Rio"},
    {"$set": {"estado": "RJ"}}
)

# Deletar documentos
colecao.delete_one({"nome": "Bruno"})
colecao.delete_many({"cidade": "Belo Horizonte"})

# Projeção: mostrar só os nomes
print("\n🔎 Somente nomes dos usuários:")
for user in colecao.find({}, {"_id": 0, "nome": 1}):
    print(user)

# Criar índice
colecao.create_index("nome")

print("\n✅ Operações concluídas.")
