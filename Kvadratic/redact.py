# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Prog\disckr.ui'
#
# Created: Sun May 26 11:37:44 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 405)
        Form.setMinimumSize(QtCore.QSize(525, 405))
        Form.setMaximumSize(QtCore.QSize(525, 405))
        Form.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border:none;\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(187, 12, 7) ;\n"
"}\n"
"QWidget {\n"
"background-color:rgb(226,226,226)\n"
"}\n"
"\n"
"\n"
"")
        self.Label_x2 = QtGui.QLabel(Form)
        self.Label_x2.setGeometry(QtCore.QRect(160, 70, 61, 31))
        self.Label_x2.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.Label_x2.setObjectName("Label_x2")
        self.Label_x2_2 = QtGui.QLabel(Form)
        self.Label_x2_2.setGeometry(QtCore.QRect(290, 70, 61, 31))
        self.Label_x2_2.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.Label_x2_2.setObjectName("Label_x2_2")
        self.Label_x2_3 = QtGui.QLabel(Form)
        self.Label_x2_3.setGeometry(QtCore.QRect(400, 70, 61, 31))
        self.Label_x2_3.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.Label_x2_3.setObjectName("Label_x2_3")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 0, 371, 51))
        self.label.setStyleSheet("font-size: 20px;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.butt = QtGui.QPushButton(Form)
        self.butt.setGeometry(QtCore.QRect(210, 120, 91, 41))
        self.butt.setStyleSheet("")
        self.butt.setObjectName("butt")
        self.label_resh = QtGui.QLabel(Form)
        self.label_resh.setGeometry(QtCore.QRect(10, 160, 111, 41))
        self.label_resh.setStyleSheet("font-size: 20px;\n"
"color: rgb(187, 12, 7);\n"
"font-weight: bold;\n"
"\n"
"")
        self.label_resh.setText("")
        self.label_resh.setObjectName("label_resh")
        self.uravn_label = QtGui.QLabel(Form)
        self.uravn_label.setGeometry(QtCore.QRect(10, 200, 521, 21))
        self.uravn_label.setStyleSheet("font-size: 20px;\n"
"font-family: molot;\n"
"")
        self.uravn_label.setText("")
        self.uravn_label.setObjectName("uravn_label")
        self.label_disc = QtGui.QLabel(Form)
        self.label_disc.setGeometry(QtCore.QRect(10, 230, 501, 21))
        self.label_disc.setStyleSheet("font-size: 20px;\n"
"color: rgb(187, 12, 7);\n"
"font-weight: bold;")
        self.label_disc.setText("")
        self.label_disc.setObjectName("label_disc")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 511, 21))
        self.label_5.setStyleSheet("font-size: 20px;\n"
"font-family: molot;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_korni = QtGui.QLabel(Form)
        self.label_korni.setGeometry(QtCore.QRect(10, 300, 501, 21))
        self.label_korni.setStyleSheet("font-size: 20px;\n"
"color: rgb(187, 12, 7);\n"
"font-weight: bold;")
        self.label_korni.setText("")
        self.label_korni.setObjectName("label_korni")
        self.label_x1 = QtGui.QLabel(Form)
        self.label_x1.setGeometry(QtCore.QRect(10, 340, 511, 21))
        self.label_x1.setStyleSheet("font-size: 20px;\n"
"font-family: molot;\n"
"")
        self.label_x1.setText("")
        self.label_x1.setObjectName("label_x1")
        self.label_x2 = QtGui.QLabel(Form)
        self.label_x2.setGeometry(QtCore.QRect(10, 380, 511, 21))
        self.label_x2.setStyleSheet("font-size: 20px;\n"
"font-family: molot;\n"
"")
        self.label_x2.setText("")
        self.label_x2.setObjectName("label_x2")
        self.a_in = QtGui.QLineEdit(Form)
        self.a_in.setGeometry(QtCore.QRect(90, 70, 61, 31))
        self.a_in.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.a_in.setText("")
        self.a_in.setObjectName("a_in")
        self.b_in = QtGui.QLineEdit(Form)
        self.b_in.setGeometry(QtCore.QRect(220, 70, 61, 31))
        self.b_in.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.b_in.setObjectName("b_in")
        self.c_in = QtGui.QLineEdit(Form)
        self.c_in.setGeometry(QtCore.QRect(330, 70, 61, 31))
        self.c_in.setStyleSheet("font-size:25px;text-align: right;\n"
"font-family: molot;\n"
"")
        self.c_in.setObjectName("c_in")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_x2.setText(QtGui.QApplication.translate("Form", "x²+", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_x2_2.setText(QtGui.QApplication.translate("Form", "x+", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_x2_3.setText(QtGui.QApplication.translate("Form", "= 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "\"Решение квадратного уравнения\"", None, QtGui.QApplication.UnicodeUTF8))
        self.butt.setText(QtGui.QApplication.translate("Form", "Решить", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

