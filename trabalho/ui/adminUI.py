import datetime
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QListWidget,
                             QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QMessageBox, QInputDialog
                             )
from PyQt6.QtCore import QDate
from tarefa.tarefa_json import carregar_tarefas, guardar_tarefas
from tarefa.tarefa import Tarefa
from user.user_json import carregar_utilizadores, guardar_utilizadores
from user.user import User
from notificações.notifications import notificar_tarefa


# Interface gráfica
class GestorTarefas(QWidget):

    def __init__(self):
        super().__init__()

        self.utilizadores = carregar_utilizadores()
        self.tarefas = carregar_tarefas(self.utilizadores)
        self.setWindowTitle("FocusFlow")
        self.setStyleSheet(open("styles/style.qss", "r").read())
        self.setGeometry(400, 200, 800, 500)

        # Layout principal (duas colunas)
        layout_principal = QHBoxLayout()

        """====================================="""
        # Coluna 1: Formulário para criar tarefas
        """====================================="""
        coluna_criar_tarefa = QVBoxLayout()

        # Campo de título
        self.campo_titulo = QLineEdit()
        self.campo_titulo.setPlaceholderText("Título da Tarefa")
        coluna_criar_tarefa.addWidget(self.campo_titulo)

        # Campo de descrição
        self.campo_descricao = QTextEdit()
        self.campo_descricao.setPlaceholderText("Descrição")
        coluna_criar_tarefa.addWidget(self.campo_descricao)

        # Campo de prioridade
        self.campo_prioridade = QComboBox()
        self.campo_prioridade.addItems(["Alta", "Média", "Baixa"])
        coluna_criar_tarefa.addWidget(self.campo_prioridade)

        # Campo de utilizador
        self.campo_utilizador = QComboBox()
        coluna_criar_tarefa.addWidget(self.campo_utilizador)

        # Botão para criar utilizador
        self.btn_criar_utilizador = QPushButton("Criar Utilizador")
        self.btn_criar_utilizador.clicked.connect(self.criar_utilizador)
        coluna_criar_tarefa.addWidget(self.btn_criar_utilizador)

        # Campo de prazo
        self.campo_prazo = QDateEdit()
        self.campo_prazo.setDisplayFormat("dd/MM/yyyy")
        self.campo_prazo.setDate(QDate.currentDate())
        coluna_criar_tarefa.addWidget(self.campo_prazo)

        # Botão para adicionar tarefa
        self.btn_adicionar = QPushButton("Adicionar Tarefa")
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        coluna_criar_tarefa.addWidget(self.btn_adicionar)

        """====================================="""
        # Adicionar a coluna de criação ao layout principal
        """====================================="""
        layout_principal.addLayout(coluna_criar_tarefa)
        """====================================="""

        """====================================="""
        # Coluna 2: Lista de tarefas e pesquisa
        """====================================="""
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

        # Visor de detalhes da tarefa
        self.visor_detalhes = QTextEdit()
        self.visor_detalhes.setReadOnly(True)  # Apenas leitura
        coluna_lista_tarefas.addWidget(self.visor_detalhes)

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

        """====================================="""
        # Adicionar a coluna de lista ao layout principal
        """====================================="""
        layout_principal.addLayout(coluna_lista_tarefas)
        """====================================="""

        # layout principal
        self.setLayout(layout_principal)

        # Inicializar a lista de utilizadores e tarefas
        self.atualizar_utilizadores()
        self.atualizar_lista()

    def exibir_detalhes_tarefa(self, item):
        index = self.lista_tarefas.row(item)
        tarefa = self.tarefas[index]
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

    def atualizar_lista(self, filtro=None):
        self.lista_tarefas.clear()
        tarefas_filtradas = self.tarefas
        if filtro:
            tarefas_filtradas = [
                t for t in self.tarefas if filtro.lower() in t.titulo.lower()]
        for tarefa in tarefas_filtradas:
            status = "[🟢]" if tarefa.concluida else "[🔴]"
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

        grupo, ok_grupo = QInputDialog.getItem(
            self, "Grupo do Utilizador", "Selecione o grupo:",
            ["admin", "desenvolvedores", "design"], 0, False
        )
        if not ok_grupo:
            return

        novo_user = User(nome.strip(), email.strip(), grupo)
        self.utilizadores.append(novo_user)
        guardar_utilizadores(self.utilizadores)
        self.atualizar_utilizadores()
