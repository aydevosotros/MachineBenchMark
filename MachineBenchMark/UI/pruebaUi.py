# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prueba1.ui'
#
# Created: Mon Jan 27 19:24:38 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 524)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 10, 791, 481))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 30, 291, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.startsDate = QtGui.QDateEdit(self.groupBox_2)
        self.startsDate.setGeometry(QtCore.QRect(130, 50, 110, 27))
        self.startsDate.setDate(QtCore.QDate(2010, 10, 1))
        self.startsDate.setObjectName(_fromUtf8("startsDate"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.endDate = QtGui.QDateEdit(self.groupBox_2)
        self.endDate.setGeometry(QtCore.QRect(130, 90, 110, 27))
        self.endDate.setDate(QtCore.QDate(2013, 12, 1))
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.widget = Ui_SymbolSearchWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(0, 140, 281, 191))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 30, 371, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.PlotVolumeButton = QtGui.QPushButton(self.groupBox_3)
        self.PlotVolumeButton.setGeometry(QtCore.QRect(30, 30, 191, 27))
        self.PlotVolumeButton.setObjectName(_fromUtf8("PlotVolumeButton"))
        self.PlotCandlesButton = QtGui.QPushButton(self.groupBox_3)
        self.PlotCandlesButton.setGeometry(QtCore.QRect(30, 70, 191, 27))
        self.PlotCandlesButton.setObjectName(_fromUtf8("PlotCandlesButton"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 210, 371, 131))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox.setGeometry(QtCore.QRect(30, 60, 60, 27))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 60, 78, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.addToPortfolioButton = QtGui.QPushButton(self.tab_2)
        self.addToPortfolioButton.setGeometry(QtCore.QRect(390, 380, 131, 27))
        self.addToPortfolioButton.setObjectName(_fromUtf8("addToPortfolioButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.listWidget = QtGui.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.getLabelButton = QtGui.QPushButton(self.tab_3)
        self.getLabelButton.setGeometry(QtCore.QRect(70, 350, 211, 27))
        self.getLabelButton.setObjectName(_fromUtf8("getLabelButton"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(370, 32, 371, 261))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_4.setGeometry(QtCore.QRect(80, 100, 150, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 40, 150, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 70, 150, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_1 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_1.setGeometry(QtCore.QRect(80, 10, 150, 22))
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_5.setGeometry(QtCore.QRect(80, 130, 150, 22))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_6.setGeometry(QtCore.QRect(80, 160, 150, 22))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setGeometry(QtCore.QRect(80, 220, 97, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(370, 300, 371, 131))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_6)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 60, 60, 27))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 60, 78, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(410, 30, 331, 361))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(60, 110, 231, 151))
        self.groupBox_8.setTitle(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.splitter = QtGui.QSplitter(self.groupBox_8)
        self.splitter.setGeometry(QtCore.QRect(10, 40, 201, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.splitter)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.comboBox_5 = QtGui.QComboBox(self.splitter)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 100, 231, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.TrainButton = QtGui.QPushButton(self.groupBox)
        self.TrainButton.setGeometry(QtCore.QRect(120, 320, 111, 27))
        self.TrainButton.setObjectName(_fromUtf8("TrainButton"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 30, 351, 391))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.labeledFilesWidget = QtGui.QListWidget(self.groupBox_7)
        self.labeledFilesWidget.setGeometry(QtCore.QRect(70, 40, 256, 192))
        self.labeledFilesWidget.setObjectName(_fromUtf8("labeledFilesWidget"))
        self.crossValidationPercent = QtGui.QSpinBox(self.groupBox_7)
        self.crossValidationPercent.setGeometry(QtCore.QRect(110, 260, 60, 27))
        self.crossValidationPercent.setMinimum(0)
        self.crossValidationPercent.setMaximum(100)
        self.crossValidationPercent.setProperty("value", 60)
        self.crossValidationPercent.setObjectName(_fromUtf8("crossValidationPercent"))
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(200, 260, 123, 27))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.crossValidationButton = QtGui.QPushButton(self.groupBox_7)
        self.crossValidationButton.setGeometry(QtCore.QRect(150, 320, 98, 27))
        self.crossValidationButton.setObjectName(_fromUtf8("crossValidationButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.comboBox_4 = QtGui.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(90, 70, 231, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.widget_2 = Ui_SymbolSearchWidget(self.tab_4)
        self.widget_2.setGeometry(QtCore.QRect(70, 190, 281, 191))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_4)
        self.listWidget_2.setGeometry(QtCore.QRect(470, 100, 256, 192))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(60, 40, 231, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 181, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(470, 60, 151, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton = QtGui.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(500, 340, 201, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 56, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Machine Learning BenchMarks", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Training Set Parameters", None))
        self.label_3.setText(_translate("MainWindow", "Starts at:", None))
        self.label_4.setText(_translate("MainWindow", "Ends at:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Options", None))
        self.PlotVolumeButton.setText(_translate("MainWindow", "Plot Volume", None))
        self.PlotCandlesButton.setText(_translate("MainWindow", "Plot Candles", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Group Training Set by", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Day/s", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Month/s", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Year/s", None))
        self.addToPortfolioButton.setText(_translate("MainWindow", "Add to Portfolio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Training Set", None))
        self.getLabelButton.setText(_translate("MainWindow", "Get Labels and add to CV", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Values", None))
        self.checkBox_4.setText(_translate("MainWindow", "Lowest value", None))
        self.checkBox_2.setText(_translate("MainWindow", "Close value", None))
        self.checkBox_3.setText(_translate("MainWindow", "Highest value", None))
        self.checkBox_1.setText(_translate("MainWindow", "Open value", None))
        self.checkBox_5.setText(_translate("MainWindow", "Volume", None))
        self.checkBox_6.setText(_translate("MainWindow", "Gain", None))
        self.checkBox.setText(_translate("MainWindow", "Scale", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Group by", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Day/s", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Month/s", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Year/s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Portfolio", None))
        self.groupBox.setTitle(_translate("MainWindow", "Machine parameters", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Soft", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Hard", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Logistic Regression", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Neural Network", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "SVM", None))
        self.TrainButton.setText(_translate("MainWindow", "Train and test", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Cross Validation", None))
        self.label_5.setText(_translate("MainWindow", "Training %", None))
        self.crossValidationButton.setText(_translate("MainWindow", "Create CV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Machine settings", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Logistic Regression", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Neural Network", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "SVM", None))
        self.label.setText(_translate("MainWindow", "1 - Choose the machine", None))
        self.label_6.setText(_translate("MainWindow", "2 - Choose the index", None))
        self.label_7.setText(_translate("MainWindow", "3 - Choose the theta", None))
        self.pushButton.setText(_translate("MainWindow", "Predict the index of today", None))
        self.pushButton_2.setText(_translate("MainWindow", "Load Thetas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Predict", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))

from SymbolSearchWidget import Ui_SymbolSearchWidget
