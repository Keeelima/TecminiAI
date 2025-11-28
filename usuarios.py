import json
import os



ARQUIVO_USUARIOS = "usuarios.json"
usuario_logado = None


# Carregar e salvar usuários

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {"users": []}

    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"users": []}


def salvar_usuarios(dados):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)



# Login

def usuario_existe(username):
    dados = carregar_usuarios()
    return any(u["username"] == username for u in dados["users"])


def validar_login(username, senha):
    dados = carregar_usuarios()
    for u in dados["users"]:
        if u["username"] == username and u["password"] == senha:
            return True
    return False


def criar_usuario(nome, username, senha):
    dados = carregar_usuarios()

    if usuario_existe(username):
        return False

    dados["users"].append({
        "nome": nome,
        "username": username,
        "password": senha,
        "memory": {}
    })

    salvar_usuarios(dados)
    return True



# Memória

def carregar_memoria(username):
    dados = carregar_usuarios()

    for u in dados["users"]:
        if u["username"] == username:
            if "memory" not in u:
                u["memory"] = {}
                salvar_usuarios(dados)
            return u["memory"]

    return {}


def salvar_memoria(username, memoria):
    dados = carregar_usuarios()

    for u in dados["users"]:
        if u["username"] == username:
            u["memory"] = memoria
            break

    salvar_usuarios(dados)
