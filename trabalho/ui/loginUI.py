from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout
from ui.adminUI import GestorTarefas
from ui.userUI import UserUI
from user.user_json import carregar_utilizadores


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FocusFlow")
        self.setStyleSheet(open("styles/style.qss", "r").read())
        self.setGeometry(400, 200, 400, 200)
        layout = QVBoxLayout()

        self.campo_email = QLineEdit()
        self.campo_email.setPlaceholderText("Email")
        layout.addWidget(self.campo_email)

        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.verificar_login)
        layout.addWidget(self.btn_login)

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
