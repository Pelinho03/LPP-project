import json
import os
from user.user import User

# Define o caminho base do projeto e o ficheiro JSON onde serão guardados os utilizadores
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "json", "utilizadores.json")


def carregar_utilizadores():
    """Carrega a lista de utilizadores a partir do ficheiro JSON.
    Retorna uma lista vazia se o ficheiro não existir."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Converte cada dicionário de utilizador num objeto User
        return [User.from_dict(user) for user in data]


def guardar_utilizadores(utilizadores):
    """Guarda a lista de utilizadores no ficheiro JSON.
    Converte cada objeto User num dicionário antes de guardar."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump([user.to_dict() for user in utilizadores], file, indent=4)
