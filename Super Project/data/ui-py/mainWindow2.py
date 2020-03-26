# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormMap(object):
    def setupUi(self, FormMap):
        FormMap.setObjectName("FormMap")
        FormMap.resize(998, 611)
        self.gridLayout_2 = QtWidgets.QGridLayout(FormMap)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Map = QtWidgets.QLabel(FormMap)
        self.Map.setText("")
        self.Map.setAlignment(QtCore.Qt.AlignCenter)
        self.Map.setObjectName("Map")
        self.gridLayout_2.addWidget(self.Map, 2, 0, 1, 4)
        self.TypeMap = QtWidgets.QComboBox(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeMap.sizePolicy().hasHeightForWidth())
        self.TypeMap.setSizePolicy(sizePolicy)
        self.TypeMap.setObjectName("TypeMap")
        self.TypeMap.addItem("")
        self.TypeMap.addItem("")
        self.TypeMap.addItem("")
        self.gridLayout_2.addWidget(self.TypeMap, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_SettingMap = QtWidgets.QPushButton(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_SettingMap.sizePolicy().hasHeightForWidth())
        self.Button_SettingMap.setSizePolicy(sizePolicy)
        self.Button_SettingMap.setObjectName("Button_SettingMap")
        self.horizontalLayout.addWidget(self.Button_SettingMap)
        self.Button_SettingMap_label = QtWidgets.QLabel(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_SettingMap_label.sizePolicy().hasHeightForWidth())
        self.Button_SettingMap_label.setSizePolicy(sizePolicy)
        self.Button_SettingMap_label.setObjectName("Button_SettingMap_label")
        self.horizontalLayout.addWidget(self.Button_SettingMap_label)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 4)
        self.Button_Search = QtWidgets.QPushButton(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Search.sizePolicy().hasHeightForWidth())
        self.Button_Search.setSizePolicy(sizePolicy)
        self.Button_Search.setObjectName("Button_Search")
        self.gridLayout_2.addWidget(self.Button_Search, 0, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.longitude_label = QtWidgets.QLabel(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longitude_label.sizePolicy().hasHeightForWidth())
        self.longitude_label.setSizePolicy(sizePolicy)
        self.longitude_label.setObjectName("longitude_label")
        self.gridLayout.addWidget(self.longitude_label, 0, 3, 1, 1)
        self.latitude = QtWidgets.QDoubleSpinBox(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latitude.sizePolicy().hasHeightForWidth())
        self.latitude.setSizePolicy(sizePolicy)
        self.latitude.setMinimum(-90.0)
        self.latitude.setMaximum(90.0)
        self.latitude.setObjectName("latitude")
        self.gridLayout.addWidget(self.latitude, 0, 2, 1, 1)
        self.adress = QtWidgets.QLineEdit(FormMap)
        self.adress.setObjectName("adress")
        self.gridLayout.addWidget(self.adress, 1, 1, 1, 4)
        self.latitude_label = QtWidgets.QLabel(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latitude_label.sizePolicy().hasHeightForWidth())
        self.latitude_label.setSizePolicy(sizePolicy)
        self.latitude_label.setObjectName("latitude_label")
        self.gridLayout.addWidget(self.latitude_label, 0, 1, 1, 1)
        self.longitude = QtWidgets.QDoubleSpinBox(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longitude.sizePolicy().hasHeightForWidth())
        self.longitude.setSizePolicy(sizePolicy)
        self.longitude.setMinimum(-180.0)
        self.longitude.setMaximum(180.0)
        self.longitude.setObjectName("longitude")
        self.gridLayout.addWidget(self.longitude, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scale = QtWidgets.QSlider(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale.sizePolicy().hasHeightForWidth())
        self.scale.setSizePolicy(sizePolicy)
        self.scale.setMaximum(17)
        self.scale.setOrientation(QtCore.Qt.Horizontal)
        self.scale.setObjectName("scale")
        self.gridLayout.addWidget(self.scale, 2, 1, 1, 4)
        self.scale_label = QtWidgets.QLabel(FormMap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_label.sizePolicy().hasHeightForWidth())
        self.scale_label.setSizePolicy(sizePolicy)
        self.scale_label.setObjectName("scale_label")
        self.gridLayout.addWidget(self.scale_label, 2, 0, 1, 1)
        self.label_adress = QtWidgets.QLabel(FormMap)
        self.label_adress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_adress.setObjectName("label_adress")
        self.gridLayout.addWidget(self.label_adress, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)

        self.retranslateUi(FormMap)
        QtCore.QMetaObject.connectSlotsByName(FormMap)

    def retranslateUi(self, FormMap):
        _translate = QtCore.QCoreApplication.translate
        FormMap.setWindowTitle(_translate("FormMap", "Form"))
        self.TypeMap.setItemText(0, _translate("FormMap", "Схема"))
        self.TypeMap.setItemText(1, _translate("FormMap", "Спутник"))
        self.TypeMap.setItemText(2, _translate("FormMap", "Гибрид"))
        self.Button_SettingMap.setText(_translate("FormMap", "Управление картой"))
        self.Button_SettingMap_label.setText(_translate("FormMap", "(для выхода нажмите Escape)"))
        self.Button_Search.setText(_translate("FormMap", "Найти"))
        self.longitude_label.setText(_translate("FormMap", "Долгота:"))
        self.latitude_label.setText(_translate("FormMap", "Широта:"))
        self.label.setText(_translate("FormMap", "Координаты:"))
        self.scale_label.setText(_translate("FormMap", "Масштаб: 0"))
        self.label_adress.setText(_translate("FormMap", "Адрес:"))

