from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QVBoxLayout ,
                             QHBoxLayout , QLabel ,  QWidget, QRadioButton)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Тестування')
main_win.resize(400,400)


qtext = QLabel('День Незалежності України')
v_line = QVBoxLayout()
v1 = QRadioButton('1991')
v2 = QRadioButton('1989')
v3 = QRadioButton('988')
v4 = QRadioButton('1919')

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(qtext, alignment=Qt.AlignCenter)
layout2.addWidget(v1, alignment=Qt.AlignCenter)
layout2.addWidget(v2, alignment=Qt.AlignCenter)
layout3.addWidget(v3, alignment=Qt.AlignCenter)
layout3.addWidget(v4, alignment=Qt.AlignCenter)

v_line.addLayout(layout1)
v_line.addLayout(layout2)
v_line.addLayout(layout3)

main_win.setLayout(v_line)

main_win.show()
app.exec_()