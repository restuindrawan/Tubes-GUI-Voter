# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\rexTwo\Desktop\polling\redeem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import mysql.connector as mc
from view.home import *

class Login(object):
    def koneksi(self):
        con = pymysql.connect(db='polling', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(317, 224)
        self.btnVote = QtWidgets.QPushButton(Form)
        self.btnVote.setGeometry(QtCore.QRect(50, 130, 211, 31))
        self.btnVote.setStyleSheet("QPushButton{\n"
"    border: 2px solid;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 228, 70);\n"
"}")
        self.btnVote.setObjectName("btnVote")
        self.btnVote.clicked.connect(self.login)
        self.voteCode = QtWidgets.QLineEdit(Form)
        self.voteCode.setGeometry(QtCore.QRect(50, 90, 211, 31))
        self.voteCode.setStyleSheet("QLineEdit{\n"
"    border: 2px solid;\n"
"    border-radius : 10px;\n"
"}")
        self.voteCode.setObjectName("voteCode")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 161, 16))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def login(self):
        try:
            code = self.voteCode.text()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="polling"
            )

            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT code from voter where code like '" + code + "'")
            result = mycursor.fetchone()



            if result == None:
                self.messagebox("Alert", "Vote Code Salah")

            else:
                self.Form = QtWidgets.QDialog()
                self.ui = Home()
                self.ui.setupUi(self.Form)
                self.ui.select_data()
                self.ui.hidden.setText(code)
                self.ui.hidden.setHidden(True)
                self.ui.hidden2.setHidden(True)
                self.Form.show()
                Form.hide()

        except mc.Error as e:
            print("Error occured")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vote"))
        self.btnVote.setText(_translate("Form", "START VOTING"))
        self.label.setText(_translate("Form", "Insert your Vote Code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
