from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from ui.adminUI import GestorTarefas
from ui.userUI import UserUI
from user.user_json import carregar_utilizadores


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FocusFlow | Login")
        self.setStyleSheet(open("styles/login.qss", "r").read())
        self.setGeometry(400, 200, 800, 500)
        layout = QVBoxLayout()
        # Define o espaçamento vertical entre os widgets (10px)
        layout.setSpacing(10)

        # Imagem
        self.image = QLabel()
        pixmap = QPixmap('assets/app_icon.png')
        pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)
        self.image.setPixmap(pixmap)
        self.image.setFixedSize(200, 200)
        self.image.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Envolver a imagem em um QHBoxLayout para centralizá-la
        image_container = QHBoxLayout()
        image_container.addWidget(self.image)
        image_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(image_container)

        # # Título
        # self.titulo = QLabel("Login")
        # self.titulo.setStyleSheet("font-weight: bold; font-size: 35px;")
        # self.titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # # Envolver o título em um QHBoxLayout para centralizá-lo
        # titulo_container = QHBoxLayout()
        # titulo_container.addWidget(self.titulo)
        # titulo_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # layout.addLayout(titulo_container)

        # Campo de email
        self.campo_email = QLineEdit()
        self.campo_email.setPlaceholderText("Email")
        self.campo_email.setFixedWidth(300)

        # Envolver o campo de email em um QHBoxLayout para centralizá-lo
        email_container = QHBoxLayout()
        email_container.addWidget(self.campo_email)
        email_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(email_container)

        # Botão de login
        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.verificar_login)
        self.btn_login.setFixedWidth(150)

        # Envolver o botão em um QHBoxLayout para centralizá-lo
        button_container = QHBoxLayout()
        button_container.addWidget(self.btn_login)
        button_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(button_container)

        # Configurar o layout principal
        self.setLayout(layout)

    def verificar_login(self):
        email = self.campo_email.text().strip()
        utilizadores = carregar_utilizadores()

        # Verificar se o utilizador existe
        user = next((u for u in utilizadores if u.email == email), None)
        if not user:
            QMessageBox.warning(self, "Erro", "Utilizador não encontrado!")
            return

        # Redirecionar com base no grupo
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
