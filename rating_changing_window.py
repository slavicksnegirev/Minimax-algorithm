# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rating_changing_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from logic import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rating_changing_window(object):
    def setupUi(self, rating_changing_window):
        rating_changing_window.setObjectName("rating_changing")
        rating_changing_window.resize(391, 133)

        self.verticalLayout = QtWidgets.QVBoxLayout(rating_changing_window)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(rating_changing_window)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.comboBox = QtWidgets.QComboBox(rating_changing_window)
        self.comboBox.setObjectName("comboBox")
        node_list = []
        for index in range(len(data_list[int(current_tree_var.get())-1])):
            if data_list[int(current_tree_var.get())-1][index][1]['data'] != ' ':
                node_list.append(str(data_list[int(current_tree_var.get())-1][index][0]))
        self.comboBox.addItems(node_list)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(rating_changing_window)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.lineEdit = QtWidgets.QLineEdit(rating_changing_window)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.buttonBox = QtWidgets.QDialogButtonBox(rating_changing_window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(rating_changing_window)
        self.buttonBox.accepted.connect(rating_changing_window.accept) # type: ignore
        self.buttonBox.rejected.connect(rating_changing_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(rating_changing_window)

    def retranslateUi(self, rating_changing_window):
        _translate = QtCore.QCoreApplication.translate
        rating_changing_window.setWindowTitle(_translate("rating_changing_window", "Изменение оценки листьев"))
        self.label.setText(_translate("rating_changing_window", "Выберите лист для изменения оценки:"))
        self.label_2.setText(_translate("rating_changing_window", "Введите новое значение оценки:"))

    def show_data(self):
        return self.comboBox.currentText(), self.lineEdit.text()

def rating_changing_dialog():
    # global rating_changing_algorithm
    rating_changing_window = QtWidgets.QDialog()
    ui = Ui_rating_changing_window()
    ui.setupUi(rating_changing_window)
    rating_changing_window.show()

    if rating_changing_window.exec():
        if ui.show_data()[1].isdigit():
            trees_dict[current_tree_var.get()].nodes(data=True)[ui.show_data()[0]]['data'] = int(ui.show_data()[1])
            data_list[int(current_tree_var.get())-1][int(ui.show_data()[0])-1][1]['data'] = int(ui.show_data()[1])
            text_output.append(f"Оценка листа {ui.show_data()[0]} изменено на {ui.show_data()[1]}")
        else:
            text_output.append(f"Некорректный ввод")