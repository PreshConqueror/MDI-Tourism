# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 120, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 111, 31))
        self.label_3.setObjectName("label_3")
        self.pushButtonLogin = QtWidgets.QPushButton(Dialog)
        self.pushButtonLogin.setGeometry(QtCore.QRect(190, 160, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 160, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_MSG = QtWidgets.QLabel(Dialog)
        self.label_MSG.setGeometry(QtCore.QRect(36, 209, 291, 61))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_MSG.setFont(font)
        self.label_MSG.setText("")
        self.label_MSG.setObjectName("label_MSG")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "User Name"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#c80352;\">LOGIN</span></p></body></html>"))
        self.pushButtonLogin.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Exit"))

