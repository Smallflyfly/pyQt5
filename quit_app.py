#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/28
"""
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QHBoxLayout, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(400, 400)
        self.setWindowTitle("退出应用程序")

        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.on_click_button)

        layout_ = QHBoxLayout()
        layout_.addWidget(self.button1)
        main_frame = QWidget()
        main_frame.setLayout(layout_)
        self.setCentralWidget(main_frame)

    # 单击事件的方法
    def on_click_button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

