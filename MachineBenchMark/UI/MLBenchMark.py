import sys
from DataMining import historicalprices
from DataMining import SymbolsParser
from PyQt4 import QtCore, QtGui
from pruebaUi import Ui_MainWindow
from DataMining.historicalprices import get_historical

import numpy as np
import pyqtgraph as pg

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.setupUi(self.ui.widget)
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.TrainButton, QtCore.SIGNAL("clicked()"), self.file_dialog)
        self.connect(self.ui.getTrainingButton, QtCore.SIGNAL("clicked()"), self.getTrainingSet)
                
    def file_dialog(self):
        self.ui.editor_window.setText('aaaaaaaaaa')
        
    def getTrainingSet(self):
        # Obtengo las fechas para la descarga
        StartDate = self.ui.startsDate.date()
        EndDate = self.ui.endDate.date()
        symbol = str(self.ui.widget.getSymbolSelected())
        get_historical(symbol, StartDate.day(), StartDate.month(), StartDate.year(), EndDate.day(), EndDate.month(), EndDate.year())
        print("Archivo descargado")  
        # Pinto los datos
        x = np.arange(1000)
        y = np.random.normal(size=(3, 1000))
        plotWidget = pg.plot(title="Three plot curves")
        for i in range(3):
            plotWidget.plot(x, y[i], pen=(i,3))       



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())