# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prueba1.ui'
#
# Created: Tue Dec 24 09:26:24 2013
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.TrainButton = QtGui.QPushButton(self.centralwidget)
        self.TrainButton.setGeometry(QtCore.QRect(110, 510, 98, 27))
        self.TrainButton.setObjectName(_fromUtf8("TrainButton"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 791, 481))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 411))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 231, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 150, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 190, 231, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 234, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.splitter)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 30, 291, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.startsDate = QtGui.QDateEdit(self.groupBox_2)
        self.startsDate.setGeometry(QtCore.QRect(130, 50, 110, 27))
        self.startsDate.setObjectName(_fromUtf8("startsDate"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.endDate = QtGui.QDateEdit(self.groupBox_2)
        self.endDate.setGeometry(QtCore.QRect(130, 90, 110, 27))
        self.endDate.setDate(QtCore.QDate(2012, 1, 1))
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.getTrainingButton = QtGui.QPushButton(self.groupBox_2)
        self.getTrainingButton.setGeometry(QtCore.QRect(70, 350, 131, 27))
        self.getTrainingButton.setObjectName(_fromUtf8("getTrainingButton"))
        self.widget = Ui_SymbolSearchWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(0, 140, 281, 191))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 30, 371, 321))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.PlotVolumeButton = QtGui.QPushButton(self.groupBox_3)
        self.PlotVolumeButton.setGeometry(QtCore.QRect(67, 30, 191, 27))
        self.PlotVolumeButton.setObjectName(_fromUtf8("PlotVolumeButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.graphicsView = PlotWidget(self.tab_3)
        self.graphicsView.setGeometry(QtCore.QRect(325, 31, 431, 391))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuML_BenchMark = QtGui.QMenu(self.menubar)
        self.menuML_BenchMark.setObjectName(_fromUtf8("menuML_BenchMark"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuML_BenchMark.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Machine Learning BenchMark", None))
        self.TrainButton.setText(_translate("MainWindow", "Train", None))
        self.groupBox.setTitle(_translate("MainWindow", "Machine parameters", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Linear Regression", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Logistic Regresion", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Neural Network", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "SVM", None))
        self.label.setText(_translate("MainWindow", "Training Set", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.label_2.setText(_translate("MainWindow", "Regularization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Machine settings", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Training Set Parameters", None))
        self.label_3.setText(_translate("MainWindow", "Starts at:", None))
        self.label_4.setText(_translate("MainWindow", "Ends at:", None))
        self.getTrainingButton.setText(_translate("MainWindow", "Get Training Set", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Options", None))
        self.PlotVolumeButton.setText(_translate("MainWindow", "Plot Volume", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Training Set", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Portfolio", None))
        self.menuML_BenchMark.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))

from pyqtgraph import PlotWidget
from SymbolSearchWidget import Ui_SymbolSearchWidget
