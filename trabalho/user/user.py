class User:
    def __init__(self, nome, email, grupo="user"):
        # Inicializa um utilizador com nome, email e grupo (por defeito "user")
        self.nome = nome
        self.email = email
        self.grupo = grupo  # Ex: "admin", "dev", "user"
        self.tarefas = []   # Lista de tarefas atribuídas a este utilizador

    def to_dict(self):
        # Converte o utilizador num dicionário (ideal para serialização)
        return {
            "nome": self.nome,
            "email": self.email,
            "grupo": self.grupo
        }

    @classmethod
    def from_dict(cls, data):
        # Cria uma instância de User a partir de um dicionário (deserialização)
        return cls(data["nome"], data["email"], data.get("grupo", "user"))

    def adicionar_tarefa(self, tarefa):
        # Adiciona uma tarefa se ainda não estiver na lista
        if tarefa not in self.tarefas:
            self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        # Remove a tarefa da lista, se existir
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
        else:
            print("Tarefa não encontrada na lista de tarefas.")

    def listar_tarefas(self):
        # Devolve a lista de tarefas atribuídas
        return self.tarefas

    def __str__(self):
        # Mostra uma string representativa do utilizador
        return f"Nome: {self.nome}, Email: {self.email}, Tarefas: {len(self.tarefas)}"
