#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/28
"""
import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.name_label = QLabel('&Name', self)
        self.name_line_edit = QLineEdit(self)

        self.password_label = QLabel('&password', self)
        self.password_line_edit = QLineEdit(self)

        self.btn_OK = QPushButton('&OK', self)
        self.btn_cancel = QPushButton('&Cancel', self)

        self.initUI()

    def initUI(self):
        self.name_label.setBuddy(self.name_line_edit)
        self.password_label.setBuddy(self.password_line_edit)
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.name_label, 0, 0)
        main_layout.addWidget(self.name_line_edit, 0, 1, 1, 2)

        main_layout.addWidget(self.password_label, 1, 0)
        main_layout.addWidget(self.password_line_edit, 1, 1, 1, 2)

        main_layout.addWidget(self.btn_OK, 2, 1)
        main_layout.addWidget(self.btn_cancel, 2, 2)

        self.setWindowTitle("QLabel Buddy")
        # self.resize(400, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelBuddy()
    window.show()

    sys.exit(app.exec_())
