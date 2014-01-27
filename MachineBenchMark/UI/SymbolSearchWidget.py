# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SymbolSearchWidget.ui'
#
# Created: Sun Dec 22 13:41:01 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from DataMining import SymbolsParser

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

class Ui_SymbolSearchWidget(QtGui.QWidget):
    def setupUi(self, SymbolSearchWidget):
        SymbolSearchWidget.setObjectName(_fromUtf8("SymbolSearchWidget"))
        SymbolSearchWidget.resize(281, 191)
        self.listView = QtGui.QListView(SymbolSearchWidget)
        self.listView.setGeometry(QtCore.QRect(10, 50, 261, 131))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.queryBox = QtGui.QLineEdit(SymbolSearchWidget)
        self.queryBox.setGeometry(QtCore.QRect(70, 10, 191, 27))
        self.queryBox.setObjectName(_fromUtf8("queryBox"))
        self.label = QtGui.QLabel(SymbolSearchWidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(SymbolSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(SymbolSearchWidget)
        
        # Initialize some parameters
        self.symbolSelected = ""
        
        # Conecting signals
        QtCore.QObject.connect(self.queryBox, QtCore.SIGNAL("textChanged(QString)"), self.queryChanged)
        self.model = QtGui.QStandardItemModel()
        self.listView.clicked.connect(self.itemSelected)

    def retranslateUi(self, SymbolSearchWidget):
        SymbolSearchWidget.setWindowTitle(_translate("SymbolSearchWidget", "Form", None))
        self.label.setText(_translate("SymbolSearchWidget", "Query:", None))
        
    def queryChanged(self, text):
#         QtCore.QObject.disconnect(self.model, QtCore.SIGNAL("itemChanged(QStandardItem)"))
        self.model.clear();
        elements = SymbolsParser.getSymbols(str(text))
        for ele in elements:
            item = QtGui.QStandardItem(ele['symbol'] + " - " + ele['name'])
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        
    def itemSelected(self, item):
        self.symbolSelected = self.model.item(item.row(), column=0).text().split(" - ")[0]
        
        
    def getSymbolSelected(self):
        return self.symbolSelected

