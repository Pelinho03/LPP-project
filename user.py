class User:
    # Método construtor: inicializa um novo objeto User com nome, email, grupo (padrão 'user') e uma lista de tarefas vazia.
    def __init__(self, nome, email, grupo="user"):
        self.nome = nome                  # Nome do utilizador
        self.email = email                # Email do utilizador
        self.grupo = grupo                # Grupo a que o utilizador pertence (por exemplo, 'user' ou 'admin')
        self.tarefas = []                 # Lista que irá armazenar as tarefas atribuídas a este utilizador

    # Converte o objeto User em um dicionário (útil para serialização, como salvar em JSON)
    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "grupo": self.grupo
        }

    # Método de classe que cria um objeto User a partir de um dicionário (deserialização)
    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["email"], data.get("grupo", "user"))  # Usa 'user' como valor padrão para grupo

    # Adiciona uma tarefa à lista de tarefas se ainda não estiver presente
    def adicionar_tarefa(self, tarefa):
        if tarefa not in self.tarefas:
            self.tarefas.append(tarefa)

    # Remove uma tarefa da lista de tarefas se ela existir; caso contrário, imprime uma mensagem de erro
    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
        else:
            print("Tarefa não encontrada na lista de tarefas.")

    # Retorna a lista de tarefas atribuídas ao utilizador
    def listar_tarefas(self):
        return self.tarefas

    # Representação textual do objeto User, útil para debugging ou exibição
    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Tarefas: {len(self.tarefas)}"
