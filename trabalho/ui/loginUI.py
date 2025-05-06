from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from ui.adminUI import GestorTarefas
from ui.userUI import UserUI
from user.user_json import carregar_utilizadores
import os


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FocusFlow | Login")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(current_dir, "../styles/style.qss")

        try:
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Arquivo de estilo não encontrado: {qss_path}")

        self.setGeometry(300, 50, 1000, 700)

        layout = QVBoxLayout()

        # Espaçador para empurrar tudo mais para o centro
        layout.addSpacerItem(QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Imagem
        self.image = QLabel()
        logo_dir = os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(
            logo_dir, "../assets/logo_focusflow_complete.png")
        pixmap = QPixmap(assets_path)
        self.image.setPixmap(pixmap.scaled(
            250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.image.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.image)

        # Pequeno espaçador entre imagem e campos
        layout.addSpacerItem(QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Campo de email
        self.campo_email = QLineEdit()
        self.campo_email.setPlaceholderText("Email")
        self.campo_email.setFixedWidth(300)
        email_container = QHBoxLayout()
        email_container.addWidget(self.campo_email)
        email_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(email_container)

        # Botão de login
        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.verificar_login)
        self.btn_login.setFixedWidth(300)
        button_container = QHBoxLayout()
        button_container.addWidget(self.btn_login)
        button_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(button_container)

        # Espaçador para preencher o fundo
        layout.addSpacerItem(QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Configurar layout principal
        self.setLayout(layout)

    def verificar_login(self):
        email = self.campo_email.text().strip()
        utilizadores = carregar_utilizadores()

        user = next((u for u in utilizadores if u.email == email), None)
        if not user:
            QMessageBox.warning(self, "Erro", "Utilizador não encontrado!")
            return

        if user.grupo == "admin":
            self.abrir_ui_admin()
        else:
            self.abrir_ui_user(user)

    def abrir_ui_admin(self):
        self.ui_admin = GestorTarefas()
        self.ui_admin.show()
        self.close()

    def abrir_ui_user(self, user):
        self.ui_user = UserUI(user)
        self.ui_user.show()
        self.close()
