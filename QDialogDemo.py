#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QApplication


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.button = QPushButton(self)
        self.dialog = QDialog()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        button = QPushButton('确定', self.dialog)
        button.clicked.connect(self.dialog.close)
        button.move(50, 50)
        self.dialog.setWindowTitle('对话框')
        self.dialog.setWindowModality(Qt.ApplicationModal)

        self.dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialogDemo()
    window.show()

    sys.exit(app.exec_())
