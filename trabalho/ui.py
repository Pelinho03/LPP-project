import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, 
    QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QDateEdit, QMessageBox
)
from storage import carregar_tarefas, guardar_tarefas
from models import Tarefa
from notifications import notificar_tarefa
from PyQt6.QtCore import Qt, QDate

# Interface gráfica
class GestorTarefas(QWidget):
    
    def __init__(self):
        super().__init__()
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

        self.campo_prioridade = QComboBox()
        self.campo_prioridade.addItems(["Alta", "Média", "Baixa"])
        self.layout.addWidget(self.campo_prioridade)

        # Campo de prazo
        self.campo_prazo = QDateEdit()
        self.campo_prazo.setDisplayFormat("dd/MM/yyyy")
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
        self.setLayout(self.layout)
        self.tarefas = carregar_tarefas()
        self.atualizar_lista()

    def atualizar_lista(self, filtro=None):
        self.lista_tarefas.clear()
        tarefas_filtradas = self.tarefas

        if filtro:
            tarefas_filtradas = [tarefa for tarefa in self.tarefas if filtro.lower() in tarefa.titulo.lower()]

        for tarefa in sorted(tarefas_filtradas, key=lambda t: t.prioridade, reverse=True):
            status = "[✔]" if tarefa.concluida else "[ ]"
            prazo = tarefa.prazo if tarefa.prazo else "Sem prazo"
            self.lista_tarefas.addItem(f"{status} {tarefa.titulo} - {tarefa.prioridade} - {prazo}")

    def pesquisar_tarefa(self):
        texto_pesquisa = self.campo_pesquisa.text()
        self.atualizar_lista(texto_pesquisa)

    def adicionar_tarefa(self):
        titulo = self.campo_titulo.text()
        descricao = self.campo_descricao.toPlainText()
        prioridade = self.campo_prioridade.currentText()
        prazo = self.campo_prazo.date().toString("yyyy-MM-dd") if self.campo_prazo.date().isValid() else None

        if not titulo:
            QMessageBox.warning(self, "Erro", "O título da tarefa não pode estar vazio.")
            return

        nova_tarefa = Tarefa(len(self.tarefas) + 1, titulo, descricao, prioridade, prazo)
        self.tarefas.append(nova_tarefa)
        guardar_tarefas(self.tarefas)
        self.atualizar_lista()
        self.notificar_tarefa(nova_tarefa)
        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.campo_prazo.clear()

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
            self.campo_prazo.setDate(datetime.datetime.strptime(tarefa.prazo, "%Y-%m-%d") if tarefa.prazo else QDateEdit().date())

            # Verificar se o botão de salvar já existe, e removê-lo antes de adicionar um novo
            if hasattr(self, 'btn_salvar_edicao'):
                self.btn_salvar_edicao.deleteLater()  # Remove o botão antigo

            def salvar_edicao():
                tarefa.titulo = self.campo_titulo.text()
                tarefa.descricao = self.campo_descricao.toPlainText()
                tarefa.prioridade = self.campo_prioridade.currentText()
                tarefa.prazo = self.campo_prazo.date().toString("yyyy-MM-dd") if self.campo_prazo.date().isValid() else ""
                guardar_tarefas(self.tarefas)
                self.atualizar_lista()
                QMessageBox.information(self, "Sucesso", "Tarefa editada com sucesso!")

            self.btn_salvar_edicao = QPushButton("Salvar Edição")
            self.layout.addWidget(self.btn_salvar_edicao)
            self.btn_salvar_edicao.clicked.connect(salvar_edicao)


#interligar tarefas 
#antecipar o termino das tarefas
#ordenar por prioridade/data
#fazer verificação de datas
