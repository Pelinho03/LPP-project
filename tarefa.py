class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, prazo=None, concluida=False, utilizador=None, bloqueada=False):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida
        self.utilizador = utilizador
        self.bloqueada = bloqueada  # NOVO

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "concluida": self.concluida,
            "utilizador": self.utilizador.nome if self.utilizador else None,
            "bloqueada": self.bloqueada  # NOVO
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data["descricao"],
            prioridade=data["prioridade"],
            prazo=data.get("prazo"),
            concluida=data.get("concluida", False),
            utilizador=None,
            bloqueada=data.get("bloqueada", False)  # NOVO
        )
