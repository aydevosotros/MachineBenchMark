from PyQt4 import QtCore, QtGui
import csv
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick
import os
import sys

from DataMining.historicalprices import get_historical
import matplotlib.pyplot as plt
import numpy as np
from pruebaUi import Ui_MainWindow
import pyqtgraph as pg

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.setupUi(self.ui.widget)
        self.ui.widget_2.setupUi(self.ui.widget_2)
        self.changeMachineParameters()
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.PlotVolumeButton, QtCore.SIGNAL("clicked()"), self.plotVolume)
        QtCore.QObject.connect(self.ui.PlotCandlesButton, QtCore.SIGNAL("clicked()"), self.plotCandle)
        QtCore.QObject.connect(self.ui.addToPortfolioButton, QtCore.SIGNAL("clicked()"), self.addToPortfolio)
        QtCore.QObject.connect(self.ui.getLabelButton, QtCore.SIGNAL("clicked()"), self.calculateWinningsLooses)
        QtCore.QObject.connect(self.ui.crossValidationButton, QtCore.SIGNAL("clicked()"), self.createCrossFiles)
        QtCore.QObject.connect(self.ui.TrainButton, QtCore.SIGNAL("clicked()"), self.callTrainingProgram)
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.changeMachineParameters)
        QtCore.QObject.connect(self.ui.comboBox_6, QtCore.SIGNAL("currentIndexChanged(QString)"), self.changeMachineParameters)
        QtCore.QObject.connect(self.ui.comboBox_7, QtCore.SIGNAL("currentIndexChanged(QString)"), self.changeMachineParameters)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.loadThetaValues)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.predictTodayValue)
        QtCore.QObject.connect(self.ui.checkBox_1, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_2, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_3, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_4, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_5, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_6, QtCore.SIGNAL("clicked()"), self.hideOptions)

        QtCore.QObject.connect(self.ui.checkBox_7, QtCore.SIGNAL("clicked()"), self.hideOptions)
        QtCore.QObject.connect(self.ui.checkBox_8, QtCore.SIGNAL("clicked()"), self.hideOptions)

    def hideOptions(self):
        if self.ui.checkBox_7.isChecked():
            self.ui.groupBox_2.hide()
        else:
            self.ui.groupBox_2.show()
            
        count = 0
        if self.ui.checkBox_1.isChecked():
            count += 1
        if self.ui.checkBox_2.isChecked():
            count += 1
        if self.ui.checkBox_3.isChecked():
            count += 1
        if self.ui.checkBox_4.isChecked():
            count += 1
        if self.ui.checkBox_5.isChecked():
            count += 1
        if self.ui.checkBox_6.isChecked():
            count += 1
            
        if self.ui.checkBox_8.isChecked() or count == 1:
            self.ui.groupBox_6.show()
        else:
            self.ui.groupBox_6.hide()
            self.ui.comboBox_3.setCurrentIndex(0)
            self.ui.spinBox_2.setValue(5)

    def changeMachineParameters(self):
        if self.ui.comboBox.currentText() == "Lineal Regression":
            self.ui.label_2.setText("By the:")
            self.ui.doubleSpinBox.hide()
            self.ui.comboBox_5.hide()
            self.ui.comboBox_6.show()
            self.ui.splitter_3.hide()
            self.ui.splitter_4.hide()
            self.ui.comboBox_7.hide()

            if self.ui.comboBox_6.currentText() == "Normal":
                self.ui.splitter_2.hide()
            else:
                self.ui.label_8.setText("Regularization")
                self.ui.splitter_2.show()
                self.ui.doubleSpinBox_2.show()
                self.ui.comboBox_7.hide()
        elif self.ui.comboBox.currentText() == "Logistic Regression":
            self.ui.label_2.setText("Regularization")
            self.ui.doubleSpinBox.show()
            self.ui.comboBox_5.hide()
            self.ui.comboBox_6.hide()
            self.ui.splitter_2.hide()
            self.ui.splitter_3.hide()
            self.ui.comboBox_7.hide()
            self.ui.splitter_4.show()
            self.ui.label_10.setText("Threshold")
            self.ui.doubleSpinBox_4.setValue(0.5)


        elif self.ui.comboBox.currentText() == "Neural Network":
            self.ui.label_2.setText("Regularization")
            self.ui.doubleSpinBox.show()
            self.ui.comboBox_5.hide()
            self.ui.comboBox_6.hide()
            self.ui.label_8.setText("Alpha")
            self.ui.splitter_2.show()
            self.ui.doubleSpinBox_2.show()
            self.ui.comboBox_7.hide()
            self.ui.splitter_4.show()
            self.ui.label_10.setText("Threshold")
            self.ui.doubleSpinBox_4.setValue(0.5)
            self.ui.label_9.setText("Iterations")
            self.ui.splitter_3.show()
            self.ui.comboBox_7.hide()

        elif self.ui.comboBox.currentText() == "SVM":
            self.ui.label_2.setText("Margin")
            self.ui.doubleSpinBox.hide()
            self.ui.comboBox_5.show()
            self.ui.comboBox_6.hide()
            self.ui.splitter_2.show()
            self.ui.splitter_3.hide()
            self.ui.doubleSpinBox_2.hide()
            self.ui.label_8.setText("Kernel")
            self.ui.comboBox_7.show()
            self.ui.splitter_4.show()
            if self.ui.comboBox_7.currentText() == "Polynomial":
                self.ui.label_9.setText("Q")
                self.ui.splitter_3.show()
            elif self.ui.comboBox_7.currentText() == "RBF":
                self.ui.label_9.setText("Sigma")
                self.ui.splitter_3.show()            
            self.ui.label_10.setText("Threshold")
            self.ui.doubleSpinBox_4.setValue(0.0)

    def getTrainingSet(self):
        # Obtengo las fechas para la descarga
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.symbol = str(self.ui.widget.getSymbolSelected())
        if self.symbol == "":
            self.statusBar().showMessage('ERROR: You cannot add to portfolio something without selecting an index')
        else:
            get_historical(self.symbol, self.StartDate.day(), self.StartDate.month(), self.StartDate.year(), self.EndDate.day(), self.EndDate.month(), self.EndDate.year())
            print("Archivo descargado")
            self.statusBar().showMessage('Index added to portfolio successfully')
                
    def modifyTrainingSet(self):
        if self.ui.checkBox_7.isChecked():
            self.trainingFile = 'rap2_training'
        else:
            self.trainingFile = str(self.ui.widget.getSymbolSelected())
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        if self.ui.checkBox_7.isChecked():
            ifile = open('../Values/rap2_training.csv', "rb")
        else:
            ifile = open('../Values/' + self.trainingFile + '.csv', "rb")
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
        if self.ui.checkBox_7.isChecked():
            ifile = open('../Values/rap2_training.csv', "rb")
        else:
            ifile = open('../Values/' + self.trainingFile + '.csv', "rb")
        reader = csv.reader(ifile)
        if self.ui.comboBox_2.currentText() == 'Minute/s':
            if self.ui.checkBox_7.isChecked():
                ofile = open('../Values/' + 'rap2_training' + '-' + str(self.ui.spinBox.value()) + 'min' + '.csv', "wb")
            else:
                ofile = open('../Values/' + self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'min' + '.csv', "wb")
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
                        if counter == (self.ui.spinBox.value()/5) or rownum == rowmax:
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
                            volValue += float(col)
                        colnum += 1
                    if counter == (self.ui.spinBox.value()/5) or rownum == rowmax:
                        counter = 0
                        writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                        highValue = 0.0
                        lowValue = sys.float_info.max     
                        volValue = 0;            
                rownum += 1         
            ifile.close()
            ofile.close()
        elif self.ui.comboBox_2.currentText() == 'Hour/s':
            horaActual = "";      
            hoursPerGroup = self.ui.spinBox.value()
            if self.ui.checkBox_7.isChecked():
                ofile = open('../Values/' + 'rap2_training' + '-' + str(self.ui.spinBox.value()) + 'h' + '.csv', "wb")
            else:   
                ofile = open('../Values/' + self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'h' + '.csv', "wb")
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
                            if horaActual != "" and horaActual != str(col).split("-")[3]:
                                if hoursPerGroup == 1:
                                    counter = 1
                                    writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                                    highValue = 0.0
                                    lowValue = sys.float_info.max     
                                    volValue = 0
                                    hoursPerGroup = self.ui.spinBox.value()
                                else:
                                    hoursPerGroup -= 1
                                    horaActual = str(col).split("-")[3]
                            else:
                                horaActual = str(col).split("-")[3]
                        if colnum == 0:
                            openDate = str(col)
                        if colnum == 1:
                            openValue = float(col)
                        if counter == 1:
                            if colnum == 0:
                                horaActual = str(col).split("-")[3]
                            if colnum == 4:
                                closeValue = float(col)
                        if colnum == 2:
                            if float(col) > highValue:
                                highValue = float(col)
                        if colnum == 3:
                            if float(col) < lowValue:
                                lowValue = float(col)
                        if colnum == 5:
                            volValue += float(col)
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
        elif self.ui.comboBox_2.currentText() == 'Day/s':
            diaActual = "";      
            daysPerGroup = self.ui.spinBox.value()
            if self.ui.checkBox_7.isChecked():
                ofile = open('../Values/' + 'rap2_training' + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv', "wb")
            else:   
                ofile = open('../Values/' + self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv', "wb")
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
                            if diaActual != "" and diaActual != str(col).split("-")[0]:
                                if daysPerGroup == 1:
                                    counter = 1
                                    writer.writerow([openDate,openValue,highValue,lowValue,closeValue,volValue])
                                    highValue = 0.0
                                    lowValue = sys.float_info.max     
                                    volValue = 0
                                    daysPerGroup = self.ui.spinBox.value()
                                else:
                                    daysPerGroup -= 1
                                    diaActual = str(col).split("-")[0]
                            else:
                                diaActual = str(col).split("-")[0]
                        if colnum == 0:
                            openDate = str(col)
                        if colnum == 1:
                            openValue = float(col)
                        if counter == 1:
                            if colnum == 0:
                                diaActual = str(col).split("-")[0]
                            if colnum == 4:
                                closeValue = float(col)
                        if colnum == 2:
                            if float(col) > highValue:
                                highValue = float(col)
                        if colnum == 3:
                            if float(col) < lowValue:
                                lowValue = float(col)
                        if colnum == 5:
                            volValue += float(col)
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
        elif self.ui.comboBox_2.currentText() == 'Month/s':
            mesActual = "";      
            monthsPerGroup = self.ui.spinBox.value()
            if self.ui.checkBox_7.isChecked():
                ofile = open('../Values/' + 'rap2_training' + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv', "wb")
            else:   
                ofile = open('../Values/' + self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv', "wb")
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
                            volValue += float(col)
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
            anyoActual = "";      
            yearsPerGroup = self.ui.spinBox.value()
            if self.ui.checkBox_7.isChecked():
                ofile = open('../Values/' + 'rap2_training' + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv', "wb")
            else:
                ofile = open('../Values/' + self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv', "wb")
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
                            volValue += float(col)
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

        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        if self.ui.checkBox_7.isChecked():
            self.trainingFile = "1"
        if self.trainingFile == "":
            self.statusBar().showMessage('ERROR: You cannot plot something without selecting an index')
        else:
            if self.ui.checkBox_7.isChecked():
                ifile = open('../Values/rap2_training.csv', "rb")
            else:
                ifile = open('../Values/' + self.trainingFile + '.csv', "rb")
            reader = csv.reader(ifile)
            x = []
            y = []
            rownum = 0
            for row in reader:
                # Save header row.
                if rownum != 0:
                    colnum = 0
                    for col in row:
                        if colnum == 0:
    #                         print(rownum - 1)
                            x.append(rownum - 1)
                        elif colnum == 5:
                            y.insert(0, int(col))
    #                     print '%-8s: %s' % (header[colnum], col)
                        colnum += 1                     
                rownum += 1         
            ifile.close()
            
            plotWidget = pg.plot(title="Volume over the time")
            plotWidget.plot(np.asarray(x), np.asarray(y), pen=(1, 3))
            self.statusBar().showMessage("Volume plotted")    

    def plotCandle(self):
        # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        if self.ui.checkBox_7.isChecked():
            self.trainingFile = "AAPL"
        if self.trainingFile == "":
            self.statusBar().showMessage('ERROR: You cannot plot something without selecting an index')
        else:
            date1 = ( self.StartDate.year(), self.StartDate.month(), self.StartDate.day())
            date2 = ( self.EndDate.year(), self.EndDate.month(), self.EndDate.day())
            
            
            mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
            alldays    = DayLocator()              # minor ticks on the days
            weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
            
            quotes = quotes_historical_yahoo(self.trainingFile, date1, date2)
            
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
            self.statusBar().showMessage("Candles plotted")

    def addToPortfolio(self):
        if self.ui.checkBox_7.isChecked():
            self.modifyTrainingSet()
            self.trainingFile = 'rap2_training'
            if self.ui.comboBox_2.currentText() == 'Minute/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.ui.spinBox.value()) + 'min' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Hour/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.ui.spinBox.value()) + 'h' + '.csv')
            if self.ui.comboBox_2.currentText() == 'Day/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Month/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Year/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv')
            
        else:
            self.getTrainingSet()
            self.modifyTrainingSet()
            self.trainingFile = str(self.ui.widget.getSymbolSelected())
    
            self.StartDate = self.ui.startsDate.date()
            self.EndDate = self.ui.endDate.date()
            if self.ui.comboBox_2.currentText() == 'Minute/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'min' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Hour/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'h' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Day/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Month/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv')
            elif self.ui.comboBox_2.currentText() == 'Year/s':
                self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv')
            self.statusBar().showMessage("Labels obtained successfully")

    def calculateWinningsLooses(self):
        for x in range(0, self.ui.listWidget.__len__()):
            openValue = 0.0
            closeValue = 0.0
            highValue = 0.0
            lowValue = 0.0
            volume = 0
            prevOpenValue = 0.0
            prevCloseValue = 0.0
            rownum = 1
            actualHour = ""
            actualDay = ""
            actualMonth = ""
            actualYear = ""
            hour = ""
            day = ""
            month = ""
            year = ""
            dateCounter = 0
            lineToWrite = ""
            counter = 0
            storedLines = 0
            lineOpenValue = 0.0
            lineCloseValue = 0.0
            fileLabel = ""
            numOfDimensions = 0
                
            if self.ui.checkBox_1.isChecked():
                numOfDimensions += 1
            if self.ui.checkBox_2.isChecked():
                numOfDimensions += 1
            if self.ui.checkBox_3.isChecked():
                numOfDimensions += 1
            if self.ui.checkBox_4.isChecked():
                numOfDimensions += 1
            if self.ui.checkBox_5.isChecked():
                numOfDimensions += 1
            if self.ui.checkBox_6.isChecked():
                numOfDimensions += 1
            
            inputFile = '../Values/' + str(self.ui.listWidget.item(x).text())
            if self.ui.checkBox_8.isChecked() or numOfDimensions == 1:
                fileLabel += '-' + str(self.ui.spinBox_2.value())
                if self.ui.comboBox_3.currentText() == "Minute/s":
                    fileLabel += "min"
                elif self.ui.comboBox_3.currentText() == "Hour/s":
                    fileLabel += "h"
                elif self.ui.comboBox_3.currentText() == "Day/s":
                    fileLabel += "d"
                elif self.ui.comboBox_3.currentText() == "Month/s":
                    fileLabel += "m"
                elif self.ui.comboBox_3.currentText() == "Year/s":
                    fileLabel += "y"
                                
            if self.ui.checkBox_1.isChecked():
                lineToWrite += "Open Value,"
                fileLabel += "-OpenValue"
            if self.ui.checkBox_2.isChecked():
                lineToWrite += "Close Value,"
                fileLabel += "-CloseValue"
            if self.ui.checkBox_3.isChecked():
                lineToWrite += "Highest Value,"
                fileLabel += "-HighValue"
            if self.ui.checkBox_4.isChecked():
                lineToWrite += "Lowest Value,"
                fileLabel += "-LowValue"
            if self.ui.checkBox_5.isChecked():
                lineToWrite += "Volume Value,"
                fileLabel += "-VolumeValue"
            if self.ui.checkBox_6.isChecked():
                lineToWrite += "Gain Value,"
                fileLabel += "-GainValue"
            if self.ui.checkBox.isChecked():
                self.scalation(inputFile)
                inputFile += "-scaled"
                
            lineToWrite += "Label\n"
            
            self.ui.labeledFilesWidget.addItem(str(self.ui.listWidget.item(x).text()).split(".")[0] + fileLabel)
            ifile = open(inputFile, "rb")
            reader = csv.reader(ifile)
            rowmax = len(list(reader))
            ifile = open(inputFile, "rb")
            reader = csv.reader(ifile)
            ofile = open('../Values/' + str(self.ui.listWidget.item(x).text()).split(".")[0] + fileLabel, "wb")
            
            datos = np.zeros((rowmax-2,numOfDimensions))
            differences = []
            header = lineToWrite;
            ofile.write(lineToWrite)
            lineToWrite = ""
            for row in reader:
                if rownum != 1:
                    colnum = 0
                    for col in row:
                        if colnum == 0:
                            day = str(col).split("-")[0]
                            month = str(col).split("-")[1]
                            year = str(col).split("-")[2]
                            if self.ui.comboBox_3.currentText() == 'Hour/s':
                                hour = str(col).split("-")[3]
                        if colnum == 1:
                            openValue = float(col)
                        if colnum == 2:
                            highValue = float(col)
                        if colnum == 3:
                            lowValue = float(col)
                        if colnum == 4:
                            closeValue = float(col)
                        if colnum == 5:
                            volume = float(col)
                        colnum += 1
                    
                    counter += 1
                    if self.ui.comboBox_3.currentText() == 'Hour/s':
                        if actualHour == "":
                            actualHour = hour
                        elif actualHour != hour:
                            dateCounter += 1
                            actualHour = hour
                    elif self.ui.comboBox_3.currentText() == 'Day/s':
                        if actualDay == "":
                            actualDay = day
                        elif actualDay != day:
                            dateCounter += 1
                            actualDay = day
                    elif self.ui.comboBox_3.currentText() == 'Month/s':
                        if actualMonth == "":
                            actualMonth = month
                        elif actualMonth != month:
                            dateCounter += 1
                            actualMonth = month
                    elif self.ui.comboBox_3.currentText() == 'Year/s':
                        if actualYear == "":
                            actualYear = year
                        elif actualYear != year:
                            dateCounter += 1
                            actualYear = year;
                    
                    if numOfDimensions != 1 and self.ui.checkBox_8.isChecked():
                            i = 0
                            if self.ui.checkBox_1.isChecked():
                                datos[rownum-3][i] = openValue
                                i += 1
                            if self.ui.checkBox_3.isChecked():
                                datos[rownum-3][i] = highValue
                                i += 1
                            if self.ui.checkBox_4.isChecked():
                                datos[rownum-3][i] = lowValue
                                i += 1
                            if self.ui.checkBox_2.isChecked():
                                datos[rownum-3][i] = closeValue
                                i += 1
                            if self.ui.checkBox_5.isChecked():
                                datos[rownum-3][i] = volume
                                i += 1
                                
                    if storedLines == 0:
                        if counter == 1:
                            prevOpenValue = openValue
                        if self.ui.comboBox_3.currentText() == 'Minute/s': 
                            if counter == (self.ui.spinBox_2.value()/5) or rownum == rowmax:
                                prevCloseValue = closeValue
                                storedLines = 1
                                counter = 0
                        else:
                            if dateCounter == self.ui.spinBox_2.value() or rownum == rowmax:
                                storedLines = 1
                                dateCounter = 0
                                counter = 0
                                check = 0
                                if self.ui.checkBox_1.isChecked():
                                    lineToWrite += str(openValue)
                                    check = 1
                                if self.ui.checkBox_2.isChecked():
                                    lineToWrite += str(closeValue)
                                    check = 1
                                if self.ui.checkBox_3.isChecked():
                                    lineToWrite += str(highValue)
                                    check = 1
                                if self.ui.checkBox_4.isChecked():
                                    lineToWrite += str(lowValue)
                                    check = 1
                                if self.ui.checkBox_5.isChecked():
                                    lineToWrite += str(volume)
                                    check = 1
                                if self.ui.checkBox_6.isChecked():
                                    lineToWrite += str(closeValue-openValue)
                                    check = 1
                                if check == 1:
                                    lineToWrite += ";"
                                lineCloseValue = closeValue
                            else:
                                prevCloseValue = closeValue

                    else:
                        if self.ui.comboBox_3.currentText() == 'Minute/s':
                            check = 0
                            if self.ui.checkBox_1.isChecked():
                                lineToWrite += str(openValue) + ';'
                                check = 1
                            if self.ui.checkBox_2.isChecked():
                                lineToWrite += str(closeValue) + ';'
                                check = 1
                            if self.ui.checkBox_3.isChecked():
                                lineToWrite += str(highValue) + ';'
                                check = 1
                            if self.ui.checkBox_4.isChecked():
                                lineToWrite += str(lowValue) + ';'
                                check = 1
                            if self.ui.checkBox_5.isChecked():
                                lineToWrite += str(volume) + ';'
                                check = 1
                            if self.ui.checkBox_6.isChecked():
                                lineToWrite += str(closeValue-openValue) + ';'
                                check = 1
                            
                            lineToWrite = lineToWrite[:-1]
                        
                        if counter == 1:
                            lineOpenValue = openValue
                        
                        if self.ui.comboBox_3.currentText() == 'Minute/s':
                            if counter == (self.ui.spinBox_2.value()/5) or rownum == rowmax:
                                lineCloseValue = closeValue
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")
                                    differences.append('+1')
                                elif prevOpenValue - prevCloseValue <= 0:
                                    ofile.write(lineToWrite+"\n-1\n")
                                    differences.append('-1')
                                prevOpenValue = lineOpenValue
                                prevCloseValue = lineCloseValue
                                lineToWrite = ""
                                counter = 0
                        else:
                            if dateCounter == self.ui.spinBox_2.value():
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")
                                    differences.append('+1')
                                elif prevOpenValue - prevCloseValue <= 0:
                                    ofile.write(lineToWrite+"\n-1\n")
                                    differences.append('-1')
                                prevOpenValue = lineOpenValue
                                prevCloseValue = lineCloseValue
                                lineOpenValue = openValue
                                lineCloseValue = closeValue
                                lineToWrite = ""
                                dateCounter = 0;
                                counter = 1
                            
                            check = 0
                            if counter != 1:
                                lineToWrite += ";"
                            if self.ui.checkBox_1.isChecked():
                                lineToWrite += str(openValue)
                                check = 1
                            if self.ui.checkBox_2.isChecked():
                                lineToWrite += str(closeValue)
                                check = 1
                            if self.ui.checkBox_3.isChecked():
                                lineToWrite += str(highValue)
                                check = 1
                            if self.ui.checkBox_4.isChecked():
                                lineToWrite += str(lowValue)
                                check = 1
                            if self.ui.checkBox_5.isChecked():
                                lineToWrite += str(volume)
                                check = 1
                            if self.ui.checkBox_6.isChecked():
                                lineToWrite += str(closeValue-openValue)
                                check = 1
                            lineCloseValue = closeValue
                                    
                            if rownum == rowmax:
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")
                                    differences.append('+1')
                                elif prevOpenValue - prevCloseValue < 0:
                                    ofile.write(lineToWrite+"\n-1\n")
                                    differences.append('-1')
                        
                rownum += 1
            
            ifile.close()
            ofile.close()
            if numOfDimensions != 1 and self.ui.checkBox_8.isChecked():
                result = self.PCA(datos, 1)

                ofile = open('../Values/' + str(self.ui.listWidget.item(x).text()).split(".")[0] + fileLabel, "wb")
                i = 0
                ofile.write(header)
                matrixsize = result.shape[1]
                for label in differences:
                    j = 0
                    tmp = ""

                    if self.ui.checkBox_7.isChecked() and self.ui.comboBox_3.currentText() == 'Minute/s':
                        while j < (self.ui.spinBox_2.value()/5) and i < matrixsize-1:
                            tmp += str(result[0][i]) + ";"
                            j+=1
                            i+=1
                    else:
                        while j < self.ui.spinBox_2.value() and i < matrixsize-1:
                            tmp += str(result[0][i]) + ";"
                            j+=1
                            i+=1
                    
                    tmp = tmp[:-1]
                    
                    ofile.write(tmp + '\n' + label + '\n')
                ofile.close()

    def createCrossFiles(self):
        #almacenamos las 2 variables
        if self.ui.labeledFilesWidget.currentItem() == None:
            self.statusBar().showMessage('ERROR: You cannot create CV of something without selecting a file')
        else:
            trainingFile = str(self.ui.labeledFilesWidget.currentItem().text())
            self.num_training = self.ui.crossValidationPercent.value()
            
            #abrimos el fichero y almacenamos el numero de lineas y las lineas y lo recargamos
            ifile = open('../Values/' + trainingFile, "rb")
            reader = csv.reader(ifile)
            num_lineas = len(list(reader)) - 1
            ifile = open('../Values/' + trainingFile, "rb")
            reader = csv.reader(ifile)
    
            num_lineas = num_lineas / 2
            
            #calculamos el numero de lineas para cada fichero
            num_lineas_training = int((num_lineas*self.num_training)/100)
            
            num_lineas = num_lineas * 2
            num_lineas_training = num_lineas_training * 2
            
            #creamos el fichero training para meter todas las lineas
            ofile = open('../Values/' + trainingFile + '-Training', "wb")
            writer = csv.writer(ofile)
            
            #vamos poniendo las lineas
            num_lineas_insertadas = 0;
            rownum = 1
            for row in reader:
                if rownum != 1:
                    if num_lineas_insertadas == num_lineas_training:
                        ofile.close()
                    
                        #creamos el fichero test y vamos poniendo las lineas
                        ofile = open('../Values/' + trainingFile + '-Test', "wb")
                    writer = csv.writer(ofile)
                    #introducir la linea adecuada
                    writer.writerow(row)
                    num_lineas_insertadas += 1
                rownum += 1
                    
            ofile.close()
            self.statusBar().showMessage("CV files created")
            
    def callTrainingProgram(self):
        machineNumber = 0
        arguments = ""
        if self.ui.comboBox.currentText() == "Lineal Regression":
            machineNumber = 3
        elif self.ui.comboBox.currentText() == "Logistic Regression":
            machineNumber = 0
        elif self.ui.comboBox.currentText() == "Neural Network":
            machineNumber = 1
        elif self.ui.comboBox.currentText() == "SVM":
            machineNumber = 2
            
        predictOrTesting = 0
    
        if machineNumber == 0:
            arguments += str(self.ui.doubleSpinBox.value())
            arguments += " " + str(self.ui.doubleSpinBox_4.value())
        elif machineNumber == 1:
            arguments += str(self.ui.doubleSpinBox.value())
            arguments += ' '
            arguments += str(self.ui.doubleSpinBox_2.value())
            arguments += " " + str(self.ui.spinBox_3.value())
            arguments += " " + str(self.ui.doubleSpinBox_4.value())


        elif machineNumber == 2:
            if self.ui.comboBox_5.currentText() == "Soft":
                arguments += str(0)
            else:
                arguments += str(1)
            
            if self.ui.comboBox_7.currentText() == "Linear":
                arguments += " " + str(0)
            elif self.ui.comboBox_7.currentText() == "Polynomial":
                arguments += " " + str(1)
                arguments += " " + self.ui.spinBox_3.value()
            else:
                arguments += " " + str(2)
                arguments += " " + self.ui.spinBox_3.value()

            
            arguments += " " + str(self.ui.doubleSpinBox_4.value())

            
        elif machineNumber == 3:
            if self.ui.comboBox_6.currentIndex() == "Normal":
                arguments += str(1)
            else:
                arguments += str(2)
                arguments += ' '
                arguments += str(self.ui.doubleSpinBox_2.value())
                
        if self.ui.labeledFilesWidget.currentItem() == None:
            self.statusBar().showMessage('ERROR: You cannot test without selecting a file')
        else:
            trainingFile = '../Values/' + str(self.ui.labeledFilesWidget.currentItem().text()) + '-Training'
            testFile = '../Values/' + str(self.ui.labeledFilesWidget.currentItem().text()) + '-Test'
            print "./lgm" + " " + str(machineNumber) + " " + str(predictOrTesting) + " " + trainingFile + " " + testFile + " " + arguments
            os.system("./lgm" + " " + str(machineNumber) + " " + str(predictOrTesting) + " " + trainingFile + " " + testFile + " " + arguments)
            self.statusBar().showMessage("Testing")

    def scalation(self,trainingSet):
        scaleFile = open(trainingSet, "rb")
        reader = csv.reader(scaleFile)
        
        absolMax = [0.0,0.0,0.0,0.0,0.0,0.0]
        
        i = 0
        while i < 6:
            absolMax[i] = sys.float_info.min;
            i += 1
        
        print absolMax
        
        rownum = 1
        for row in reader:
            if rownum != 1:
                colnum = 1
                for col in row:
                    if colnum != 1:
                        num = float(col);
    
                        if num < 0:
                            num *= -1.0;
             
                        if num > absolMax[colnum-2]:
                            absolMax[colnum-2] = num;
                    colnum += 1
            rownum += 1
            
        scaleFile = open(trainingSet, "rb")
        reader = csv.reader(scaleFile)
        ofile = open(trainingSet+"-scaled", "wb")
        
        rownum = 1
        for row in reader:
            lineToWrite = ""
            colnum = 1
            for col in row:
                if rownum == 1:
                    if colnum == 1:
                        lineToWrite += str(col)
                    else:
                        lineToWrite += "," + str(col)
                else:
                    if colnum == 1:
                        lineToWrite += str(col)
                    else:
                        lineToWrite += "," + str(float(col) / absolMax[colnum-2])
                        
                colnum += 1
            lineToWrite += "\n"
            ofile.write(lineToWrite)
            rownum += 1
    
        scaleFile.close()
        ofile.close()

    def loadThetaValues(self):
        filePath = "../Values"
        if self.ui.comboBox_4.currentText() == "Logistic Regression":
            filePath += "/LR"
        elif self.ui.comboBox_4.currentText() == "Neural Network":
            filePath += "/NN"
        elif self.ui.comboBox_4.currentText() == "SVM":
            filePath += "/SVM"
        
        if self.ui.widget_2.getSymbolSelected() == "":
            self.statusBar().showMessage('ERROR: You cannot load a Theta file without selecting an index')
        else:
            filePath += "/" + str(self.ui.widget_2.getSymbolSelected())
                    
            fileList = os.listdir(filePath)
            
            for thetaFile in fileList:
                self.ui.listWidget_2.addItem(thetaFile)
            self.statusBar().showMessage("File loaded")
            
    def predictTodayValue(self):
        filePath = "../Values"
        if self.ui.comboBox_4.currentText() == "Logistic Regression":
            filePath += "/LR"
        elif self.ui.comboBox_4.currentText() == "Neural Network":
            filePath += "/NN"
        elif self.ui.comboBox_4.currentText() == "SVM":
            filePath += "/SVM"
        
        if self.ui.listWidget_2.currentItem() == None:
            self.statusBar().showMessage('ERROR: You cannot predict without selecting a file')
        else:
            filePath += "/" + str(self.ui.widget_2.getSymbolSelected()) + "/"
            filePath += str(self.ui.listWidget_2.currentItem().text())
            
            print filePath
            self.statusBar().showMessage("Predicting")
    
    def PCA(self, datos, k):
                
        sigma = (datos*datos)/len(datos)
        
        U, s, v = np.linalg.svd(sigma, full_matrices=True)

        uReduce = U[:,0:k]

        z = uReduce.T*datos.T
    
        return z

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

