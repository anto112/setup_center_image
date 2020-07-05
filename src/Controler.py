from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *
import sys
from ModelData import *


class UiController:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_view = Ui_MainWindow(self.MainWindow)
        self.main_view.setupUi(self.MainWindow)
        self.model = ModelData
        self.give_response_from_view()
        self.MainWindow.show()
        self.main_view.plusIcon.hide()
        self.image = None
        self.cx = int(self.main_view.lineEdit.text())
        self.cy = int(self.main_view.lineEdit_2.text())
        self.r1 = int(self.main_view.lineEdit_3.text())
        self.r2 = int(self.main_view.lineEdit_4.text())
        self.r3 = int(self.main_view.lineEdit_5.text())
        self.r4 = int(self.main_view.lineEdit_6.text())
        self.r5 = int(self.main_view.lineEdit_7.text())
        self.videoStreamURL = 'http://192.168.100.104:8000/stream.mjpg'
        sys.exit(app.exec_())

    def give_response_from_view(self):
        self.main_view.camera_open.connect(self.onclick_open_camera)
        self.main_view.stop_video.connect(self.onclick_stop_video)
        self.main_view.set_center.connect(self.onclick_set_center)
        self.main_view.check_show.connect(self.onclick_show_circle)
        self.main_view.set_radius.connect(self.onclick_set_radius)

    def mouseReleaseEvent(self, e):
        self.model.mouseReleaseEvent(self, e)

    def saveImage(self):
        self.model.saveImage(self)

    def onclick_set_radius(self):
        self.model.onclick_set_radius(self)

    def onclick_show_circle(self):
        self.model.onclick_show_circle(self)

    def onclick_set_center(self):
        self.model.onclick_set_center(self)

    def onclick_open_camera(self):
        self.model.onclick_open_camera(self)
        self.onclick_play_button()

    def onclick_stop_video(self):
        self.model.stop_camera(self)

    def next_frame_slot(self):
        self.model.next_frame_slot(self)

    def display(self):
        self.model.display(self)

    def onclick_play_button(self):
        self.model.play_video(self)


if __name__ == '__main__':
    c = UiController()
    sys.exit(c.run())