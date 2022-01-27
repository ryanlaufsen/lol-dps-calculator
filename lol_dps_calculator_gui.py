# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lol-dps-calculator-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from lol_dps_calculator import calculateDPS

# atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps = calculateDPS()

# import threading

# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

# def getData():
#     atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps = calculateDPS()
#     getData.atk_dmg = atk_dmg
#     getData.atk_speed = atk_speed
#     getData.crit_chance = crit_chance
#     getData.crit_multiplier = crit_multiplier
#     getData.average_dps = average_dps

# set_interval(getData, 1)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("LOL DPS Calculator")
        MainWindow.resize(870, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setMinimumSize(QtCore.QSize(546, 0))
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(72)
        self.title.setFont(font)
        self.title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.atk_speed_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(48)
        self.atk_speed_label.setFont(font)
        self.atk_speed_label.setTextFormat(QtCore.Qt.AutoText)
        self.atk_speed_label.setScaledContents(False)
        self.atk_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.atk_speed_label.setWordWrap(False)
        self.atk_speed_label.setObjectName("atk_speed_label")
        self.gridLayout.addWidget(self.atk_speed_label, 1, 1, 1, 1)
        self.atk_speed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.atk_speed.setFont(font)
        self.atk_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.atk_speed.setObjectName("atk_speed")
        self.gridLayout.addWidget(self.atk_speed, 1, 2, 1, 1)
        self.atk_dmg_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(48)
        self.atk_dmg_label.setFont(font)
        self.atk_dmg_label.setTextFormat(QtCore.Qt.AutoText)
        self.atk_dmg_label.setScaledContents(False)
        self.atk_dmg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.atk_dmg_label.setWordWrap(False)
        self.atk_dmg_label.setObjectName("atk_dmg_label")
        self.gridLayout.addWidget(self.atk_dmg_label, 0, 1, 1, 1)
        self.crit_multiplier = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.crit_multiplier.setFont(font)
        self.crit_multiplier.setAlignment(QtCore.Qt.AlignCenter)
        self.crit_multiplier.setObjectName("crit_multiplier")
        self.gridLayout.addWidget(self.crit_multiplier, 3, 2, 1, 1)
        self.atk_dmg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.atk_dmg.setFont(font)
        self.atk_dmg.setAlignment(QtCore.Qt.AlignCenter)
        self.atk_dmg.setObjectName("atk_dmg")
        self.gridLayout.addWidget(self.atk_dmg, 0, 2, 1, 1)
        self.crit_multiplier_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(48)
        self.crit_multiplier_label.setFont(font)
        self.crit_multiplier_label.setTextFormat(QtCore.Qt.AutoText)
        self.crit_multiplier_label.setScaledContents(False)
        self.crit_multiplier_label.setAlignment(QtCore.Qt.AlignCenter)
        self.crit_multiplier_label.setWordWrap(False)
        self.crit_multiplier_label.setObjectName("crit_multiplier_label")
        self.gridLayout.addWidget(self.crit_multiplier_label, 3, 1, 1, 1)
        self.crit_chance_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(48)
        self.crit_chance_label.setFont(font)
        self.crit_chance_label.setTextFormat(QtCore.Qt.AutoText)
        self.crit_chance_label.setScaledContents(False)
        self.crit_chance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.crit_chance_label.setWordWrap(False)
        self.crit_chance_label.setObjectName("crit_chance_label")
        self.gridLayout.addWidget(self.crit_chance_label, 2, 1, 1, 1)
        self.average_dps = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.average_dps.setFont(font)
        self.average_dps.setStyleSheet("color: rgb(0, 85, 255)")
        self.average_dps.setTextFormat(QtCore.Qt.RichText)
        self.average_dps.setAlignment(QtCore.Qt.AlignCenter)
        self.average_dps.setObjectName("average_dps")
        self.gridLayout.addWidget(self.average_dps, 5, 2, 1, 1)
        self.average_dps_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(60)
        self.average_dps_label.setFont(font)
        self.average_dps_label.setTextFormat(QtCore.Qt.AutoText)
        self.average_dps_label.setScaledContents(False)
        self.average_dps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.average_dps_label.setWordWrap(False)
        self.average_dps_label.setObjectName("average_dps_label")
        self.gridLayout.addWidget(self.average_dps_label, 5, 1, 1, 1)
        self.crit_chance = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.crit_chance.setFont(font)
        self.crit_chance.setAlignment(QtCore.Qt.AlignCenter)
        self.crit_chance.setObjectName("crit_chance")
        self.gridLayout.addWidget(self.crit_chance, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("billy")
        font.setPointSize(48)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow, atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("MainWindow", "LOL DPS Calculator"))
        self.atk_speed_label.setText(_translate("MainWindow", "Attack Speed"))
        self.atk_speed.setText(_translate("MainWindow", str(atk_speed)))
        self.atk_dmg_label.setText(_translate("MainWindow", "Attack Damage"))
        self.crit_multiplier.setText(_translate("MainWindow", str(crit_multiplier)))
        self.atk_dmg.setText(_translate("MainWindow", str(atk_dmg)))
        self.crit_multiplier_label.setText(_translate("MainWindow", "Crit Multiplier"))
        self.crit_chance_label.setText(_translate("MainWindow", "Crit Chance"))
        self.average_dps.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">{}</span></p></body></html>".format(str(average_dps))))
        self.average_dps_label.setText(_translate("MainWindow", "Average DPS"))
        self.crit_chance.setText(_translate("MainWindow", str(crit_chance)))
