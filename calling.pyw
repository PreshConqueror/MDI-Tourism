#Calling Program
import sys
from login import *
from MDI_Tourism2 import *
from PyQt5.QtWidgets import *
     
class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonLogin.clicked.connect(self.loginuser)
        self.ui.pushButton_2.clicked.connect(self.exitlogin)

    def loginuser(self):
        uid = self.ui.lineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        msgtitle = 'Login Access'
        boxmsg = 'Access denial try again'

        user = 'Precious'
        passwd= '61910198'
        print("username: %s and password: %s" %(uid, pwd))

        if uid == user and pwd == passwd:
            boxmsg = 'Access granted'
            self.accept()

    def exitlogin(self):
        sys.exit(app.exec_())

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_sportsEvent)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_SportsVenue)
        self.ui.mdiArea.addSubWindow(self.ui.subwindowEventList)
        self.ui.mdiArea.addSubWindow(self.ui.subwindowVenueList)
        
        self.ui.subwindow_sportsEvent.setFixedSize(380, 350)
        self.ui.subwindow_SportsVenue.setFixedSize(500, 350)
        self.ui.subwindowEventList.setFixedSize(550, 400)
        self.ui.subwindowVenueList.setFixedSize(550, 350)
        
        self.ui.actionAdd_New_Event.triggered.connect(self.mdishowEvent)
        self.ui.actionAdd_New_Venue.triggered.connect(self.mdishowVenue)
        self.ui.actionShow_File_ContentEvent.triggered.connect(self.mdishowEventList)
        self.ui.actionShow_File_Content_Venue.triggered.connect(self.mdishowVenueList)

        self.ui.actionExit.triggered.connect(self.mdiexitlogin)

        self.ui.pushButtonReloadEvent.clicked.connect(self.reLoadEventDetails)
        self.ui.pushButtonReloadVenue.clicked.connect(self.reLoadVenueDetails)
        
        self.ui.pushButtonSaveEvent.clicked.connect(self.saveEventDetails)
        self.ui.pushButtonSaveVenue.clicked.connect(self.saveVenueDetails)

    def reLoadEventDetails(self):
        self.ui.listWidgetEventList.clear()
        f = open('eventvenues.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            self.ui.listWidgetEventList.addItem(line) 

    def reLoadVenueDetails(self):
        self.ui.listWidgetVenueList.clear()
        f = open('eventsports.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            self.ui.listWidgetVenueList.addItem(line) 

    def saveEventDetails(self):
        event_info = self.ui.lineEdit_venue.text()+', '+self.ui.lineEdit_Title.text()+', '+self.ui.lineEdit_Date.text()+', '+self.ui.lineEditStartTime.text()+', '+self.ui.lineEdit_EndTime.text()+', '+self.ui.lineEdit_NumGuest.text()
        f = open('eventvenues.txt', 'a' )
        f.write(event_info+"\n")
        f.close()
        self.ui.lineEdit_venue.setText('')
        self.ui.lineEdit_Title.setText('')
        self.ui.lineEdit_Date.setText('')
        self.ui.lineEditStartTime.setText('')
        self.ui.lineEdit_EndTime.setText('')
        self.ui.lineEdit_NumGuest.setText('')

    def saveVenueDetails(self):
        venue_info = self.ui.lineEditVName.text()+', '+self.ui.lineEdit_Address.text()+', '+self.ui.lineEdit_Capacity.text()
        f = open('eventsports.txt', 'a' )
        f.write(venue_info+"\n")
        f.close()
        self.ui.lineEditVName.setText('')
        self.ui.lineEdit_Address.setText('')
        self.ui.lineEdit_Capacity.setText('')

    def cascadeArrange(self):
        self.ui.mdiArea.cascadeSubWindows()
        
    def tileArrange(self):
        self.ui.mdiArea.tileSubWindows()

    def mdishowEvent(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[0])

    def mdishowVenue(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[1])

    def mdishowEventList(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[2])

    def mdishowVenueList(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[3])
        
    def mdiexitlogin(self):
        sys.exit(app.exec_())
        
if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
