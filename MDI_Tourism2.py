# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MDI_Tourism2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 1181, 721))
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow_sportsEvent = QtWidgets.QWidget()
        self.subwindow_sportsEvent.setObjectName("subwindow_sportsEvent")
        self.labelTitle_sportsEvent = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelTitle_sportsEvent.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTitle_sportsEvent.setFont(font)
        self.labelTitle_sportsEvent.setObjectName("labelTitle_sportsEvent")
        self.labelTitle = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelTitle.setGeometry(QtCore.QRect(20, 90, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelDate = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelDate.setGeometry(QtCore.QRect(20, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.labelStartTime = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelStartTime.setGeometry(QtCore.QRect(20, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelStartTime.setFont(font)
        self.labelStartTime.setObjectName("labelStartTime")
        self.labelEndTime = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelEndTime.setGeometry(QtCore.QRect(20, 210, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelEndTime.setFont(font)
        self.labelEndTime.setObjectName("labelEndTime")
        self.labelNumGuest = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.labelNumGuest.setGeometry(QtCore.QRect(20, 250, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNumGuest.setFont(font)
        self.labelNumGuest.setObjectName("labelNumGuest")
        self.lineEdit_Title = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEdit_Title.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.lineEdit_Date = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEdit_Date.setGeometry(QtCore.QRect(180, 130, 161, 20))
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.lineEditStartTime = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEditStartTime.setGeometry(QtCore.QRect(180, 170, 161, 20))
        self.lineEditStartTime.setObjectName("lineEditStartTime")
        self.lineEdit_EndTime = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEdit_EndTime.setGeometry(QtCore.QRect(180, 210, 161, 20))
        self.lineEdit_EndTime.setObjectName("lineEdit_EndTime")
        self.lineEdit_NumGuest = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEdit_NumGuest.setGeometry(QtCore.QRect(180, 250, 161, 20))
        self.lineEdit_NumGuest.setObjectName("lineEdit_NumGuest")
        self.pushButtonSaveEvent = QtWidgets.QPushButton(self.subwindow_sportsEvent)
        self.pushButtonSaveEvent.setGeometry(QtCore.QRect(180, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveEvent.setFont(font)
        self.pushButtonSaveEvent.setObjectName("pushButtonSaveEvent")
        self.label_venue = QtWidgets.QLabel(self.subwindow_sportsEvent)
        self.label_venue.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_venue.setFont(font)
        self.label_venue.setObjectName("label_venue")
        self.lineEdit_venue = QtWidgets.QLineEdit(self.subwindow_sportsEvent)
        self.lineEdit_venue.setGeometry(QtCore.QRect(180, 50, 161, 20))
        self.lineEdit_venue.setObjectName("lineEdit_venue")
        self.subwindow_SportsVenue = QtWidgets.QWidget()
        self.subwindow_SportsVenue.setObjectName("subwindow_SportsVenue")
        self.labelTitle_sportsVenue = QtWidgets.QLabel(self.subwindow_SportsVenue)
        self.labelTitle_sportsVenue.setGeometry(QtCore.QRect(120, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTitle_sportsVenue.setFont(font)
        self.labelTitle_sportsVenue.setObjectName("labelTitle_sportsVenue")
        self.labelVName = QtWidgets.QLabel(self.subwindow_SportsVenue)
        self.labelVName.setGeometry(QtCore.QRect(30, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelVName.setFont(font)
        self.labelVName.setObjectName("labelVName")
        self.label_VenueAddress = QtWidgets.QLabel(self.subwindow_SportsVenue)
        self.label_VenueAddress.setGeometry(QtCore.QRect(30, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_VenueAddress.setFont(font)
        self.label_VenueAddress.setObjectName("label_VenueAddress")
        self.label_Capacity = QtWidgets.QLabel(self.subwindow_SportsVenue)
        self.label_Capacity.setGeometry(QtCore.QRect(30, 160, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Capacity.setFont(font)
        self.label_Capacity.setObjectName("label_Capacity")
        self.lineEditVName = QtWidgets.QLineEdit(self.subwindow_SportsVenue)
        self.lineEditVName.setGeometry(QtCore.QRect(130, 80, 251, 20))
        self.lineEditVName.setObjectName("lineEditVName")
        self.lineEdit_Address = QtWidgets.QLineEdit(self.subwindow_SportsVenue)
        self.lineEdit_Address.setGeometry(QtCore.QRect(130, 120, 251, 20))
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.lineEdit_Capacity = QtWidgets.QLineEdit(self.subwindow_SportsVenue)
        self.lineEdit_Capacity.setGeometry(QtCore.QRect(130, 160, 251, 20))
        self.lineEdit_Capacity.setObjectName("lineEdit_Capacity")
        self.pushButtonSaveVenue = QtWidgets.QPushButton(self.subwindow_SportsVenue)
        self.pushButtonSaveVenue.setGeometry(QtCore.QRect(130, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveVenue.setFont(font)
        self.pushButtonSaveVenue.setObjectName("pushButtonSaveVenue")
        self.subwindowEventList = QtWidgets.QWidget()
        self.subwindowEventList.setObjectName("subwindowEventList")
        self.listWidgetEventList = QtWidgets.QListWidget(self.subwindowEventList)
        self.listWidgetEventList.setGeometry(QtCore.QRect(30, 50, 481, 281))
        self.listWidgetEventList.setObjectName("listWidgetEventList")
        self.pushButtonReloadEvent = QtWidgets.QPushButton(self.subwindowEventList)
        self.pushButtonReloadEvent.setGeometry(QtCore.QRect(390, 350, 121, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReloadEvent.setFont(font)
        self.pushButtonReloadEvent.setObjectName("pushButtonReloadEvent")
        self.labelTitle_2 = QtWidgets.QLabel(self.subwindowEventList)
        self.labelTitle_2.setGeometry(QtCore.QRect(200, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setObjectName("labelTitle_2")
        self.subwindowVenueList = QtWidgets.QWidget()
        self.subwindowVenueList.setObjectName("subwindowVenueList")
        self.labelVenuTitle = QtWidgets.QLabel(self.subwindowVenueList)
        self.labelVenuTitle.setGeometry(QtCore.QRect(210, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelVenuTitle.setFont(font)
        self.labelVenuTitle.setObjectName("labelVenuTitle")
        self.listWidgetVenueList = QtWidgets.QListWidget(self.subwindowVenueList)
        self.listWidgetVenueList.setGeometry(QtCore.QRect(30, 60, 481, 241))
        self.listWidgetVenueList.setObjectName("listWidgetVenueList")
        self.pushButtonReloadVenue = QtWidgets.QPushButton(self.subwindowVenueList)
        self.pushButtonReloadVenue.setGeometry(QtCore.QRect(390, 310, 121, 23))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReloadVenue.setFont(font)
        self.pushButtonReloadVenue.setObjectName("pushButtonReloadVenue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 21))
        self.menubar.setObjectName("menubar")
        self.menuSubWindows = QtWidgets.QMenu(self.menubar)
        self.menuSubWindows.setObjectName("menuSubWindows")
        self.menuArrange = QtWidgets.QMenu(self.menubar)
        self.menuArrange.setObjectName("menuArrange")
        self.menuOlympic_Events = QtWidgets.QMenu(self.menuArrange)
        self.menuOlympic_Events.setObjectName("menuOlympic_Events")
        self.menuOlympic_Venues = QtWidgets.QMenu(self.menuArrange)
        self.menuOlympic_Venues.setObjectName("menuOlympic_Venues")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSports_Event = QtWidgets.QAction(MainWindow)
        self.actionSports_Event.setObjectName("actionSports_Event")
        self.actionSports_Venue = QtWidgets.QAction(MainWindow)
        self.actionSports_Venue.setObjectName("actionSports_Venue")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_New_Event = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Event.setObjectName("actionAdd_New_Event")
        self.actionEdit_Existing_Event = QtWidgets.QAction(MainWindow)
        self.actionEdit_Existing_Event.setObjectName("actionEdit_Existing_Event")
        self.actionDelete_Existing = QtWidgets.QAction(MainWindow)
        self.actionDelete_Existing.setObjectName("actionDelete_Existing")
        self.actionShow_File_ContentEvent = QtWidgets.QAction(MainWindow)
        self.actionShow_File_ContentEvent.setObjectName("actionShow_File_ContentEvent")
        self.actionAdd_New_Venue = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Venue.setObjectName("actionAdd_New_Venue")
        self.actionEdit_Existing_Record = QtWidgets.QAction(MainWindow)
        self.actionEdit_Existing_Record.setObjectName("actionEdit_Existing_Record")
        self.actionDelete_Existing_Record = QtWidgets.QAction(MainWindow)
        self.actionDelete_Existing_Record.setObjectName("actionDelete_Existing_Record")
        self.actionShow_File_Content_Venue = QtWidgets.QAction(MainWindow)
        self.actionShow_File_Content_Venue.setObjectName("actionShow_File_Content_Venue")
        self.actionArrange_Casscade = QtWidgets.QAction(MainWindow)
        self.actionArrange_Casscade.setObjectName("actionArrange_Casscade")
        self.actionArrange_Tile = QtWidgets.QAction(MainWindow)
        self.actionArrange_Tile.setObjectName("actionArrange_Tile")
        self.menuSubWindows.addAction(self.actionArrange_Casscade)
        self.menuSubWindows.addAction(self.actionArrange_Tile)
        self.menuSubWindows.addSeparator()
        self.menuSubWindows.addAction(self.actionExit)
        self.menuOlympic_Events.addAction(self.actionAdd_New_Event)
        self.menuOlympic_Events.addAction(self.actionEdit_Existing_Event)
        self.menuOlympic_Events.addAction(self.actionDelete_Existing)
        self.menuOlympic_Events.addAction(self.actionShow_File_ContentEvent)
        self.menuOlympic_Venues.addAction(self.actionAdd_New_Venue)
        self.menuOlympic_Venues.addAction(self.actionEdit_Existing_Record)
        self.menuOlympic_Venues.addAction(self.actionDelete_Existing_Record)
        self.menuOlympic_Venues.addAction(self.actionShow_File_Content_Venue)
        self.menuArrange.addAction(self.menuOlympic_Events.menuAction())
        self.menuArrange.addAction(self.menuOlympic_Venues.menuAction())
        self.menubar.addAction(self.menuSubWindows.menuAction())
        self.menubar.addAction(self.menuArrange.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subwindow_sportsEvent.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.labelTitle_sportsEvent.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#c8066e;\">TOURISM EVENTS</span></p></body></html>"))
        self.labelTitle.setText(_translate("MainWindow", "Event Title"))
        self.labelDate.setText(_translate("MainWindow", "Event Date"))
        self.labelStartTime.setText(_translate("MainWindow", "Start Time"))
        self.labelEndTime.setText(_translate("MainWindow", "End Time"))
        self.labelNumGuest.setText(_translate("MainWindow", "Number Of Guest"))
        self.pushButtonSaveEvent.setText(_translate("MainWindow", "Save"))
        self.label_venue.setText(_translate("MainWindow", "Event Venue"))
        self.subwindow_SportsVenue.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.labelTitle_sportsVenue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#c804be;\">TOURISM VENUE</span></p></body></html>"))
        self.labelVName.setText(_translate("MainWindow", "Venue Name"))
        self.label_VenueAddress.setText(_translate("MainWindow", "Venue Address"))
        self.label_Capacity.setText(_translate("MainWindow", "Capacity"))
        self.pushButtonSaveVenue.setText(_translate("MainWindow", "Save"))
        self.subwindowEventList.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.pushButtonReloadEvent.setText(_translate("MainWindow", "Reload Events"))
        self.labelTitle_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#c200c8;\">EVENT LIST</span></p></body></html>"))
        self.subwindowVenueList.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.labelVenuTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#c801a4;\">VENUE LIST</span></p></body></html>"))
        self.pushButtonReloadVenue.setText(_translate("MainWindow", "Reload Events"))
        self.menuSubWindows.setTitle(_translate("MainWindow", "File"))
        self.menuArrange.setTitle(_translate("MainWindow", "Data Maintance"))
        self.menuOlympic_Events.setTitle(_translate("MainWindow", "Sports Events"))
        self.menuOlympic_Venues.setTitle(_translate("MainWindow", "Sports Venues"))
        self.menuReport.setTitle(_translate("MainWindow", "Reporting"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSports_Event.setText(_translate("MainWindow", "Sports Event"))
        self.actionSports_Venue.setText(_translate("MainWindow", "Sports Venue"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_New_Event.setText(_translate("MainWindow", "Add New Event"))
        self.actionEdit_Existing_Event.setText(_translate("MainWindow", "Edit Existing Event"))
        self.actionDelete_Existing.setText(_translate("MainWindow", "Delete Existing"))
        self.actionShow_File_ContentEvent.setText(_translate("MainWindow", "Show File Content"))
        self.actionAdd_New_Venue.setText(_translate("MainWindow", "Add New Venue"))
        self.actionEdit_Existing_Record.setText(_translate("MainWindow", "Edit Existing Record"))
        self.actionDelete_Existing_Record.setText(_translate("MainWindow", "Delete Existing Record"))
        self.actionShow_File_Content_Venue.setText(_translate("MainWindow", "Show File Content"))
        self.actionArrange_Casscade.setText(_translate("MainWindow", "Arrange Casscade"))
        self.actionArrange_Tile.setText(_translate("MainWindow", "Arrange Tile"))

