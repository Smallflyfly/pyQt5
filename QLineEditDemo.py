#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/29
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QFont, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QApplication


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit('Hello python')
        self.form_layout = QFormLayout()
        self.initUI()

    def initUI(self):
        self.edit1.setValidator(QIntValidator())
        # 不超过9999
        self.edit1.setMaxLength(4)
        self.edit1.setAlignment(Qt.AlignRight)
        self.edit1.setFont(QFont('Arial', 20))

        self.edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        self.edit3.setInputMask('99_999_999999;#')

        self.edit4.textChanged.connect(self.text_change)

        self.edit5.setEchoMode(QLineEdit.Password)

        self.edit6.editingFinished.connect(self.enter_press)
        self.edit6.setReadOnly(True)

        self.form_layout.addRow('整数校验', self.edit1)
        self.form_layout.addRow('浮点校验', self.edit2)
        self.form_layout.addRow('Input Mask', self.edit3)
        self.form_layout.addRow('文本变化', self.edit4)
        self.form_layout.addRow('密码', self.edit5)
        self.form_layout.addRow('只读', self.edit6)

        self.setLayout(self.form_layout)
        self.setWindowTitle('QLineEdit综合案例')

    def text_change(self, text):
        print('text: ', text)

    def enter_press(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditDemo()
    window.show()

    sys.exit(app.exec_())




