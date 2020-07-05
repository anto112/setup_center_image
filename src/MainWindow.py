# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
    camera_open = QtCore.pyqtSignal()
    stop_video = QtCore.pyqtSignal()
    set_center = QtCore.pyqtSignal()
    check_show = QtCore.pyqtSignal()
    set_radius = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.centralwidget = QtWidgets.QWidget()

    def connect_signal_to_controller(self):
        self.pushButton_3.clicked.connect(self.camera_open)
        self.pushButton_4.clicked.connect(self.stop_video)
        self.pushButton.clicked.connect(self.set_center)
        self.checkBox.clicked.connect(self.check_show)
        self.pushButton_2.clicked.connect(self.set_radius)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 450)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 380, 50, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/stop.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 380, 50, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/camera_live.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(450, 110, 180, 310))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 30, 100, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('100')

        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 80, 100, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText('200')

        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 130, 100, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText('400')

        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 180, 100, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText('600')

        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 230, 100, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText('800')

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 270, 50, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 270, 100, 30))
        self.checkBox.setText("Show")
        self.checkBox.setObjectName("checkBox")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(18)
        self.label_10.setStyleSheet("border-width:3px;\n"
                                    "border: 1px solid black;")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 15, 180, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 60, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('1298')

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 50, 60, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('966')

        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(130, 10, 40, 65))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 400, 300))
        self.label.setText("")
        self.label.setStyleSheet("border-width:3px;\n"
                                 "border: 1px solid black;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.plusIcon = QtWidgets.QLabel(self.centralwidget)
        self.plusIcon.setGeometry(QtCore.QRect(10, 60, 400, 300))
        self.plusIcon.setStyleSheet("border-width:3px;\n"
                                    "border: 1px solid black;")
        self.plusIcon.setObjectName("plusIcon")


        blue = QtGui.QPixmap(400, 300)
        blue.fill(QtCore.Qt.transparent)
        p = QtGui.QPainter(blue)
        pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 0, 0)), 1)
        p.setPen(pen)
        p.drawLine(0, 150, 400, 150)
        p.drawLine(0, 0, 400, 300)
        p.drawLine(200, 0, 200, 300)
        p.drawLine(400, 0, 0, 300)
        p.end()
        self.plusIcon.setPixmap(blue)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connect_signal_to_controller()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton_4.setText(_translate("MainWindow", "Close Cam"))
        self.groupBox.setTitle(_translate("MainWindow", "Radius of circle:"))
        self.pushButton_2.setText(_translate("MainWindow", "Set"))
        self.label_5.setText(_translate("MainWindow", "1. "))
        self.label_6.setText(_translate("MainWindow", "2. "))
        self.label_7.setText(_translate("MainWindow", "3. "))
        self.label_8.setText(_translate("MainWindow", "4. "))
        self.label_9.setText(_translate("MainWindow", "5. "))
        # self.pushButton_3.setText(_translate("MainWindow", "Open Cam"))
        self.label_10.setText(_translate("MainWindow", "Main Window"))
        self.label_3.setText(_translate("MainWindow", "Icy:"))
        self.label_2.setText(_translate("MainWindow", "Icx:"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
