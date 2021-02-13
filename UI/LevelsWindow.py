import main
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow(object):
    def setupUi(self, MainWindow):
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(340, 270, 121, 41))
        self.pushButton2.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(280, 270, 121, 41))
        self.pushButton1.setObjectName("pushButton")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "win"))
        self.pushButton.setText(_translate("MainWindow", "Level 1"))
        self.pushButton1.setText(_translate("MainWindow", "Level 2"))
