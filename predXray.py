# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bestGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from dl import DeepLearning

class Ui_Form(object):
    fpath = ""
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
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(470, 300, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.buttonChoose.clicked.connect(self.loadImage)
        self.buttonResult.setEnabled(False)
        self.buttonResult.clicked.connect(self.getResult)
        self.labelResult.setText("Lütfen bir X-ray görüntüsü yükleyin!")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def loadImage(self):
        dlg = QFileDialog()
        fpath = QFileDialog.getOpenFileName(caption="Open File", filter="Image Files (*.png *.jpg *.jpeg)")
        ipath = fpath[0]
        if len(ipath)>0:
            self.buttonResult.setEnabled(True)
            self.buttonChoose.setEnabled(False)
            self.labelResult.setText("Görüntü Başarıyla yüklendi!")

        pixmap = QPixmap(ipath)
        pixmap_resized = pixmap.scaled(299, 299, QtCore.Qt.KeepAspectRatio)
        self.labelShowImage.setPixmap(pixmap_resized)
        Ui_Form.fpath = ipath
    
    def getResult(self):
        self.progressBar.setVisible(True)
        dl = DeepLearning(Ui_Form().fpath)
        result = dl.getClass()
        result = str(result[0])
        self.doAction()
        txt = "Verilen X-ray görüntüsüne göre kişi %92.03 oranında "
        if result == "0":
            self.labelResult.setText(txt+"Covid-19!")
        elif result == "1":
            self.labelResult.setText(txt+"Akciğer Opasitesi!")
        elif result == "2":
            self.labelResult.setText(txt+"Normal!")
        elif result == "3":
            self.labelResult.setText(txt+"Viral Zatürre!")
        
        self.buttonResult.setEnabled(False)
        self.buttonChoose.setEnabled(True)
        self.progressBar.setVisible(False)
    
    def doAction(self):
        for i in range(101):
            time.sleep(0.01)
            self.progressBar.setValue(i)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Covid-19 X-ray"))
        self.buttonResult.setText(_translate("Form", "Sonuç"))
        self.buttonChoose.setText(_translate("Form", "Görüntü Yükle"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
