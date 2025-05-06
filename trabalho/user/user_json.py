import json
import os
from user.user import User

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "json", "utilizadores.json")


def carregar_utilizadores():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [User.from_dict(user) for user in data]


def guardar_utilizadores(utilizadores):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump([user.to_dict() for user in utilizadores], file, indent=4)
