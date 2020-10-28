#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/27
"""
import sys

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QToolTip, QPushButton, QHBoxLayout, QWidget


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)
        self.button1 = QPushButton('退出应用程序')
        self.initUI()

    def initUI(self):
        self.setWindowTitle("第一个主窗口")
        self.resize(400, 400)
        # self.status = self.statusBar()
        # self.status.showMessage("只出现几秒", 5000)
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.button1.setToolTip("这是一个按钮")
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

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        size = self.geometry()
        left = (screen_width - size.width()) // 2
        top = (screen_height - size.height()) // 2
        self.move(left, top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/ico/Safari 512x512.ico'))
    window = FirstMainWindow()
    window.center()

    window.show()

    sys.exit(app.exec_())


