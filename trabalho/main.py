# Arquivo principal
import sys
from PyQt6.QtWidgets import QApplication
from ui.adminUI import GestorTarefas
from ui.loginUI import LoginUI
from ui.userUI import UserUI

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     gestor = GestorTarefas()
#     gestor.show()
#     sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginUI()
    login.show()
    sys.exit(app.exec())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     userUI = UserUI()
#     userUI.show()
#     sys.exit(app.exec())
