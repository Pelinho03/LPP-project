import json
import os
from user.user import User  # Importa a classe User do módulo user/user.py

# Define o caminho base do projeto, subindo dois níveis a partir do ficheiro atual
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define o caminho completo para o ficheiro JSON onde os utilizadores serão armazenados
FILENAME = os.path.join(BASE_DIR, "json", "utilizadores.json")


# Função para carregar os utilizadores a partir do ficheiro JSON
def carregar_utilizadores():
    # Se o ficheiro não existir, retorna uma lista vazia
    if not os.path.exists(FILENAME):
        return []
    # Abre o ficheiro em modo leitura e carrega os dados JSON
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Converte cada dicionário em um objeto User utilizando o método from_dict
        return [User.from_dict(user) for user in data]


# Função para guardar a lista de utilizadores no ficheiro JSON
def guardar_utilizadores(utilizadores):
    # Abre o ficheiro em modo escrita e escreve os dados formatados como JSON
    with open(FILENAME, "w", encoding="utf-8") as file:
        # Converte cada objeto User em dicionário usando to_dict e grava no ficheiro
        json.dump([user.to_dict() for user in utilizadores], file, indent=4)
