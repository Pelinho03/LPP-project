class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, prazo=None, concluida=False, utilizador=None, bloqueada=False):
        # Inicialização dos atributos principais da tarefa
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida
        self.utilizador = utilizador  # Pode ser associado mais tarde
        self.bloqueada = bloqueada    # Indica se a tarefa está bloqueada por dependências

    def to_dict(self):
        # Converte a tarefa num dicionário para guardar em JSON
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "concluida": self.concluida,
            "utilizador": self.utilizador.nome if self.utilizador else None,
            "bloqueada": self.bloqueada
        }

    @classmethod
    def from_dict(cls, data):
        # Cria uma instância da classe Tarefa a partir de um dicionário (ex: ao carregar de JSON)
        return cls(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data["descricao"],
            prioridade=data["prioridade"],
            prazo=data.get("prazo"),
            concluida=data.get("concluida", False),
            utilizador=None,  # A associação ao utilizador será feita depois
            bloqueada=data.get("bloqueada", False)
        )

    def __str__(self):
        # Representação em string da tarefa, útil para debugging ou listagens simples
        return f"Tarefa {self.titulo}, Prioridade {self.prioridade}, Prazo {self.prazo}, Concluída {self.concluida}, Utilizador: {self.utilizador.nome if self.utilizador else 'Nenhum'}"
