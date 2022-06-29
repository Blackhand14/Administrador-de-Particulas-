from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow 
import sys

# Aplicación de Qt
app = QApplication()
window = MainWindow() 
# Se hace visible el botón
window.show()
# Qt loop
sys.exit(app.exec_()) 
