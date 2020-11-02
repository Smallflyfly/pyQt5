#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QApplication


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.h_layout = QHBoxLayout()
        self.check_box1 = QCheckBox('复选框1')
        self.check_box2 = QCheckBox('复选框2')
        self.check_box3 = QCheckBox('复选框3')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框演示')
        self.check_box1.setChecked(True)
        self.check_box1.stateChanged.connect(self.check_state)

        self.check_box2.stateChanged.connect(self.check_state)

        self.check_box3.stateChanged.connect(self.check_state)
        self.check_box3.setTristate(True)
        self.check_box3.setCheckState(Qt.PartiallyChecked)

        self.h_layout.addWidget(self.check_box1)
        self.h_layout.addWidget(self.check_box2)
        self.h_layout.addWidget(self.check_box3)

        self.setLayout(self.h_layout)

    def check_state(self):
        checkbox1_state = self.check_box1.text() + ', isChecked=' + str(
            self.check_box1.isChecked()) + ', checkState=' + str(self.check_box1.checkState()) + '\n'
        checkbox2_state = self.check_box2.text() + ', isChecked=' + str(
            self.check_box2.isChecked()) + ', checkState=' + str(self.check_box2.checkState()) + '\n'
        checkbox3_state = self.check_box3.text() + ', isChecked=' + str(
            self.check_box3.isChecked()) + ', checkState=' + str(self.check_box3.checkState()) + '\n'
        print(checkbox1_state + checkbox2_state + checkbox3_state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QCheckBoxDemo()
    window.show()

    sys.exit(app.exec_())