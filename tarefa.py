class Tarefa:
    # Método construtor: inicializa uma nova tarefa com os atributos fornecidos
    def __init__(self, id, titulo, descricao, prioridade, prazo=None, concluida=False, utilizador=None, bloqueada=False):
        self.id = id                              # Identificador único da tarefa
        self.titulo = titulo                      # Título da tarefa
        self.descricao = descricao                # Descrição detalhada da tarefa
        self.prioridade = prioridade              # Prioridade da tarefa (por exemplo: alta, média, baixa)
        self.prazo = prazo                        # Prazo de entrega/conclusão (pode ser None)
        self.concluida = concluida                # Indica se a tarefa está concluída 
        self.utilizador = utilizador              # Objeto User associado 
        self.bloqueada = bloqueada                # Indica se a tarefa está bloqueada 

    # Converte o objeto Tarefa para um dicionário, útil para serialização (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "concluida": self.concluida,
            "utilizador": self.utilizador.nome if self.utilizador else None,  # Só guarda o nome do utilizador
            "bloqueada": self.bloqueada
        }

    # Método de classe que cria um objeto Tarefa a partir de um dicionário
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data["descricao"],
            prioridade=data["prioridade"],
            prazo=data.get("prazo"),                        # Usa None se o campo não existir
            concluida=data.get("concluida", False),         # Por padrão, não concluída
            utilizador=None,                                # O utilizador precisa ser associado posteriormente
            bloqueada=data.get("bloqueada", False)          # Por padrão, não bloqueada
        )

    # Representação textual do objeto Tarefa, útil para debug ou listagens
    def __str__(self):
        return f"Tarefa {self.titulo}, Prioridade {self.prioridade}, Prazo {self.prazo}, Concluída {self.concluida}, Utilizador: {self.utilizador.nome if self.utilizador else 'Nenhum'}"
