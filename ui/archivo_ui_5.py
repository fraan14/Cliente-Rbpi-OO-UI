# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppal_ui_5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(356, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("comun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 10, 340, 361))
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 319, 449))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_1.setEnabled(True)
        self.widget_1.setMinimumSize(QtCore.QSize(0, 81))
        self.widget_1.setMaximumSize(QtCore.QSize(16777215, 81))
        self.widget_1.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.widget_1.setObjectName("widget_1")
        self.label_10 = QtWidgets.QLabel(self.widget_1)
        self.label_10.setGeometry(QtCore.QRect(70, 19, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_1)
        self.label_11.setGeometry(QtCore.QRect(70, 42, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_1)
        self.label_12.setGeometry(QtCore.QRect(10, 16, 51, 51))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("usuario_persona.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.widget_1)
        self.pushButton.setGeometry(QtCore.QRect(213, 20, 35, 35))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setToolTip("")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-style: outset;")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_1)
        self.pushButton_6.setGeometry(QtCore.QRect(255, 20, 35, 35))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setToolTip("")
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("border-style: outset;")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("saliente rojo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.widget_1)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 81))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 81))
        self.widget_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.widget_2.setObjectName("widget_2")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(70, 19, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(70, 42, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setGeometry(QtCore.QRect(10, 16, 51, 51))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("usuario_pc.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 20, 35, 35))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("border-style: outset;")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_3.setEnabled(True)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 81))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 81))
        self.widget_3.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.widget_3.setObjectName("widget_3")
        self.label_22 = QtWidgets.QLabel(self.widget_3)
        self.label_22.setGeometry(QtCore.QRect(70, 19, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_3)
        self.label_23.setGeometry(QtCore.QRect(70, 42, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_3)
        self.label_24.setGeometry(QtCore.QRect(10, 16, 51, 51))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("usuario_persona.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 20, 35, 35))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("border-style: outset;")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_4.setEnabled(True)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 81))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 81))
        self.widget_4.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.widget_4.setObjectName("widget_4")
        self.label_26 = QtWidgets.QLabel(self.widget_4)
        self.label_26.setGeometry(QtCore.QRect(70, 19, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.widget_4)
        self.label_27.setGeometry(QtCore.QRect(70, 42, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.widget_4)
        self.label_28.setGeometry(QtCore.QRect(10, 16, 51, 51))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("usuario_persona.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 20, 35, 35))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("border-style: outset;")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_5.setEnabled(True)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 81))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 81))
        self.widget_5.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.widget_5.setObjectName("widget_5")
        self.label_30 = QtWidgets.QLabel(self.widget_5)
        self.label_30.setGeometry(QtCore.QRect(70, 19, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.widget_5)
        self.label_31.setGeometry(QtCore.QRect(70, 42, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.widget_5)
        self.label_32.setGeometry(QtCore.QRect(10, 16, 51, 51))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("usuario_persona.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 20, 35, 35))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setToolTip("")
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("border-style: outset;")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telefonia IP"))
        self.label_10.setText(_translate("MainWindow", "CC Rodriguez Martin"))
        self.label_11.setText(_translate("MainWindow", "SIAG"))
        self.label_14.setText(_translate("MainWindow", "CC Rodriguez Martin"))
        self.label_15.setText(_translate("MainWindow", "SIAG"))
        self.label_22.setText(_translate("MainWindow", "CC Rodriguez Martin"))
        self.label_23.setText(_translate("MainWindow", "SIAG"))
        self.label_26.setText(_translate("MainWindow", "CC Rodriguez Martin"))
        self.label_27.setText(_translate("MainWindow", "SIAG"))
        self.label_30.setText(_translate("MainWindow", "CC Rodriguez Martin"))
        self.label_31.setText(_translate("MainWindow", "SIAG"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())