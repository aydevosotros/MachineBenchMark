import urllib
import re

#https://www.google.com/finance/historical?cid=694653&startdate=Dec+15%2C+2000&enddate=Dec+14%2C+2013&ei=jcSsUpDrIKjmsgemUg

def get_historical(symbol, startDay, startMonth, startYear, endDay, endMonth, endYear):
	base_url = 'http://www.google.com/finance/historical?q='
	time_range = '&startdate='+monthTraslator(startMonth)+'+'+str(startDay)+'%2C+'+str(startYear)+'&enddate='+monthTraslator(endMonth)+'+'+str(endDay)+'%2C+'+str(endYear) #Esto se formatea para unas fechas concretas
	print("Descagando: " + base_url + symbol + time_range + "&output=csv", symbol+".csv")
	data = urllib.urlopen(base_url + symbol + time_range + "&output=csv")
	print(data.read())

def monthTraslator(month):
	if month == 1:
		return "Jan"
	elif month == 2:
		return "Feb"
	elif month == 3:
		return "Mar"
	elif month == 4:
		return "Apr"
	elif month == 5:
		return "May"
	elif month == 6:
		return "Jun"
	elif month == 7:
		return "Jul"
	elif month == 8:
		return "Aug"
	elif month == 9:
		return "Sep"
	elif month == 10:
		return "Oct"
	elif month == 11:
		return "Nov"
	elif month == 12:
		return "Dec"