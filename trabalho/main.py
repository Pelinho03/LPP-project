# Arquivo principal
import sys
from PyQt6.QtWidgets import QApplication
from ui import GestorTarefas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gestor = GestorTarefas()
    gestor.show()
    sys.exit(app.exec())
