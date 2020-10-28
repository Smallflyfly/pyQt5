#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/28
"""
import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QApplication, QLineEdit


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.normal_line_edit = QLineEdit()
        self.no_echo_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.password_echo_on_line_edit = QLineEdit()
        self.form_layout = QFormLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入文本框模式")
        self.form_layout.addRow("Normal", self.normal_line_edit)
        self.form_layout.addRow("NoEcho", self.no_echo_line_edit)
        self.form_layout.addRow("Password", self.password_line_edit)
        self.form_layout.addRow("PasswordNoEcho", self.password_echo_on_line_edit)

        self.normal_line_edit.setPlaceholderText("Normal")
        self.no_echo_line_edit.setPlaceholderText("NoEcho")
        self.password_line_edit.setPlaceholderText("Password")
        self.password_echo_on_line_edit.setPlaceholderText("PasswordNoEcho")

        self.normal_line_edit.setEchoMode(QLineEdit.Normal)
        self.no_echo_line_edit.setEchoMode(QLineEdit.NoEcho)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_echo_on_line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(self.form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditDemo()
    window.show()

    sys.exit(app.exec_())
