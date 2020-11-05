#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/03
"""
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QFontDialog, QApplication


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.font_button = QPushButton('选择字体')
        self.v_layout = QVBoxLayout()
        self.label = QLabel('测试字体')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog 例子')

        self.font_button.clicked.connect(self.get_font)

        self.v_layout.addWidget(self.font_button)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)

    def get_font(self):
        font, ok = QFontDialog.getFont()
        if font and ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFontDialogDemo()
    window.show()

    sys.exit(app.exec_())