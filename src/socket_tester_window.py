# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\socket_tester_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.client = QtWidgets.QWidget()
        self.client.setObjectName("client")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.client)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ip = QtWidgets.QLineEdit(self.client)
        self.ip.setObjectName("ip")
        self.horizontalLayout.addWidget(self.ip)
        self.port = QtWidgets.QLineEdit(self.client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.Connect = QtWidgets.QPushButton(self.client)
        self.Connect.setObjectName("Connect")
        self.horizontalLayout.addWidget(self.Connect)
        self.disconnect_client = QtWidgets.QPushButton(self.client)
        self.disconnect_client.setObjectName("disconnect_client")
        self.horizontalLayout.addWidget(self.disconnect_client)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.client)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.message = QtWidgets.QLineEdit(self.client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setText("")
        self.message.setObjectName("message")
        self.horizontalLayout_2.addWidget(self.message)
        self.end_char = QtWidgets.QComboBox(self.client)
        self.end_char.setObjectName("end_char")
        self.end_char.addItem("")
        self.end_char.addItem("")
        self.end_char.addItem("")
        self.end_char.addItem("")
        self.horizontalLayout_2.addWidget(self.end_char)
        self.send = QtWidgets.QPushButton(self.client)
        self.send.setObjectName("send")
        self.horizontalLayout_2.addWidget(self.send)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.client, "")
        self.server = QtWidgets.QWidget()
        self.server.setObjectName("server")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.server)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ip_server = QtWidgets.QLineEdit(self.server)
        self.ip_server.setObjectName("ip_server")
        self.horizontalLayout_3.addWidget(self.ip_server)
        self.port_server = QtWidgets.QLineEdit(self.server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_server.sizePolicy().hasHeightForWidth())
        self.port_server.setSizePolicy(sizePolicy)
        self.port_server.setObjectName("port_server")
        self.horizontalLayout_3.addWidget(self.port_server)
        self.bind = QtWidgets.QPushButton(self.server)
        self.bind.setObjectName("bind")
        self.horizontalLayout_3.addWidget(self.bind)
        self.disconnect_server = QtWidgets.QPushButton(self.server)
        self.disconnect_server.setObjectName("disconnect_server")
        self.horizontalLayout_3.addWidget(self.disconnect_server)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.server_text = QtWidgets.QTextEdit(self.server)
        self.server_text.setReadOnly(True)
        self.server_text.setObjectName("server_text")
        self.gridLayout_5.addWidget(self.server_text, 1, 0, 1, 2)
        self.message_server = QtWidgets.QLineEdit(self.server)
        self.message_server.setText("")
        self.message_server.setObjectName("message_server")
        self.gridLayout_5.addWidget(self.message_server, 2, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ip_recipient = QtWidgets.QLineEdit(self.server)
        self.ip_recipient.setText("")
        self.ip_recipient.setObjectName("ip_recipient")
        self.gridLayout_4.addWidget(self.ip_recipient, 1, 0, 1, 2)
        self.send_to = QtWidgets.QPushButton(self.server)
        self.send_to.setObjectName("send_to")
        self.gridLayout_4.addWidget(self.send_to, 1, 2, 1, 1)
        self.send_stream = QtWidgets.QPushButton(self.server)
        self.send_stream.setObjectName("send_stream")
        self.gridLayout_4.addWidget(self.send_stream, 0, 2, 1, 1)
        self.end_char_server = QtWidgets.QComboBox(self.server)
        self.end_char_server.setObjectName("end_char_server")
        self.end_char_server.addItem("")
        self.end_char_server.addItem("")
        self.end_char_server.addItem("")
        self.end_char_server.addItem("")
        self.gridLayout_4.addWidget(self.end_char_server, 0, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.tabWidget.addTab(self.server, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ip.setPlaceholderText(_translate("MainWindow", "IP"))
        self.port.setPlaceholderText(_translate("MainWindow", "Port"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.disconnect_client.setText(_translate("MainWindow", "Disconnect"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.message.setPlaceholderText(_translate("MainWindow", "Message"))
        self.end_char.setItemText(0, _translate("MainWindow", "\\n"))
        self.end_char.setItemText(1, _translate("MainWindow", "\\r\\n"))
        self.end_char.setItemText(2, _translate("MainWindow", "\\t"))
        self.end_char.setItemText(3, _translate("MainWindow", "None"))
        self.send.setText(_translate("MainWindow", "Send Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.client), _translate("MainWindow", "Client"))
        self.ip_server.setText(_translate("MainWindow", "127.0.0.1"))
        self.ip_server.setPlaceholderText(_translate("MainWindow", "IP"))
        self.port_server.setText(_translate("MainWindow", "8080"))
        self.port_server.setPlaceholderText(_translate("MainWindow", "Port"))
        self.bind.setText(_translate("MainWindow", "Bind"))
        self.disconnect_server.setText(_translate("MainWindow", "Disconnect"))
        self.message_server.setPlaceholderText(_translate("MainWindow", "Message"))
        self.ip_recipient.setPlaceholderText(_translate("MainWindow", "IP"))
        self.send_to.setText(_translate("MainWindow", "Send To"))
        self.send_stream.setText(_translate("MainWindow", "Send Stream"))
        self.end_char_server.setItemText(0, _translate("MainWindow", "\\n"))
        self.end_char_server.setItemText(1, _translate("MainWindow", "\\r\\n"))
        self.end_char_server.setItemText(2, _translate("MainWindow", "\\t"))
        self.end_char_server.setItemText(3, _translate("MainWindow", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.server), _translate("MainWindow", "Echo Server"))
