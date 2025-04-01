class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, prazo=None, concluida=False):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "concluida": self.concluida
        }

    @staticmethod
    def from_dict(data):
        return Tarefa(
            data["id"], data["titulo"], data["descricao"],
            data["prioridade"], data.get("prazo"), data["concluida"]
        )
