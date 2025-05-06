# Arquivo principal
import sys
from PyQt6.QtWidgets import QApplication
from ui.adminUI import GestorTarefas
from ui.loginUI import LoginUI
from ui.userUI import UserUI
from user.user import User  # para efeitos de teste

# TESTAR ADMIN UI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gestor = GestorTarefas()
    gestor.show()
    sys.exit(app.exec())

# LOGIN UI (MAIN UI)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginUI()
    login.show()
    sys.exit(app.exec())

# TESTAR USER UI
if __name__ == "__main__":
    # user ficticio para efeitos de teste e criar a UI sem necessidade de login
    user_mock = User(nome="Daniel",
                     email="daniel@email.pt", grupo="designer")
    # ----------------------------------------------------------------------------#
    app = QApplication(sys.argv)
    userUI = UserUI(user_mock)
    userUI.show()
    sys.exit(app.exec())
