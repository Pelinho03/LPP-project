import json
import os
from tarefa.tarefa import Tarefa

FILENAME = "json/tarefas.json"


def carregar_tarefas(utilizadores=None):
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
        tarefas = []
        for t in data:
            tarefa = Tarefa.from_dict(t)
            if utilizadores and "utilizador" in t:
                user_nome = t["utilizador"]
                user = next(
                    (u for u in utilizadores if u.nome == user_nome), None)
                if user:
                    tarefa.utilizador = user
            tarefas.append(tarefa)
        return tarefas


def guardar_tarefas(tarefas):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump([t.to_dict() for t in tarefas], file, indent=4)


def to_dict(self):
    return {
        "id": self.id,
        "titulo": self.titulo,
        "descricao": self.descricao,
        "prioridade": self.prioridade,
        "prazo": self.prazo,
        "concluida": self.concluida,
        "utilizador": self.utilizador.nome if self.utilizador else None
    }


@staticmethod
def from_dict(data):
    tarefa = Tarefa(
        data["id"], data["titulo"], data["descricao"],
        data["prioridade"], data.get("prazo"), data["concluida"]
    )
    tarefa.utilizador_nome = data.get("utilizador")
    return tarefa
