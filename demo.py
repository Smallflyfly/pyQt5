#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/26
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# from design01 import Ui_MainWindow
from hvlayout import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    exit(app.exec_())
