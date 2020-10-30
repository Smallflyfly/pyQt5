#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/30
"""
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.v_layout = QVBoxLayout()
        self.button1 = QPushButton('第一个按钮')
        self.button2 = QPushButton('图像按钮')
        self.button3 = QPushButton('不可用按钮')
        self.button4 = QPushButton('&MyButton')

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton")

        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.which_button(self.button1))
        self.button1.clicked.connect(lambda: self.button_status(self.button1))

        self.button2.setIcon(QIcon(QPixmap('./images/python.jpg')))
        self.button2.clicked.connect(lambda: self.which_button(self.button2))

        self.button3.setEnabled(False)

        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.which_button(self.button4))

        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.button3)
        self.v_layout.addWidget(self.button4)

        self.setLayout(self.v_layout)

    def which_button(self, btn):
        print('被单击的按钮是<' + btn.text() + '>')

    def button_status(self, btn: QPushButton):
        if btn.isChecked():
            print(btn.text() + '被选中')
        else:
            print(btn.text() + '未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPushButtonDemo()
    window.show()

    sys.exit(app.exec_())
