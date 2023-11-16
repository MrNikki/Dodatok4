from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(500,300)
main_win.move(600,300)



main_win.show()
app.exec()