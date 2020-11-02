#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider, QApplication


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.label = QLabel('滑块标签')
        self.v_layout = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider2 = QSlider(Qt.Vertical)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.adjustSize()

        # 设置滑块的最小值
        self.slider.setMinimum(12)
        # 设置最大值
        self.slider.setMaximum(50)
        # 设置步长
        self.slider.setSingleStep(1)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度位置 刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.value_change)

        # 设置滑块的最小值
        self.slider2.setMinimum(12)
        # 设置最大值
        self.slider2.setMaximum(50)
        # 设置步长
        self.slider2.setSingleStep(1)
        # 设置当前值
        self.slider2.setValue(18)
        # 设置刻度位置 刻度在下方
        self.slider2.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider2.setTickInterval(1)
        self.slider2.valueChanged.connect(self.value_change)

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.slider)
        self.v_layout.addWidget(self.slider2)

        self.setLayout(self.v_layout)

    def value_change(self):
        print('当前值：{}'.format(self.sender().value()))
        size = self.sender().value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSliderDemo()
    window.show()

    sys.exit(app.exec_())
