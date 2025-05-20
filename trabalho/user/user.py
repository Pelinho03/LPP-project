class User:
    def __init__(self, nome, email, grupo="user"):
        self.nome = nome
        self.email = email
        self.grupo = grupo
        self.tarefas = []

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "grupo": self.grupo
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["email"], data.get("grupo", "user"))

    def adicionar_tarefa(self, tarefa):
        if tarefa not in self.tarefas:
            self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
        else:
            print("Tarefa não encontrada na lista de tarefas.")

    def listar_tarefas(self):
        return self.tarefas

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Tarefas: {len(self.tarefas)}"
