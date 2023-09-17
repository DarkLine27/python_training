from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QVBoxLayout ,
                             QHBoxLayout , QLabel ,  QWidget)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Тестування')
main_win.resize(400,400)

main_win.show()
app.exec_()