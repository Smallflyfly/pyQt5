#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLineEdit, QInputDialog, QApplication


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

        self.setLayout(self.form_layout)

    def get_item(self):
        items = ('C', 'C++', 'R', 'Python', 'Java')
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if ok and item:
            self.line_edit1.setText(item)

    def get_text(self):
        text, ok = QInputDialog.getText(self, '请输入文本', '输入姓名')
        if text and ok:
            self.line_edit2.setText(text)

    def get_int(self):
        num, ok = QInputDialog.getInt(self, '整数输入框', '输入数字')
        if num and ok:
            self.line_edit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QInputDialogDemo()
    window.show()

    sys.exit(app.exec_())
