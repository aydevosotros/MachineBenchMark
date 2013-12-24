import sys
import csv
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
        QtCore.QObject.connect(self.ui.PlotVolumeButton, QtCore.SIGNAL("clicked()"), self.plotVolume)
        self.connect(self.ui.getTrainingButton, QtCore.SIGNAL("clicked()"), self.getTrainingSet)
                
    def file_dialog(self):
        self.ui.editor_window.setText('aaaaaaaaaa')
        
    def getTrainingSet(self):
        # Obtengo las fechas para la descarga
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.symbol = str(self.ui.widget.getSymbolSelected())
        get_historical(self.symbol, self.StartDate.day(), self.StartDate.month(), self.StartDate.year(), self.EndDate.day(), self.EndDate.month(), self.EndDate.year())
        print("Archivo descargado")  
        # Pinto los datos
                
        
    def plotVolume(self):
        ifile = open('../Values/' + self.symbol + '.csv', "rb")
        reader = csv.reader(ifile)
        x = []
        y = []
        rownum = 0
        for row in reader:
            # Save header row.
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    if colnum == 0:
                        print(rownum - 1)
                        x.append(rownum - 1)
                    elif colnum == 5:
                        y.append(int(col))
                    print '%-8s: %s' % (header[colnum], col)
                    colnum += 1                     
            rownum += 1         
        ifile.close()
        
        plotWidget = pg.plot(title="Volume over the time")
        plotWidget.plot(np.asarray(x), np.asarray(y), pen=(1, 3))    




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
