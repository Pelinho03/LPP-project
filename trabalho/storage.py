import json
import os
from models import Tarefa

FILENAME = "config.json"

def carregar_tarefas():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Tarefa.from_dict(tarefa) for tarefa in data]

def guardar_tarefas(tarefas):
     with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump([tarefa.to_dict() for tarefa in tarefas], file, indent=4)