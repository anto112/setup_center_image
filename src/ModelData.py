import os
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import math
import datetime


class ModelData:
    """ Initial Class"""

    def __init__(self):
        super(ModelData, self).__init__()

    def onclick_set_radius(self):
        self.r1 = int(self.main_view.lineEdit_3.text())
        self.r2 = int(self.main_view.lineEdit_4.text())
        self.r3 = int(self.main_view.lineEdit_5.text())
        self.r4 = int(self.main_view.lineEdit_6.text())
        self.r5 = int(self.main_view.lineEdit_7.text())

    def onclick_show_circle(self):
        if self.image is None:
            pass
        else:
            if self.main_view.checkBox.isChecked():
                self.img_circle = self.image_ori.copy()
                h, w = self.img_circle.shape[:2]
                b = self.cy
                a = round(b / math.sin(45))
                cv2.circle(self.img_circle, (self.cx, self.cy), self.r1, (255, 0, 4), 4, -1)
                cv2.circle(self.img_circle, (self.cx, self.cy), self.r2, (255, 0, 4), 4, -1)
                cv2.circle(self.img_circle, (self.cx, self.cy), self.r3, (255, 0, 4), 4, -1)
                cv2.circle(self.img_circle, (self.cx, self.cy), self.r4, (255, 0, 4), 4, -1)
                cv2.circle(self.img_circle, (self.cx, self.cy), self.r5, (255, 0, 4), 4, -1)
                cv2.line(self.img_circle, (0, self.cy), (self.cx,self.cy), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx, self.cy), (w, self.cy), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx, 0), (self.cx,self.cy), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx, self.cy), (self.cx, h), (255, 0, 4), 3)
                #line 45 degree
                cv2.line(self.img_circle, (self.cx + a, 0), (self.cx, self.cy), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx, self.cy), (self.cx - a, h), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx - a, 0), (self.cx, self.cy), (255, 0, 4), 3)
                cv2.line(self.img_circle, (self.cx, self.cy), (self.cx + a, h), (255, 0, 4), 3)
                self.display()

    def display(self):
        if self.main_view.checkBox.isChecked():
            self.img = cv2.resize(self.img_circle, (400, 300), interpolation=cv2.INTER_AREA)
        else:
            self.img = cv2.resize(self.image_ori, (400, 300), interpolation=cv2.INTER_AREA)
        my_label = self.main_view.label
        image = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        my_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def onclick_set_center(self):
        self.cx = int(self.main_view.lineEdit.text())
        self.cy = int(self.main_view.lineEdit_2.text())
        self.onclick_show_circle()

    def onclick_open_camera(self):
        self.cap = cv2.VideoCapture(self.videoStreamURL)
        if self.cap.isOpened is False:
            pass
        else:
            self.next_frame_slot()
            self.main_view.label.mouseReleaseEvent = self.mouseReleaseEvent

    def stop_camera(self):
        if self.cap:
            self.timer.stop()
            self.cap.release()
            self.main_view.label.clear()
        else:
            pass

    def next_frame_slot(self):
        if self.cap.isOpened is False:
            pass
        else:
            self.ret, self.image = self.cap.read()
            if self.image is None:
                pass
            else:
                self.image_ori = self.image.copy()
                self.onclick_show_circle()
                self.fps = self.cap.get(cv2.CAP_PROP_FPS)

                self.display()

    def play_video(self):
        """ Video Controller"""
        if self.cap.isOpened():
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.next_frame_slot)
            self.timer.start(1000. / self.fps)

    def mouseReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            pass

        else:
            menu = QtWidgets.QMenu()
            Action = menu.addAction("Save Image")
            Action.triggered.connect(self.saveImage)
            menu.exec_(e.globalPos())

    def saveImage(self):
        ss = datetime.datetime.now().strftime("%d-%H-%M-%S")
        filename = "../result/image_" + str(ss) + ".png"
        cv2.imwrite(filename, self.image)
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Save File")
        msgbox.setText("\nImage saved succeed !!")
        msgbox.setIconPixmap(QtGui.QPixmap('../assets/check.png'))
        msgbox.exec()

