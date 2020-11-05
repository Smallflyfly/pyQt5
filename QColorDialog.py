#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/03
"""
import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QColorDialog, QLabel, QApplication, QPushButton, QVBoxLayout


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.label = QLabel('颜色测试')
        self.color_button = QPushButton('设置颜色')
        self.bg_color_button = QPushButton('设置背景颜色')
        self.v_layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog 例子')

        self.color_button.clicked.connect(self.get_color)

        self.bg_color_button.clicked.connect(self.get_bg_color)

        self.v_layout.addWidget(self.color_button)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.bg_color_button)

        self.setLayout(self.v_layout)

    def get_color(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)

    def get_bg_color(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QColorDialogDemo()
    window.show()

    sys.exit(app.exec_())
