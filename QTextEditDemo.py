#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/29
"""
import sys

from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QApplication


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.text_edit = QTextEdit()
        self.btn_text = QPushButton('显示文本')
        self.btn_html = QPushButton('显示HTML')
        self.v_layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addWidget(self.btn_text)
        self.v_layout.addWidget(self.btn_html)

        self.btn_text.clicked.connect(self.on_click_button_text)

        self.btn_html.clicked.connect(self.on_click_button_html)

        self.setLayout(self.v_layout)

    def on_click_button_text(self):
        self.text_edit.setPlainText('Hello world!')

    def on_click_button_html(self):
        self.text_edit.setHtml('<font color="blue" size="5">Hello world!</font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTextEditDemo()
    window.show()

    sys.exit(app.exec_())