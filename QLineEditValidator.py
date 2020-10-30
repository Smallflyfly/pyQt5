#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/29
"""
import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class QLineEditValidatorDemo(QWidget):
    def __init__(self):
        super(QLineEditValidatorDemo, self).__init__()
        self.int_line_edit = QLineEdit()
        self.double_line_edit = QLineEdit()
        self.validator_line_edit = QLineEdit()
        self.int_validator = QIntValidator()
        self.double_validator = QDoubleValidator()
        self.reg_validator = QRegExpValidator()
        self.form_layout = QFormLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        self.form_layout.addRow('整数类型', self.int_line_edit)
        self.form_layout.addRow('浮点型', self.double_line_edit)
        self.form_layout.addRow('数字和字母', self.validator_line_edit)

        self.int_line_edit.setPlaceholderText('整型')
        self.double_line_edit.setPlaceholderText('浮点型')
        self.validator_line_edit.setPlaceholderText('数字和字母')

        self.int_validator.setRange(1, 99)
        self.double_validator.setRange(-360, 360)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_validator.setDecimals(2)

        _reg = QRegExp('[a-zA-Z0-9]+$')
        self.reg_validator.setRegExp(_reg)

        self.int_line_edit.setValidator(self.int_validator)
        self.double_line_edit.setValidator(self.double_validator)
        self.validator_line_edit.setValidator(self.reg_validator)

        self.setLayout(self.form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditValidatorDemo()
    window.show()

    sys.exit(app.exec_())

