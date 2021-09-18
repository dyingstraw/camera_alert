# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 562)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.light01 = QtWidgets.QLabel(self.centralwidget)
        self.light01.setGeometry(QtCore.QRect(490, 450, 41, 41))
        self.light01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.light01.setStyleSheet("#light01{\n"
"    background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.813725 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.light01.setText("")
        self.light01.setObjectName("light01")
        self.light02 = QtWidgets.QLabel(self.centralwidget)
        self.light02.setGeometry(QtCore.QRect(570, 450, 41, 41))
        self.light02.setStyleSheet("#light02{\n"
"    background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.813725 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.light02.setText("")
        self.light02.setObjectName("light02")
        self.light03 = QtWidgets.QLabel(self.centralwidget)
        self.light03.setGeometry(QtCore.QRect(650, 450, 41, 41))
        self.light03.setStyleSheet("#light03{\n"
"    background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.813725 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.light03.setText("")
        self.light03.setObjectName("light03")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 281, 471))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 461))
        self.groupBox.setObjectName("groupBox")
        self.logText = QtWidgets.QTextEdit(self.groupBox)
        self.logText.setGeometry(QtCore.QRect(10, 100, 251, 361))
        self.logText.setObjectName("logText")
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(20, 50, 240, 37))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.portSelect = QtWidgets.QSpinBox(self.widget1)
        self.portSelect.setMaximum(65536)
        self.portSelect.setObjectName("portSelect")
        self.horizontalLayout.addWidget(self.portSelect)
        self.openServer = QtWidgets.QPushButton(self.widget1)
        self.openServer.setObjectName("openServer")
        self.horizontalLayout.addWidget(self.openServer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 26))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondebug = QtWidgets.QAction(MainWindow)
        self.actiondebug.setObjectName("actiondebug")
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.menutest.addAction(self.actiondebug)
        self.menutest.addSeparator()
        self.menutest.addAction(self.actionsettings)
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.openServer, self.portSelect)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "服务"))
        self.label.setText(_translate("MainWindow", "端口："))
        self.openServer.setText(_translate("MainWindow", "打开服务器"))
        self.menutest.setTitle(_translate("MainWindow", "高级"))
        self.actiondebug.setText(_translate("MainWindow", "debug"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))

