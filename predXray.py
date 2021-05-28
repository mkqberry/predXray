# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bestGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from dl import DeepLearning

class Ui_Form(object):
    fpath = ""
    fname = ""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 438)
        self.buttonResult = QtWidgets.QPushButton(Form)
        self.buttonResult.setGeometry(QtCore.QRect(470, 170, 93, 28))
        self.buttonResult.setObjectName("buttonResult")
        self.buttonChoose = QtWidgets.QPushButton(Form)
        self.buttonChoose.setGeometry(QtCore.QRect(590, 170, 93, 28))
        self.buttonChoose.setObjectName("buttonChoose")
        self.labelShowImage = QtWidgets.QLabel(Form)
        self.labelShowImage.setGeometry(QtCore.QRect(30, 20, 301, 291))
        self.labelShowImage.setText("")
        self.labelShowImage.setObjectName("labelShowImage")
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setGeometry(QtCore.QRect(20, 370, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.buttonChoose.clicked.connect(self.loadImage)
        self.buttonResult.setEnabled(False)
        self.buttonResult.clicked.connect(self.getResult)
        self.labelResult.setText("Please upload an X-Ray image!")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def loadImage(self):
        fpath = QFileDialog.getOpenFileName(caption="Open File", filter="Image Files (*.png *.jpg *.jpeg)")
        ipath = fpath[0]
        if len(ipath)>0:
            self.buttonResult.setEnabled(True)
            self.buttonChoose.setEnabled(False)
            self.labelResult.setText("Image uploaded successfully!")

        pixmap = QPixmap(ipath)
        pixmap_resized = pixmap.scaled(299, 299, QtCore.Qt.KeepAspectRatio)
        self.labelShowImage.setPixmap(pixmap_resized)
        Ui_Form.fpath = ipath
        Ui_Form.fname = fpath[0].split("/")[-1]
    
    def getResult(self):
        dl = DeepLearning(Ui_Form.fpath, Ui_Form.fname)
        result = dl.getClass()
        result = str(result[0])
        if result == "0":
            self.labelResult.setText("Covid-19")
        elif result == "1":
            self.labelResult.setText("Lung Opacity")
        elif result == "2":
            self.labelResult.setText("Normal")
        elif result == "3":
            self.labelResult.setText("Viral Pneumonia")
        
        self.buttonResult.setEnabled(False)
        self.buttonChoose.setEnabled(True)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "predX-ray"))
        self.buttonResult.setText(_translate("Form", "Predict"))
        self.buttonChoose.setText(_translate("Form", "Upload"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
