#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/03
"""
import sys

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit, QFileDialog, QApplication


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.btn1 = QPushButton('加载图片')
        self.btn2 = QPushButton('加载文本文件')
        self.v_layout = QVBoxLayout()
        self.image_label = QLabel()
        self.contents = QTextEdit()
        self.initUI()

    def initUI(self):
        self.btn1.clicked.connect(self.load_image)
        self.btn2.clicked.connect(self.load_text)

        self.v_layout.addWidget(self.btn1)
        self.v_layout.addWidget(self.image_label)
        self.v_layout.addWidget(self.btn2)
        self.v_layout.addWidget(self.contents)

        self.setLayout(self.v_layout)
        self.setWindowTitle('文件对话框演示')

    def load_image(self):
        frame, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png)')
        self.image_label.setPixmap(QPixmap(frame))

    def load_text(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            with open(filenames[0], encoding='utf-8', mode='r') as f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFileDialogDemo()
    window.show()

    sys.exit(app.exec_())
