#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/10/29
"""
import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class QLineEditMaskDemo(QWidget):
    def __init__(self):
        super(QLineEditMaskDemo, self).__init__()
        self.form_layout = QFormLayout()
        self.ip_line_edit = QLineEdit()
        self.mac_line_edit = QLineEdit()
        self.date_line_edit = QLineEdit()
        self.license_line_edit = QLineEdit()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        self.ip_line_edit.setInputMask('000.000.000.000;_')
        self.mac_line_edit.setInputMask('HH:HH:HH:HH:HH;_')
        self.date_line_edit.setInputMask('0000-00-00;_')
        self.license_line_edit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        self.form_layout.addRow('数字掩码', self.ip_line_edit)
        self.form_layout.addRow('Mac掩码', self.mac_line_edit)
        self.form_layout.addRow('日期掩码', self.date_line_edit)
        self.form_layout.addRow('许可证掩码', self.license_line_edit)

        self.setLayout(self.form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditMaskDemo()
    window.show()

    sys.exit(app.exec_())
