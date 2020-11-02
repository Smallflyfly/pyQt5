#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QApplication


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.v_layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.spinbox = QSpinBox()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件')

        self.label.setAlignment(Qt.AlignCenter)

        self.spinbox.valueChanged.connect(self.value_change)
        self.spinbox.setValue(5)
        self.spinbox.setRange(0, 10)
        self.spinbox.setSingleStep(2)

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.spinbox)

        self.setLayout(self.v_layout)

    def value_change(self):
        self.label.setText('当前值: {}'.format(self.spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSpinBoxDemo()
    window.show()

    sys.exit(app.exec_())