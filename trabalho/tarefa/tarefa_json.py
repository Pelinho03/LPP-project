import json
import os
from tarefa.tarefa import Tarefa

# Caminho base do projeto, usado para localizar o ficheiro de tarefas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "json", "tarefas.json")

# Função para carregar tarefas a partir de um ficheiro JSON


def carregar_tarefas(utilizadores=None):
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        tarefas = []
        for t in data:
            tarefa = Tarefa.from_dict(t)

            # Se houver lista de utilizadores, tenta associar a tarefa ao utilizador correto
            if utilizadores and "utilizador" in t:
                user_nome = t["utilizador"]
                user = next(
                    (u for u in utilizadores if u.nome == user_nome), None)
                if user:
                    tarefa.utilizador = user

            tarefas.append(tarefa)
        return tarefas

# Função para guardar tarefas no ficheiro JSON


def guardar_tarefas(tarefas):
    with open(FILENAME, "w", encoding="utf-8") as file:
        # Converte cada tarefa num dicionário antes de guardar
        json.dump([t.to_dict() for t in tarefas], file, indent=4)

# Método auxiliar para converter uma tarefa num dicionário (usado na exportação para JSON)


def to_dict(self):
    return {
        "id": self.id,
        "titulo": self.titulo,
        "descricao": self.descricao,
        "prioridade": self.prioridade,
        "prazo": self.prazo,
        "concluida": self.concluida,
        # Se existir um utilizador associado, guarda apenas o nome
        "utilizador": self.utilizador.nome if self.utilizador else None
    }

# Método estático para criar uma Tarefa a partir de um dicionário (usado ao carregar do JSON)


@staticmethod
def from_dict(data):
    tarefa = Tarefa(
        data["id"], data["titulo"], data["descricao"],
        data["prioridade"], data.get("prazo"), data["concluida"]
    )
    # Guarda temporariamente o nome do utilizador (associação feita depois)
    tarefa.utilizador_nome = data.get("utilizador")
    return tarefa
