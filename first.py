#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/26
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个窗口
    widget = QWidget()
    widget.resize(400, 400)
    widget.move(300, 300)
    widget.setWindowTitle("This is a window")
    widget.show()

    # 进入主程序循环，并通过exit安全退出主循环
    sys.exit(app.exec_())
