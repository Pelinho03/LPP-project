import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget,
    QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QMessageBox, QInputDialog
)
from PyQt6.QtCore import Qt, QDate
from storage import carregar_tarefas, guardar_tarefas
from storage_users import carregar_utilizadores, guardar_utilizadores
from models import Tarefa
from users import User
from notifications import notificar_tarefa


# Interface gráfica
class GestorTarefas(QWidget):

    def __init__(self):
        super().__init__()
        self.utilizadores = carregar_utilizadores()
        self.tarefas = carregar_tarefas(self.utilizadores)
        self.setWindowTitle("Gestor de Tarefas")
        self.setGeometry(400, 200, 700, 400)
        self.layout = QVBoxLayout()

        # Campo de Pesquisa
        self.campo_pesquisa = QLineEdit()
        self.campo_pesquisa.setPlaceholderText("Pesquisar Tarefa")
        self.campo_pesquisa.textChanged.connect(self.pesquisar_tarefa)
        self.layout.addWidget(self.campo_pesquisa)

        # Lista de Tarefas
        self.lista_tarefas = QListWidget()
        self.layout.addWidget(self.lista_tarefas)

        # Formulário
        self.campo_titulo = QLineEdit()
        self.campo_titulo.setPlaceholderText("Título da Tarefa")
        self.layout.addWidget(self.campo_titulo)

        self.campo_descricao = QTextEdit()
        self.campo_descricao.setPlaceholderText("Descrição")
        self.layout.addWidget(self.campo_descricao)

        # self.campo_prioridade = QComboBox()
        # self.campo_prioridade.addItems(["Alta", "Média", "Baixa"])
        # self.layout.addWidget(self.campo_prioridade)

        # Botões de prioridade e utilizador
        botoes_prioridade_ordenação = QHBoxLayout()
        self.campo_prioridade = QComboBox()
        self.campo_prioridade.addItems(["Alta", "Média", "Baixa"])
        botoes_prioridade_ordenação.addWidget(self.campo_prioridade)

        self.campo_utilizador = QComboBox()
        botoes_prioridade_ordenação.addWidget(self.campo_utilizador)

        self.btn_criar_utilizador = QPushButton("Criar Utilizador")
        self.btn_criar_utilizador.clicked.connect(self.criar_utilizador)
        botoes_prioridade_ordenação.addWidget(self.btn_criar_utilizador)

        self.atualizar_utilizadores()

        self.layout.addLayout(botoes_prioridade_ordenação)

        # Campo de prazo
        self.campo_prazo = QDateEdit()
        self.campo_prazo.setDisplayFormat("dd/MM/yyyy")
        self.campo_prazo.setDate(QDate.currentDate())
        self.layout.addWidget(self.campo_prazo)

        # Botão Adicionar
        self.btn_adicionar = QPushButton("Adicionar Tarefa")
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        self.layout.addWidget(self.btn_adicionar)

        # Botões de ações
        botoes_layout = QHBoxLayout()
        self.btn_remover = QPushButton("Remover Tarefa")
        self.btn_remover.clicked.connect(self.remover_tarefa)
        botoes_layout.addWidget(self.btn_remover)

        self.btn_concluir = QPushButton("Marcar como Concluída")
        self.btn_concluir.clicked.connect(self.marcar_concluida)
        botoes_layout.addWidget(self.btn_concluir)

        self.btn_editar = QPushButton("Editar Tarefa")
        self.btn_editar.clicked.connect(self.editar_tarefa)
        botoes_layout.addWidget(self.btn_editar)

        self.layout.addLayout(botoes_layout)

        # Botões de ordenação
        botoes_ordenacao = QHBoxLayout()
        self.btn_ordenar_prioridade = QPushButton("Ordenar por Prioridade")
        self.btn_ordenar_prioridade.clicked.connect(
            self.ordenar_por_prioridade)
        botoes_ordenacao.addWidget(self.btn_ordenar_prioridade)

        self.btn_ordenar_data = QPushButton("Ordenar por Data")
        self.btn_ordenar_data.clicked.connect(self.ordenar_por_data)
        botoes_ordenacao.addWidget(self.btn_ordenar_data)

        self.layout.addLayout(botoes_ordenacao)

        self.setLayout(self.layout)
        self.tarefas = carregar_tarefas()
        self.atualizar_lista()

    def atualizar_lista(self, filtro=None):
        self.lista_tarefas.clear()
        tarefas_filtradas = self.tarefas
        if filtro:
            tarefas_filtradas = [
                t for t in self.tarefas if filtro.lower() in t.titulo.lower()]
        for tarefa in tarefas_filtradas:
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def pesquisar_tarefa(self):
        texto_pesquisa = self.campo_pesquisa.text()
        self.atualizar_lista(texto_pesquisa)

    def adicionar_tarefa(self):
        titulo = self.campo_titulo.text()
        descricao = self.campo_descricao.toPlainText()
        prioridade = self.campo_prioridade.currentText()
        prazo = self.campo_prazo.date().toString(
            "yyyy-MM-dd") if self.campo_prazo.date().isValid() else None

        utilizador_nome = self.campo_utilizador.currentText()
        utilizador = next(
            (u for u in self.utilizadores if u.nome == utilizador_nome), None)

        if prazo and QDate.currentDate() > self.campo_prazo.date():
            QMessageBox.warning(
                self, "Erro", "A data de prazo não pode ser anterior à data atual.")
            return

        if not titulo:
            QMessageBox.warning(
                self, "Erro", "O título da tarefa não pode estar vazio.")
            return

        nova_tarefa = Tarefa(
            len(self.tarefas) + 1,
            titulo,
            descricao,
            prioridade,
            prazo,
            False,
            utilizador
        )

        self.tarefas.append(nova_tarefa)
        guardar_tarefas(self.tarefas)
        self.atualizar_lista()
        self.notificar_tarefa(nova_tarefa)

        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.campo_prazo.clear()

    def notificar_tarefa(self, tarefa):
        print(f"Notificando tarefa: {tarefa.titulo}")

    def remover_tarefa(self):
        index = self.lista_tarefas.currentRow()
        if index >= 0:
            self.tarefas.pop(index)
            guardar_tarefas(self.tarefas)
            self.atualizar_lista()

    def marcar_concluida(self):
        index = self.lista_tarefas.currentRow()
        if index >= 0:
            self.tarefas[index].concluida = True
            guardar_tarefas(self.tarefas)
            self.atualizar_lista()

    def editar_tarefa(self):
        index = self.lista_tarefas.currentRow()
        if index >= 0:
            tarefa = self.tarefas[index]
            self.campo_titulo.setText(tarefa.titulo)
            self.campo_descricao.setText(tarefa.descricao)
            self.campo_prioridade.setCurrentText(tarefa.prioridade)

            if tarefa.prazo:
                data = datetime.datetime.strptime(tarefa.prazo, "%Y-%m-%d")
                self.campo_prazo.setDate(
                    QDate(data.year, data.month, data.day))
            else:
                self.campo_prazo.setDate(QDate.currentDate())

            # Remover botão antigo, se existir
            if hasattr(self, 'btn_salvar_edicao'):
                self.btn_salvar_edicao.setParent(None)
                self.btn_salvar_edicao.deleteLater()

            # Criar botão de salvar edição
            self.btn_salvar_edicao = QPushButton("Salvar Edição")
            self.layout.addWidget(self.btn_salvar_edicao)

            def salvar_edicao():
                tarefa.titulo = self.campo_titulo.text()
                tarefa.descricao = self.campo_descricao.toPlainText()
                tarefa.prioridade = self.campo_prioridade.currentText()
                tarefa.prazo = self.campo_prazo.date().toString(
                    "yyyy-MM-dd") if self.campo_prazo.date().isValid() else ""
                guardar_tarefas(self.tarefas)
                self.atualizar_lista()
                QMessageBox.information(
                    self, "Sucesso", "Tarefa editada com sucesso!")
                self.btn_salvar_edicao.hide()  # Esconde o botão depois de salvar

            self.btn_salvar_edicao.clicked.connect(salvar_edicao)

    def ordenar_por_prioridade(self):
        prioridades = {"Alta": 0, "Média": 1, "Baixa": 2}
        self.tarefas.sort(key=lambda t: prioridades.get(t.prioridade, 3))
        self.atualizar_lista()

    def ordenar_por_data(self):
        def converter_data(tarefa):
            try:
                return datetime.datetime.strptime(tarefa.prazo, "%Y-%m-%d") if tarefa.prazo else datetime.datetime.max
            except Exception:
                return datetime.datetime.max
        self.tarefas.sort(key=converter_data)
        self.atualizar_lista()

    def atualizar_utilizadores(self):
        self.campo_utilizador.clear()
        for user in self.utilizadores:
            self.campo_utilizador.addItem(user.nome)

    def criar_utilizador(self):
        nome, ok_nome = QInputDialog.getText(
            self, "Criar Utilizador", "Nome do Utilizador:")
        if not ok_nome or not nome.strip():
            QMessageBox.warning(
                self, "Erro", "O nome do Utilizador não pode estar vazio.")
            return

        email, ok_email = QInputDialog.getText(
            self, "Criar Utilizador", "Email do Utilizador:")
        if not ok_email or not email.strip():
            QMessageBox.warning(
                self, "Erro", "O email do Utilizador não pode estar vazio.")
            return

        novo_user = User(nome.strip(), email.strip())
        self.utilizadores.append(novo_user)
        guardar_utilizadores(self.utilizadores)
        self.atualizar_utilizadores()
