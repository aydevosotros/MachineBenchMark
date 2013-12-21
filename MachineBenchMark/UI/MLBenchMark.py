import sys
from DataMining import historicalprices
from PyQt4 import QtCore, QtGui
from pruebaUi import Ui_MainWindow
from DataMining.historicalprices import get_historical

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.TrainButton, QtCore.SIGNAL("clicked()"), self.file_dialog)
        self.connect(self.ui.getTrainingButton, QtCore.SIGNAL("clicked()"), self.getTrainingSet)
        
    def file_dialog(self):
        self.ui.editor_window.setText('aaaaaaaaaa')
        
    def getTrainingSet(self):
        # Obtengo las fechas para la descarga
        StartDate = self.ui.startsDate.date()
        EndDate = self.ui.endDate.date()
        get_historical('GOOG', StartDate.day(), StartDate.month(), StartDate.year(), EndDate.day(), EndDate.month(), EndDate.year())
        print("Archivo descargado") 
        
        print(StartDate.day())   
        print(StartDate.month())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())