# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/Settings.ui'
#
# Created: Wed Feb 12 04:10:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(546, 185)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName("verticalLayout")
		self.formLayout = QtGui.QFormLayout()
		self.formLayout.setObjectName("formLayout")
		self.lb_username = QtGui.QLabel(Form)
		self.lb_username.setObjectName("lb_username")
		self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_username)
		self.le_username = QtGui.QLineEdit(Form)
		self.le_username.setObjectName("le_username")
		self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_username)
		self.lb_passwd = QtGui.QLabel(Form)
		self.lb_passwd.setObjectName("lb_passwd")
		self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lb_passwd)
		self.le_passwd = QtGui.QLineEdit(Form)
		self.le_passwd.setEchoMode(QtGui.QLineEdit.Password)
		self.le_passwd.setObjectName("le_passwd")
		self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_passwd)
		self.line = QtGui.QFrame(Form)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.line)
		self.lb_comicViewer = QtGui.QLabel(Form)
		self.lb_comicViewer.setObjectName("lb_comicViewer")
		self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lb_comicViewer)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.le_comicViewer = QtGui.QLineEdit(Form)
		self.le_comicViewer.setMinimumSize(QtCore.QSize(300, 0))
		self.le_comicViewer.setText("")
		self.le_comicViewer.setObjectName("le_comicViewer")
		self.horizontalLayout.addWidget(self.le_comicViewer)
		self.btn_comicViewer = QtGui.QPushButton(Form)
		self.btn_comicViewer.setObjectName("btn_comicViewer")
		self.horizontalLayout.addWidget(self.btn_comicViewer)
		self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
		self.lb_download = QtGui.QLabel(Form)
		self.lb_download.setObjectName("lb_download")
		self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lb_download)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.le_download = QtGui.QLineEdit(Form)
		self.le_download.setMinimumSize(QtCore.QSize(300, 0))
		self.le_download.setObjectName("le_download")
		self.horizontalLayout_2.addWidget(self.le_download)
		self.btn_download = QtGui.QPushButton(Form)
		self.btn_download.setObjectName("btn_download")
		self.horizontalLayout_2.addWidget(self.btn_download)
		self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
		self.verticalLayout.addLayout(self.formLayout)
		self.buttonBox = QtGui.QDialogButtonBox(Form)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)
		self.lb_username.setBuddy(self.le_username)
		self.lb_passwd.setBuddy(self.le_passwd)
		self.lb_comicViewer.setBuddy(self.le_comicViewer)
		self.lb_download.setBuddy(self.le_download)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Settings", None, QtGui.QApplication.UnicodeUTF8))
		self.lb_username.setText(QtGui.QApplication.translate("Form", "Username:", None, QtGui.QApplication.UnicodeUTF8))
		self.lb_passwd.setText(QtGui.QApplication.translate("Form", "Password:", None, QtGui.QApplication.UnicodeUTF8))
		self.lb_comicViewer.setText(QtGui.QApplication.translate("Form", "Comic viewer", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_comicViewer.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
		self.lb_download.setText(QtGui.QApplication.translate("Form", "Download Directory:", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_download.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))

