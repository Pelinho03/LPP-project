class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, prazo=None, concluida=False, utilizador=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida
        self.utilizador = utilizador

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

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["titulo"],
            data["descricao"],
            data["prioridade"],
            data.get("prazo"),
            data.get("concluida", False),
            None  # O utilizador será atribuído depois
        )

    def __str__(self):
        return f"Tarefa {self.titulo}, Prioridade {self.prioridade}, Prazo {self.prazo}, Concluída {self.concluida}, Utilizador: {self.utilizador.nome if self.utilizador else 'Nenhum'}"
