#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QApplication


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.v_layout = QVBoxLayout()
        self.label = QLabel('请选择编程语言')
        self.comboBox = QComboBox()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件')
        self.comboBox.addItem('C++')
        self.comboBox.addItem('C')
        self.comboBox.addItem('Python')
        self.comboBox.addItems(['Java', 'C#', 'R'])
        self.comboBox.currentIndexChanged.connect(self.selection_change)

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.comboBox)

        self.setLayout(self.v_layout)

    def selection_change(self, index):
        self.label.setText(self.comboBox.currentText())
        # self.label.adjustSize()

        for count in range(self.comboBox.count()):
            print('item {} = {}'.format(count, self.comboBox.itemText(count)))
        print('current index {}, selection changed {}'.format(index, self.comboBox.currentText()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QComboBoxDemo()
    window.show()

    sys.exit(app.exec_())
