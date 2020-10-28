#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/28
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QApplication, QWidget


class LabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.palette = QPalette()
        self.initUI()

    def initUI(self):
        self.label1.setText("这是一个文本标签")
        self.label1.setAutoFillBackground(True)
        # 设置背景色
        self.palette.setColor(QPalette.Window, Qt.blue)
        self.label1.setPalette(self.palette)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setToolTip('这是一个图片标签')
        self.label3.setPixmap(QPixmap("./images/timg.jpg"))

        self.label4.setText("<a href='www.baidu.com'>百度知道</a>")
        self.label4.setAlignment(Qt.AlignRight)
        self.label4.setToolTip("这是个超级链接")

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.label3)
        vlayout.addWidget(self.label4)

        self.label2.linkHovered.connect(self.linkHovered)

        self.label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vlayout)
        self.setWindowTitle("QLabel控件演示")
        self.resize(600, 600)

    def linkHovered(self):
        print('当鼠标划过')

    def linkClicked(self):
        print("当鼠标单击label4，触发事件")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LabelDemo()
    window.show()

    sys.exit(app.exec_())
