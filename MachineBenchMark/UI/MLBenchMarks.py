import sys
import csv
import os
from DataMining import historicalprices
from DataMining import SymbolsParser
from PyQt4 import QtCore, QtGui
from pruebaUi import Ui_MainWindow
from DataMining.historicalprices import get_historical
from PIL import Image
from numpy import *


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
        self.changeMachineParameters()
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.PlotVolumeButton, QtCore.SIGNAL("clicked()"), self.plotVolume)
        QtCore.QObject.connect(self.ui.PlotCandlesButton, QtCore.SIGNAL("clicked()"), self.plotCandle)
        QtCore.QObject.connect(self.ui.addToPortfolioButton, QtCore.SIGNAL("clicked()"), self.addToPortfolio)
        QtCore.QObject.connect(self.ui.getLabelButton, QtCore.SIGNAL("clicked()"), self.calculateWinningsLooses)
        QtCore.QObject.connect(self.ui.crossValidationButton, QtCore.SIGNAL("clicked()"), self.createCrossFiles)
        QtCore.QObject.connect(self.ui.TrainButton, QtCore.SIGNAL("clicked()"), self.callTrainingProgram)
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.changeMachineParameters)
        
    def changeMachineParameters(self):
        if self.ui.comboBox.currentText() == "Logistic Regression":
            self.ui.label_2.setText("Regularization")
            self.ui.doubleSpinBox.show()
            self.ui.comboBox_5.hide()
        elif self.ui.comboBox.currentText() == "Neural Network":
            self.ui.label_2.setText("Regularization")
            self.ui.doubleSpinBox.show()
            self.ui.comboBox_5.hide()
        elif self.ui.comboBox.currentText() == "SVM":
            self.ui.label_2.setText("Margin")
            self.ui.doubleSpinBox.hide()
            self.ui.comboBox_5.show()

    def getTrainingSet(self):
        # Obtengo las fechas para la descarga
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        self.symbol = str(self.ui.widget.getSymbolSelected())
        get_historical(self.symbol, self.StartDate.day(), self.StartDate.month(), self.StartDate.year(), self.EndDate.day(), self.EndDate.month(), self.EndDate.year())
        print("Archivo descargado")  
        # Pinto los datos
                
    def modifyTrainingSet(self):
        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
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
        ifile = open('../Values/' + self.trainingFile + '.csv', "rb")
        reader = csv.reader(ifile)
        if self.ui.comboBox_2.currentText() == 'Day/s':
            print "Partimos por dias"
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
        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        ifile = open('../Values/' + self.trainingFile + '.csv', "rb")
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
        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        date1 = ( self.StartDate.year(), self.StartDate.month(), self.StartDate.day())
        date2 = ( self.EndDate.year(), self.EndDate.month(), self.EndDate.day())
        
        
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays    = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12
        
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

    def addToPortfolio(self):
        self.getTrainingSet()
        self.modifyTrainingSet()
        self.trainingFile = str(self.ui.widget.getSymbolSelected())
        self.StartDate = self.ui.startsDate.date()
        self.EndDate = self.ui.endDate.date()
        if self.ui.comboBox_2.currentText() == 'Day/s':
            self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'd' + '.csv')
        elif self.ui.comboBox_2.currentText() == 'Month/s':
            self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'm' + '.csv')
        elif self.ui.comboBox_2.currentText() == 'Year/s':
            self.ui.listWidget.addItem(self.trainingFile + '-' + str(self.StartDate.year())+str(self.StartDate.month()).zfill(2)+str(self.StartDate.day()).zfill(2) + '-' + str(self.EndDate.year())+str(self.EndDate.month()).zfill(2)+str(self.EndDate.day()).zfill(2) + '-' + str(self.ui.spinBox.value()) + 'y' + '.csv')

    def calculateWinningsLooses(self):
        print "Empezamos a calcular ganancias/perdidas"
        for x in range(0, self.ui.listWidget.__len__()):
            openValue = 0.0
            closeValue = 0.0
            highValue = 0.0
            lowValue = 0.0
            volume = 0
            prevOpenValue = 0.0
            prevCloseValue = 0.0
            rownum = 1
            actualMonth = ""
            actualYear = ""
            month = ""
            year = ""
            dateCounter = 0
            lineToWrite = ""
            counter = 0
            storedLines = 0
            lineOpenValue = 0.0
            lineCloseValue = 0.0
            fileLabel = ""
            fileLabel += str(self.ui.spinBox_2.value())
            if self.ui.comboBox_3.currentText() == "Day/s":
                fileLabel += "d"
            elif self.ui.comboBox_3.currentText() == "Month/s":
                fileLabel += "m"
            elif self.ui.comboBox_3.currentText() == "Year/s":
                fileLabel += "y"
                
            if self.ui.radioButton.isChecked():
                lineToWrite += "Open Value,"
                fileLabel += "-OpenValue"
            if self.ui.radioButton_2.isChecked():
                lineToWrite += "Close Value,"
                fileLabel += "-CloseValue"
            if self.ui.radioButton_3.isChecked():
                lineToWrite += "Highest Value,"
                fileLabel += "-HighValue"
            if self.ui.radioButton_4.isChecked():
                lineToWrite += "Lowest Value,"
                fileLabel += "-LowValue"
            if self.ui.radioButton_5.isChecked():
                lineToWrite += "Volume Value,"
                fileLabel += "-VolumeValue"
            if self.ui.radioButton_6.isChecked():
                lineToWrite += "Gain Value,"
                fileLabel += "-GainValue"
            if self.ui.radioButton_7.isChecked():
                lineToWrite += "PCA Value,"
                fileLabel += "-PCAValue"
            lineToWrite += "Label\n"
            
            self.ui.labeledFilesWidget.addItem(str(self.ui.listWidget.item(x).text()).split(".")[0] + "-" + fileLabel)
            ifile = open('../Values/' + str(self.ui.listWidget.item(x).text()), "rb")
            reader = csv.reader(ifile)
            rowmax = len(list(reader))
            ifile = open('../Values/' + str(self.ui.listWidget.item(x).text()), "rb")
            reader = csv.reader(ifile)
            ofile = open('../Values/' + str(self.ui.listWidget.item(x).text()).split(".")[0] + "-" + fileLabel, "wb")
            
            
            ofile.write(lineToWrite)  
            lineToWrite = ""
            for row in reader:
                if rownum != 1:
                    colnum = 0
                    for col in row:
                        if colnum == 0:
                            month = str(col).split("-")[1]
                            year = str(col).split("-")[2]
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
                    if self.ui.comboBox_3.currentText() == 'Month/s':
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
                    
                    if storedLines == 0:
                        if counter == 1:
                            prevOpenValue = openValue
                        if self.ui.comboBox_3.currentText() == 'Day/s': 
                            if counter == self.ui.spinBox_2.value() or rownum == rowmax:
                                prevCloseValue = closeValue
                                storedLines = 1
                                counter = 0
                        else:
                            if dateCounter == self.ui.spinBox_2.value() or rownum == rowmax:
                                storedLines = 1
                                dateCounter = 0
                                counter = 0
                                check = 0
                                if self.ui.radioButton.isChecked():
                                    lineToWrite += str(openValue)
                                    check = 1
                                if self.ui.radioButton_2.isChecked():
                                    lineToWrite += str(closeValue)
                                    check = 1
                                if self.ui.radioButton_3.isChecked():
                                    lineToWrite += str(highValue)
                                    check = 1
                                if self.ui.radioButton_4.isChecked():
                                    lineToWrite += str(lowValue)
                                    check = 1
                                if self.ui.radioButton_5.isChecked():
                                    lineToWrite += str(volume)
                                    check = 1
                                if self.ui.radioButton_6.isChecked():
                                    lineToWrite += str(closeValue-openValue)
                                    check = 1
                                if check == 1:
                                    lineToWrite += ";"
                                lineCloseValue = closeValue
                            else:
                                prevCloseValue = closeValue

                    else:
                        if self.ui.comboBox_3.currentText() == 'Day/s':
                            check = 0
                            if self.ui.radioButton.isChecked():
                                lineToWrite += str(openValue)
                                check = 1
                            if self.ui.radioButton_2.isChecked():
                                lineToWrite += str(closeValue)
                                check = 1
                            if self.ui.radioButton_3.isChecked():
                                lineToWrite += str(highValue)
                                check = 1
                            if self.ui.radioButton_4.isChecked():
                                lineToWrite += str(lowValue)
                                check = 1
                            if self.ui.radioButton_5.isChecked():
                                lineToWrite += str(volume)
                                check = 1
                            if self.ui.radioButton_6.isChecked():
                                lineToWrite += str(closeValue-openValue)
                                check = 1
                            
                            if check == 1:
                                if counter < self.ui.spinBox_2.value():
                                    lineToWrite += ";"

                        
                        if counter == 1:
                            lineOpenValue = openValue
                        
                        if self.ui.comboBox_3.currentText() == 'Day/s':
                            if counter == self.ui.spinBox_2.value() or rownum == rowmax:
                                lineCloseValue = closeValue
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")  
                                elif prevOpenValue - prevCloseValue < 0:
                                    ofile.write(lineToWrite+"\n-1\n") 
                                prevOpenValue = lineOpenValue
                                prevCloseValue = lineCloseValue
                                lineToWrite = ""
                                counter = 0
                        else:
                            if dateCounter == self.ui.spinBox_2.value():
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")  
                                elif prevOpenValue - prevCloseValue < 0:
                                    ofile.write(lineToWrite+"\n-1\n") 
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
                            if self.ui.radioButton.isChecked():
                                lineToWrite += str(openValue)
                                check = 1
                            if self.ui.radioButton_2.isChecked():
                                lineToWrite += str(closeValue)
                                check = 1
                            if self.ui.radioButton_3.isChecked():
                                lineToWrite += str(highValue)
                                check = 1
                            if self.ui.radioButton_4.isChecked():
                                lineToWrite += str(lowValue)
                                check = 1
                            if self.ui.radioButton_5.isChecked():
                                lineToWrite += str(volume)
                                check = 1
                            if self.ui.radioButton_6.isChecked():
                                lineToWrite += str(closeValue-openValue)
                                check = 1
                            lineCloseValue = closeValue
                                    
                            if rownum == rowmax:
                                if prevOpenValue - prevCloseValue > 0:
                                    ofile.write(lineToWrite+"\n+1\n")  
                                elif prevOpenValue - prevCloseValue < 0:
                                    ofile.write(lineToWrite+"\n-1\n") 
                rownum += 1
            ifile.close()
            ofile.close()

    def createCrossFiles(self):
        #almacenamos las 2 variables
        trainingFile = str(self.ui.labeledFilesWidget.currentItem().text())
        print trainingFile
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
            
    def callTrainingProgram(self):
        machineNumber = 0
        predictOrTesting = 0
        arguments = ""
        if self.ui.comboBox.currentText() == "Logistic Regression":
            machineNumber = 0
        elif self.ui.comboBox.currentText() == "Neural Network":
            machineNumber = 1
        elif self.ui.comboBox.currentText() == "SVM":
            machineNumber = 2
        if self.ui.comboBox_4.currentText() == "Train and Test":
            predictOrTesting = 0
        elif self.ui.comboBox_4.currentText() == "Predict":
            predictOrTesting = 1
    
        if machineNumber == 0:
            arguments += str(self.ui.doubleSpinBox.value())
        elif machineNumber == 1:
            arguments += str(self.ui.doubleSpinBox.value())
        elif machineNumber == 2:
            if self.ui.comboBox_5.value() == "Soft":
                arguments += str(0)
            else:
                arguments += str(1)
            
        trainingFile = '../Values/' + str(self.ui.labeledFilesWidget.currentItem().text()) + '-Training'
        testFile = '../Values/' + str(self.ui.labeledFilesWidget.currentItem().text()) + '-Test'
        
        os.system("./lgm" + " " + str(machineNumber) + " " + str(predictOrTesting) + " " + trainingFile + " " + testFile + " " + arguments)
    
#     def scalation(self,sample):
#         absolMax = sys.float_info.min;
#             
#         for(int i = 0; i < trainingSet.size(); i++){
#             for(int j = 0; j < trainingSet[i].input.size(); j++){
#                 double num = trainingSet[i].input[j];
# 
#                 if(num < 0){
#                     num *= -1.0;
#                 }
# 
#                 if(num > absolMax){
#                     absolMax = num;
#                 }
#             }
#         }
# 
#         for(int i = 0; i < trainingSet.size(); i++){
#             for(int j = 0; j < trainingSet[i].input.size(); j++){
#                 trainingSet[i].input[j] /= absolMax;
#             }
#         }

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
