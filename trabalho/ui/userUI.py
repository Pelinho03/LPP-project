from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from tarefa.tarefa_json import carregar_tarefas
from user.user_json import carregar_utilizadores
import os


class UserUI(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.tarefas_user = []  # Armazena as tarefas associadas ao utilizador
        self.setWindowTitle(f"FocusFlow | Tarefas do/a {self.user.nome}")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(current_dir, "../styles/style.qss")

        try:
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Arquivo de estilo não encontrado: {qss_path}")
        self.setGeometry(300, 50, 1000, 700)

        # Layout geral (vertical)
        layout_geral = QVBoxLayout()

        """====================================="""
        # Navbar (linha superior com botões)
        """====================================="""
        layout_navbar = QHBoxLayout()

        # Botão "Voltar"
        self.btn_retroceder = QPushButton("Voltar")
        self.btn_retroceder.setFixedWidth(100)
        self.btn_retroceder.clicked.connect(self.voltar_login)
        layout_navbar.addWidget(self.btn_retroceder)

        # logo
        self.logo = QLabel()
        logo_dir = os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(
            logo_dir, "../assets/logo_focusflow_lettering.png")
        pixmap = QPixmap(assets_path)
        self.logo.setPixmap(pixmap.scaled(
            100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout_navbar.addWidget(
            self.logo, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Centralizar os botões no navbar
        layout_navbar.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Adicionar o navbar ao layout geral
        layout_geral.addLayout(layout_navbar)

        """====================================="""
        # Coluna 1: Lista de tarefas e pesquisa
        """====================================="""

        # Layout principal (duas colunas)
        layout_principal = QHBoxLayout()

        coluna_lista_tarefas = QVBoxLayout()

        # Campo de pesquisa
        self.campo_pesquisa = QLineEdit()
        self.campo_pesquisa.setPlaceholderText("Pesquisar Tarefa")
        self.campo_pesquisa.textChanged.connect(self.pesquisar_tarefa)
        coluna_lista_tarefas.addWidget(self.campo_pesquisa)

        # Lista de tarefas
        self.lista_tarefas = QListWidget()
        self.lista_tarefas.itemClicked.connect(
            self.exibir_detalhes_tarefa)  # Conectar clique ao método
        coluna_lista_tarefas.addWidget(self.lista_tarefas)

        # Botões de ações
        botoes_layout = QHBoxLayout()
        self.btn_concluir = QPushButton("Marcar como Concluída")
        self.btn_concluir.clicked.connect(self.marcar_concluida)
        botoes_layout.addWidget(self.btn_concluir)

        self.btn_desmarcar = QPushButton("Desmarcar Tarefa")
        self.btn_desmarcar.clicked.connect(self.desmarcar_tarefa)
        botoes_layout.addWidget(self.btn_desmarcar)

        coluna_lista_tarefas.addLayout(botoes_layout)

        # Botões de ordenação
        botoes_ordenacao = QHBoxLayout()
        self.btn_ordenar_prioridade = QPushButton("Ordenar por Prioridade")
        self.btn_ordenar_prioridade.clicked.connect(
            self.ordenar_por_prioridade)
        botoes_ordenacao.addWidget(self.btn_ordenar_prioridade)

        self.btn_ordenar_data = QPushButton("Ordenar por Data")
        self.btn_ordenar_data.clicked.connect(self.ordenar_por_data)
        botoes_ordenacao.addWidget(self.btn_ordenar_data)

        coluna_lista_tarefas.addLayout(botoes_ordenacao)

        # Adicionar a coluna de lista ao layout principal
        layout_principal.addLayout(coluna_lista_tarefas)

        """====================================="""
        # Coluna 2: Visor de detalhes da tarefa
        """====================================="""
        coluna_detalhes_tarefa = QVBoxLayout()

        # Visor de detalhes da tarefa
        self.visor_detalhes = QTextEdit()
        self.visor_detalhes.setReadOnly(True)  # Apenas leitura
        coluna_detalhes_tarefa.addWidget(self.visor_detalhes)

        # Adicionar a coluna de detalhes ao layout principal
        layout_principal.addLayout(coluna_detalhes_tarefa)

        layout_geral.addLayout(layout_principal)

        self.setLayout(layout_geral)

        # Configurar o layout principal
        self.setLayout(layout_principal)

        # Carregar tarefas associadas ao utilizador
        self.carregar_tarefas()

    def carregar_tarefas(self):
        """Carrega as tarefas associadas ao utilizador."""
        utilizadores = carregar_utilizadores()  # Carregar todos os utilizadores
        # Carregar todas as tarefas com utilizadores associados
        tarefas = carregar_tarefas(utilizadores)
        self.tarefas_user = [
            t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
        self.lista_tarefas.clear()
        for tarefa in self.tarefas_user:
            status = "[🟢]" if tarefa.concluida else "[🔴]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def exibir_detalhes_tarefa(self, item):
        """Exibe os detalhes da tarefa selecionada no visor."""
        index = self.lista_tarefas.row(item)
        if index < 0 or index >= len(self.tarefas_user):
            self.visor_detalhes.setText("Erro: Tarefa inválida selecionada.")
            return

        tarefa = self.tarefas_user[index]
        detalhes = (
            f"Título: {tarefa.titulo}\n"
            f"-----------------------------------------------------------\n"
            f"Descrição: {tarefa.descricao}\n"
            f"-----------------------------------------------------------\n"
            f"Prioridade: {tarefa.prioridade}\n"
            f"Prazo: {tarefa.prazo if tarefa.prazo else 'Sem prazo'}\n"
            f"Concluída: {'Sim' if tarefa.concluida else 'Não'}\n"
            f"Utilizador: {tarefa.utilizador.nome if tarefa.utilizador else 'Nenhum'}\n"
        )
        self.visor_detalhes.setText(detalhes)

    def pesquisar_tarefa(self):
        """Filtra as tarefas com base no texto de pesquisa."""
        texto_pesquisa = self.campo_pesquisa.text().lower()
        tarefas = carregar_tarefas()
        tarefas_user = [
            t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
        tarefas_filtradas = [
            t for t in tarefas_user if texto_pesquisa in t.titulo.lower()]
        self.lista_tarefas.clear()
        for tarefa in tarefas_filtradas:
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def desmarcar_tarefa(self):
        """desmarca a tarefa selecionada."""
        index = self.lista_tarefas.currentRow()
        if index >= 0:
            tarefas = carregar_tarefas()
            tarefas_user = [
                t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
            tarefa = tarefas_user[index]
            tarefa.concluida = False
            self.carregar_tarefas()

    def marcar_concluida(self):
        """Marca a tarefa selecionada como concluída."""
        index = self.lista_tarefas.currentRow()
        if index >= 0:
            tarefas = carregar_tarefas()
            tarefas_user = [
                t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
            tarefa = tarefas_user[index]
            tarefa.concluida = True
            self.carregar_tarefas()

    def ordenar_por_prioridade(self):
        """Ordena as tarefas por prioridade."""
        prioridades = {"Alta": 0, "Média": 1, "Baixa": 2}
        tarefas = carregar_tarefas()
        tarefas_user = [
            t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
        tarefas_user.sort(key=lambda t: prioridades.get(t.prioridade, 3))
        self.lista_tarefas.clear()
        for tarefa in tarefas_user:
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def ordenar_por_data(self):
        """Ordena as tarefas por data."""
        tarefas = carregar_tarefas()
        tarefas_user = [
            t for t in tarefas if t.utilizador and t.utilizador.email == self.user.email]
        tarefas_user.sort(key=lambda t: t.prazo or "")
        self.lista_tarefas.clear()
        for tarefa in tarefas_user:
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(
                f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def voltar_login(self):
        from ui.loginUI import LoginUI
        self.close()
        self.login = LoginUI()
        self.login.show()
