# Arquivo principal
import sys
from PyQt6.QtWidgets import QApplication
from ui import GestorTarefas
from login import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gestor = GestorTarefas()
    gestor.show()
    sys.exit(app.exec())


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
