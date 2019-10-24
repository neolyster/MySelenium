# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoFill.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QIcon
import os
from PyQt5.QtCore import  Qt,pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import ProcessData,SeleFunc

class Ui_Form(QtWidgets.QWidget):
    list = []#储存excel数据
    SaveFile = ''#保存文件的位置
    d1 = SeleFunc.AutoClass()
    index = True
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 346)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 60, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 60, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 90, 431, 231))
        self.listWidget.setObjectName("listWidget")
        self.pushButton.clicked.connect(self.jump_to_dir)
        self.pushButton_2.clicked.connect(self.jump_to_dir2)

        self.pushButton_3.clicked.connect(self.SeleData)
        self.pushButton_4.clicked.connect(self.Begin)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AutoFill"))
        self.pushButton.setText(_translate("Form", "选择Excel文件"))
        self.pushButton_2.setText(_translate("Form", "选择保存位置"))

        self.pushButton_3.setText(_translate("Form", "准备"))

        self.pushButton_4.setText(_translate("Form", "开始"))

    def jump_to_dir(self):

        file_name = QFileDialog.getOpenFileName(self,r'打开Excel文件',r'',r'Excel Files(*.xls *.xlsx)')#这里用空格隔开 不然又BUG
        self.lineEdit.setText(str(file_name[0]))

    def jump_to_dir2(self):
        SaveFile = QFileDialog.getExistingDirectory(self,r"选择文件夹","/")
        self.lineEdit_2.setText(SaveFile)
        self.d1.ChangeSavePath(SaveFile)
        print(self.d1.SavePath)

    def SeleData(self):
        try:
            self.list = ProcessData.FindData(self.lineEdit.text())
        except ValueError:
            print("Error")
    def Begin(self):
        #self.d1.Prepare()
        self.d1.FindTag(self.list)

        #print(self.d1.IsFirst)
        
if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    #widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())