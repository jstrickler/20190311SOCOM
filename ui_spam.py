# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spam.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Spam(object):
    def setupUi(self, Spam):
        Spam.setObjectName("Spam")
        Spam.resize(717, 487)
        self.centralwidget = QtWidgets.QWidget(Spam)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_hello = QtWidgets.QLabel(self.centralwidget)
        self.lab_hello.setObjectName("lab_hello")
        self.verticalLayout.addWidget(self.lab_hello)
        self.bt_push = QtWidgets.QPushButton(self.centralwidget)
        self.bt_push.setObjectName("bt_push")
        self.verticalLayout.addWidget(self.bt_push)
        self.bt_dont = QtWidgets.QPushButton(self.centralwidget)
        self.bt_dont.setObjectName("bt_dont")
        self.verticalLayout.addWidget(self.bt_dont)
        self.cb_milk = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_milk.setObjectName("cb_milk")
        self.verticalLayout.addWidget(self.cb_milk)
        self.cb_cookies = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_cookies.setObjectName("cb_cookies")
        self.verticalLayout.addWidget(self.cb_cookies)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        Spam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Spam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWombats = QtWidgets.QMenu(self.menubar)
        self.menuWombats.setObjectName("menuWombats")
        Spam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Spam)
        self.statusbar.setObjectName("statusbar")
        Spam.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Spam)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Spam)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(Spam)
        self.actionQuit.setObjectName("actionQuit")
        self.actionEat = QtWidgets.QAction(Spam)
        self.actionEat.setObjectName("actionEat")
        self.actionExcrete = QtWidgets.QAction(Spam)
        self.actionExcrete.setObjectName("actionExcrete")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuWombats.addAction(self.actionEat)
        self.menuWombats.addAction(self.actionExcrete)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWombats.menuAction())

        self.retranslateUi(Spam)
        self.actionQuit.triggered.connect(Spam.close)
        self.bt_push.clicked.connect(Spam.handle_push)
        self.bt_dont.clicked.connect(Spam.handle_dont)
        QtCore.QMetaObject.connectSlotsByName(Spam)
        Spam.setTabOrder(self.bt_push, self.bt_dont)
        Spam.setTabOrder(self.bt_dont, self.cb_milk)
        Spam.setTabOrder(self.cb_milk, self.cb_cookies)

    def retranslateUi(self, Spam):
        _translate = QtCore.QCoreApplication.translate
        Spam.setWindowTitle(_translate("Spam", "MainWindow"))
        self.lab_hello.setText(_translate("Spam", "HELLO SOCOM WORLD"))
        self.bt_push.setText(_translate("Spam", "Push Me"))
        self.bt_dont.setText(_translate("Spam", "DO NOT PUSH!"))
        self.cb_milk.setText(_translate("Spam", "Milk"))
        self.cb_cookies.setText(_translate("Spam", "Cookies"))
        self.label.setText(_translate("Spam", "TextLabel"))
        self.menuFile.setTitle(_translate("Spam", "File"))
        self.menuEdit.setTitle(_translate("Spam", "Edit"))
        self.menuWombats.setTitle(_translate("Spam", "Wombats"))
        self.actionOpen.setText(_translate("Spam", "Open"))
        self.actionClose.setText(_translate("Spam", "Close"))
        self.actionQuit.setText(_translate("Spam", "Quit"))
        self.actionEat.setText(_translate("Spam", "Eat"))
        self.actionExcrete.setText(_translate("Spam", "Excrete"))

