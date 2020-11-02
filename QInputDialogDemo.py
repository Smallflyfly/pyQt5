#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLineEdit


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.form_layout = QFormLayout()
        self.button1 = QPushButton('获取列表中的选项')
        self.line_edit1 = QLineEdit()
        self.button2 = QPushButton('获取字符串')
        self.line_edit2 = QLineEdit()
        self.button3 = QPushButton('获取整数')
        self.line_edit3 = QLineEdit()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框例子')

        self.button1.clicked.connect(self.get_item)
        self.form_layout.addRow(self.button1, self.line_edit1)

        self.button2.clicked.connect(self.get_text)
        self.form_layout.addRow(self.button2, self.line_edit2)

        self.button3.clicked.connect(self.get_int)
        self.form_layout.addRow(self.button3, self.line_edit3)



    def get_item(self):

    def get_text(self):

    def get_int(self):

