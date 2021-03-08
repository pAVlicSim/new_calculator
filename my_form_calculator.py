# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 332)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_result = QtWidgets.QTextEdit(Form)
        self.textEdit_result.setObjectName("textEdit_result")
        self.verticalLayout.addWidget(self.textEdit_result)
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setMaxLength(10000)
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_numbers = QtWidgets.QTabWidget(Form)
        self.tabWidget_numbers.setObjectName("tabWidget_numbers")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_clear_one = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_clear_one.setObjectName("pushButton_clear_one")
        self.gridLayout.addWidget(self.pushButton_clear_one, 0, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_clear_all = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_clear_all.setObjectName("pushButton_clear_all")
        self.gridLayout.addWidget(self.pushButton_clear_all, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_cursor_right = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_cursor_right.setObjectName("pushButton_cursor_right")
        self.gridLayout.addWidget(self.pushButton_cursor_right, 0, 2, 1, 1)
        self.pushButton_comma = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_comma.setObjectName("pushButton_comma")
        self.gridLayout.addWidget(self.pushButton_comma, 2, 3, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_cursor_left = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_cursor_left.setAutoRepeat(True)
        self.pushButton_cursor_left.setObjectName("pushButton_cursor_left")
        self.gridLayout.addWidget(self.pushButton_cursor_left, 0, 1, 1, 1)
        self.pushButton_plus_minus = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_plus_minus.setObjectName("pushButton_plus_minus")
        self.gridLayout.addWidget(self.pushButton_plus_minus, 1, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 3, 1, 1)
        self.toolButton_ordinary_numbers = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.toolButton_ordinary_numbers.setObjectName("toolButton_ordinary_numbers")
        self.gridLayout.addWidget(self.toolButton_ordinary_numbers, 1, 4, 1, 1)
        self.toolButton_superscript_numbers = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.toolButton_superscript_numbers.setObjectName("toolButton_superscript_numbers")
        self.gridLayout.addWidget(self.toolButton_superscript_numbers, 2, 4, 1, 1)
        self.toolButton_subscript_numbers = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.toolButton_subscript_numbers.setObjectName("toolButton_subscript_numbers")
        self.gridLayout.addWidget(self.toolButton_subscript_numbers, 3, 4, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.tabWidget_numbers.addTab(self.tabWidgetPage1, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_numbers)
        self.tabWidget_actions = QtWidgets.QTabWidget(Form)
        self.tabWidget_actions.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_actions.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_actions.setUsesScrollButtons(False)
        self.tabWidget_actions.setTabBarAutoHide(True)
        self.tabWidget_actions.setObjectName("tabWidget_actions")
        self.tab_aritmetic = QtWidgets.QWidget()
        self.tab_aritmetic.setObjectName("tab_aritmetic")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_aritmetic)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_plus = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout_2.addWidget(self.pushButton_plus, 0, 0, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout_2.addWidget(self.pushButton_percent, 0, 2, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout_2.addWidget(self.pushButton_divide, 0, 1, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout_2.addWidget(self.pushButton_minus, 2, 0, 1, 1)
        self.pushButton_root = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_root.setObjectName("pushButton_root")
        self.gridLayout_2.addWidget(self.pushButton_root, 3, 1, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout_2.addWidget(self.pushButton_multiply, 2, 1, 1, 1)
        self.pushButton_result = QtWidgets.QPushButton(self.tab_aritmetic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_result.sizePolicy().hasHeightForWidth())
        self.pushButton_result.setSizePolicy(sizePolicy)
        self.pushButton_result.setObjectName("pushButton_result")
        self.gridLayout_2.addWidget(self.pushButton_result, 3, 2, 1, 1)
        self.pushButton_degree = QtWidgets.QPushButton(self.tab_aritmetic)
        self.pushButton_degree.setObjectName("pushButton_degree")
        self.gridLayout_2.addWidget(self.pushButton_degree, 3, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.tabWidget_actions.addTab(self.tab_aritmetic, "")
        self.tab_inginiring = QtWidgets.QWidget()
        self.tab_inginiring.setObjectName("tab_inginiring")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_inginiring)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        self.tabWidget_actions.addTab(self.tab_inginiring, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_actions)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.tabWidget_numbers.setCurrentIndex(0)
        self.tabWidget_actions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Калькулятор"))
        self.lineEdit_1.setPlaceholderText(_translate("Form", "0"))
        self.pushButton_clear_one.setText(_translate("Form", "⌫"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_clear_all.setText(_translate("Form", "CA"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_cursor_right.setText(_translate("Form", "⮞"))
        self.pushButton_comma.setText(_translate("Form", ","))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_cursor_left.setText(_translate("Form", "⮜"))
        self.pushButton_plus_minus.setText(_translate("Form", "±"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.toolButton_ordinary_numbers.setText(_translate("Form", "n"))
        self.toolButton_superscript_numbers.setText(_translate("Form", "ⁿ"))
        self.toolButton_subscript_numbers.setText(_translate("Form", "ₙ"))
        self.tabWidget_numbers.setTabText(self.tabWidget_numbers.indexOf(self.tabWidgetPage1), _translate("Form", "Цифры"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_divide.setText(_translate("Form", "÷"))
        self.pushButton_minus.setText(_translate("Form", "−"))
        self.pushButton_root.setText(_translate("Form", "ⁿ√x"))
        self.pushButton_multiply.setText(_translate("Form", "×"))
        self.pushButton_result.setText(_translate("Form", "="))
        self.pushButton_degree.setText(_translate("Form", "xⁿ"))
        self.tabWidget_actions.setTabText(self.tabWidget_actions.indexOf(self.tab_aritmetic), _translate("Form", "Арифметика"))
        self.tabWidget_actions.setTabText(self.tabWidget_actions.indexOf(self.tab_inginiring), _translate("Form", "Инженерный"))
