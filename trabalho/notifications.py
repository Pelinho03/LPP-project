from plyer import notification

def notificar_tarefa(self, tarefa):
    if tarefa.prioridade == "Alta":
        notification.notify(
            title="Tarefa Importante!",
            message=f"{tarefa.titulo}: {tarefa.descricao}",
            timeout=5
        )