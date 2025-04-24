from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from tarefa.tarefa_json import carregar_tarefas


class UserUI(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle(f"Tarefas de {self.user.nome}")
        self.setGeometry(400, 200, 600, 400)
        layout = QVBoxLayout()

        # Lista de tarefas
        self.lista_tarefas = QListWidget()
        layout.addWidget(self.lista_tarefas)

        self.setLayout(layout)
        self.carregar_tarefas()

    def carregar_tarefas(self):
        tarefas = carregar_tarefas()
        tarefas_user = [
            t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
        for tarefa in tarefas_user:
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")
