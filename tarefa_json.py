import json  # Módulo para ler e escrever arquivos JSON
import os  # Módulo para operações com caminhos de arquivos e diretórios
from tarefa.tarefa import Tarefa  # Importa a classe Tarefa do módulo correspondente

# Define o caminho base do projeto (diretório acima do atual)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho completo para o arquivo de tarefas em formato JSON
FILENAME = os.path.join(BASE_DIR, "json", "tarefas.json")

# Função para carregar as tarefas do ficheiro JSON
def carregar_tarefas(utilizadores=None):
    # Se o ficheiro não existir, retorna uma lista vazia
    if not os.path.exists(FILENAME):
        return []

    # Abre o ficheiro e carrega os dados JSON
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)  # Lista de dicionários
        tarefas = []

        for t in data:
            tarefa = Tarefa.from_dict(t)  # Converte dicionário para objeto Tarefa
            # Se a lista de utilizadores for fornecida e houver um utilizador associado na tarefa
            if utilizadores and "utilizador" in t:
                user_nome = t["utilizador"]
                # Procura o utilizador com o nome correspondente
                user = next((u for u in utilizadores if u.nome == user_nome), None)
                if user:
                    tarefa.utilizador = user  # Associa o objeto utilizador à tarefa
            tarefas.append(tarefa)
        return tarefas  # Retorna a lista de objetos Tarefa

# Função para guardar a lista de tarefas no ficheiro JSON
def guardar_tarefas(tarefas):
    with open(FILENAME, "w", encoding="utf-8") as file:
        # Serializa as tarefas em dicionários e escreve no ficheiro com indentação
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
