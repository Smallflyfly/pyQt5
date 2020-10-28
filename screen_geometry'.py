#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/28
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def on_click_button(widget):
    print("窗口长: {}, 窗口宽".format(widget.size().width()), widget.size().height())
    print("窗口x: {}, 窗口y: {}".format(widget.x(), widget.y()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QWidget()

    btn = QPushButton(widget)
    btn.setText("按钮")
    btn.move(50, 50)
    btn.clicked.connect(lambda: on_click_button(widget))

    # 设置工作区的尺寸  非整个窗口尺寸
    widget.resize(400, 400)
    widget.move(500, 200)
    widget.setWindowTitle("屏幕坐标")

    widget.show()

    sys.exit(app.exec_())
