#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/30
"""
import sys

from PyQt5.QtWidgets import QDialog, QRadioButton, QHBoxLayout, QApplication


class RadioButtonDemo(QDialog):
    def __init__(self):
        super(RadioButtonDemo, self).__init__()
        self.button1 = QRadioButton('单选按钮1')
        self.button2 = QRadioButton('单选按钮2')
        self.h_layout = QHBoxLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButtonDemo')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.button_state)

        self.button2.toggled.connect(self.button_state)

        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)

        self.setLayout(self.h_layout)

    def button_state(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print('<' + radio_button.text() + '>被选中')
        else:
            print('<' + radio_button.text() + '>未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RadioButtonDemo()
    window.show()

    sys.exit(app.exec_())