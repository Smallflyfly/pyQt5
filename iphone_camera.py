#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/02
"""
import cv2


def camera_capture():
    cam = cv2.VideoCapture(0)
    while True:
        _, im = cam.read()

        cv2.imshow('im', im)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camera_capture()