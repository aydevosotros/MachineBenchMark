import sys
import csv
from DataMining import historicalprices
from DataMining import SymbolsParser
from PyQt4 import QtCore, QtGui
from pruebaUi import Ui_MainWindow
from DataMining.historicalprices import get_historical

import numpy as np
import pyqtgraph as pg

import matplotlib.pyplot as plt
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.setupUi(self.ui.widget)
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.TrainButton, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.PlotVolumeButton, QtCore.SIGNAL("clicked()"), self.plotVolume)
        QtCore.QObject.connect(self.ui.PlotCandlesButton, QtCore.SIGNAL("clicked()"), self.plotCandle)
        QtCore.QObject.connect(self.ui.addToPortfolioButton, QtCore.SIGNAL("clicked()"), self.addToPortfolio)
        QtCore.QObject.connect(self.ui.getLabelButton, QtCore.SIGNAL("clicked()"), self.calculateWinningsLooses)
                
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
                
    def modifyTrainingSet(self):
        self.symbol = str(self.ui.widget.getSymbolSelected())
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        ifile = open('../Values/' + self.symbol + '.csv', "rb")
        reader = csv.reader(ifile)
        rownum = 1
        counter = 0
        openDate = ""
        openValue = 0.0
        closeValue = 0.0
        highValue = 0.0
        lowValue = sys.float_info.max
        volValue = 0
        rowmax = len(list(reader))
        ifile = open('../Values/' + self.symbol + '.csv', "rb")
        reader = csv.reader(ifile)
        if self.ui.comboBox_2.currentText() == 'Day/s':
            print "Partimos por dias"
            ofile = open('../Values/' + self.symbol + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv', "wb")
            writer = csv.writer(ofile)
            for row in reader:
                # Save header row.
                if rownum == 1:
                    header = row
                    writer.writerow(header)
                else:
                    counter += 1
                    colnum = 0
                    for col in row:
                        if counter == self.ui.spinBox.value() or rownum == rowmax:
                            if colnum == 0:
                                openDate = str(col);
                            if colnum == 1:
                                openValue = float(col)
                        if counter == 1:
                            if colnum == 4:
                                closeValue = float(col)
                        if colnum == 2:
                            if float(col) > highValue:
                                highValue = float(col)
                        if colnum == 3:
                            if float(col) < lowValue:
                                lowValue = float(col)
                        if colnum == 5:
                            volValue += int(col)
                        colnum += 1
                    if counter == self.ui.spinBox.value() or rownum == rowmax:
                        counter = 0
                        writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                        highValue = 0.0
                        lowValue = sys.float_info.max     
                        volValue = 0;            
                rownum += 1         
            ifile.close()
            ofile.close()
        elif self.ui.comboBox_2.currentText() == 'Month/s':
            print "Partimos por meses"
            mesActual = "";      
            monthsPerGroup = self.ui.spinBox.value()      
            ofile = open('../Values/' + self.symbol + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv', "wb")
            writer = csv.writer(ofile)
            for row in reader:
                # Save header row.
                if rownum == 1:
                    header = row
                    writer.writerow(header)
                else:
                    counter += 1
                    colnum = 0
                    for col in row:

                        if colnum == 0:
                            if mesActual != "" and mesActual != str(col).split("-")[1]:
                                if monthsPerGroup == 1:
                                    counter = 1
                                    writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                                    highValue = 0.0
                                    lowValue = sys.float_info.max     
                                    volValue = 0
                                    monthsPerGroup = self.ui.spinBox.value()
                                else:
                                    monthsPerGroup -= 1
                                    mesActual = str(col).split("-")[1]
                            else:
                                mesActual = str(col).split("-")[1]
                        if colnum == 0:
                            openDate = str(col)
                        if colnum == 1:
                            openValue = float(col)
                        if counter == 1:
                            if colnum == 0:
                                mesActual = str(col).split("-")[1]
                            if colnum == 4:
                                closeValue = float(col)
                        if colnum == 2:
                            if float(col) > highValue:
                                highValue = float(col)
                        if colnum == 3:
                            if float(col) < lowValue:
                                lowValue = float(col)
                        if colnum == 5:
                            volValue += int(col)
                        colnum += 1
                    if rownum == rowmax:
                        counter = 0
                        writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                        highValue = 0.0
                        lowValue = sys.float_info.max     
                        volValue = 0;            
                rownum += 1         
            ifile.close()
            ofile.close()
        elif self.ui.comboBox_2.currentText() == 'Year/s':
            print "Partimos por anyos"
            anyoActual = "";      
            yearsPerGroup = self.ui.spinBox.value()      
            ofile = open('../Values/' + self.symbol + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv', "wb")
            writer = csv.writer(ofile)
            for row in reader:
                # Save header row.
                if rownum == 1:
                    header = row
                    writer.writerow(header)
                else:
                    counter += 1
                    colnum = 0
                    for col in row:

                        if colnum == 0:
                            if anyoActual != "" and anyoActual != str(col).split("-")[2]:
                                if yearsPerGroup == 1:
                                    counter = 1
                                    writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                                    highValue = 0.0
                                    lowValue = sys.float_info.max     
                                    volValue = 0
                                    yearsPerGroup = self.ui.spinBox.value()
                                else:
                                    yearsPerGroup -= 1
                                    anyoActual = str(col).split("-")[2]
                            else:
                                anyoActual = str(col).split("-")[2]
                        if colnum == 0:
                            openDate = str(col)
                        if colnum == 1:
                            openValue = float(col)
                        if counter == 1:
                            if colnum == 0:
                                anyoActual = str(col).split("-")[2]
                            if colnum == 4:
                                closeValue = float(col)
                        if colnum == 2:
                            if float(col) > highValue:
                                highValue = float(col)
                        if colnum == 3:
                            if float(col) < lowValue:
                                lowValue = float(col)
                        if colnum == 5:
                            volValue += int(col)
                        colnum += 1
                    if rownum == rowmax:
                        counter = 0
                        writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                        highValue = 0.0
                        lowValue = sys.float_info.max     
                        volValue = 0;            
                rownum += 1         
            ifile.close()
            ofile.close()
    
    def plotVolume(self):
        self.symbol = str(self.ui.widget.getSymbolSelected())
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
                        y.insert(0, int(col))
                    print '%-8s: %s' % (header[colnum], col)
                    colnum += 1                     
            rownum += 1         
        ifile.close()
        
        plotWidget = pg.plot(title="Volume over the time")
        plotWidget.plot(np.asarray(x), np.asarray(y), pen=(1, 3))    

    def plotCandle(self):
        # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.symbol = str(self.ui.widget.getSymbolSelected())
        date1 = ( self.StartDate.year(), self.StartDate.month(), self.StartDate.day())
        date2 = ( self.EndDate.year(), self.EndDate.month(), self.EndDate.day())
        
        
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays    = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12
        
        quotes = quotes_historical_yahoo(self.symbol, date1, date2)
        
        if len(quotes) == 0:
            raise SystemExit
        
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        #ax.xaxis.set_minor_formatter(dayFormatter)
        
        #plot_day_summary(ax, quotes, ticksize=3)
        candlestick(ax, quotes, width=0.6)
        
        ax.xaxis_date()
        ax.autoscale_view()
        plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        
        plt.show()

    def addToPortfolio(self):
        self.getTrainingSet()
        self.modifyTrainingSet()
        self.symbol = str(self.ui.widget.getSymbolSelected())
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.ui.listWidget.addItem(self.symbol + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv')

    def calculateWinningsLooses(self):
        print "Empezamos a calcular ganancias/perdidas"
        for x in range(0, self.ui.listWidget.__len__()):
            ifile = open('../Values/' + str(self.ui.listWidget.item(x).text()), "rb")
            reader = csv.reader(ifile)
            ofile = open('../Values/' + str(self.ui.listWidget.item(x).text()) + "-labeled" '.csv', "wb")
            writer = csv.writer(ofile)
            openValue = 0.0
            closeValue = 0.0
            rownum = 0
            for row in reader:
                if rownum != 0:
                    colnum = 0
                    for col in row:
                        if colnum == 1:
                            openValue = float(col)
                        if colnum == 4:
                            closeValue = float(col)
                        colnum += 1
                    if openValue - closeValue > 0:
                        writer.writerow(["+1"])  
                    if openValue - closeValue < 0:
                        writer.writerow(["-1"])  
                rownum += 1
            ifile.close()
            ofile.close()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
