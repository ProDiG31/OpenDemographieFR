# coding: utf-8
import csv
import os
import time
import datetime

codeCommuneData =[]
data = {}


# -------- FUNCTIONS WHICH BE EXECUTED BELOW ------------------

def loadDemographie(year):
	print ('[INFO] - Counting Row ')
	filename = '../source/demo_fr_%s.csv' % year
	totalrows =  len(open(filename).readlines()) - 1
	t0 = time.time()

	with open(filename) as csvfile:
	# ---- Read each line of csv file
		reader = csv.DictReader(csvfile, delimiter=';' , lineterminator ='\n')
		rowNumber = 0
		
		print ('[INFO] - line %d: %s' % (rowNumber, totalrows))
		for row in reader:
			#print(row)
            # ----- load data
			cdeCommune = row["COM"]
			#NmeCommune = row[1]
			NbHabitant = row["POP"]

			# Si le code commune a deja etait lu
			if (cdeCommune in data):
				data[cdeCommune].append([year,NbHabitant])
			else: #sinon on l'ajoute dans le table 
				data[cdeCommune] = [[year,NbHabitant]]

			if(cdeCommune not in codeCommuneData):
				codeCommuneData.append(cdeCommune)
            

			# ---- Log current activities
			rowNumber += 1
			percent = rowNumber * 100 / totalrows
			elapsedTime = time.time() - t0
			try:
				rate = rowNumber // elapsedTime
			except ZeroDivisionError:
				rate = 1
			timeLeftSec = abs((rowNumber - totalrows) / rate)
			timeLeftString = str(datetime.timedelta(seconds=timeLeftSec))

			print ('[INFO] %s - line %d : %s	- Progressing :	%.3f%%	- Elapsed time : %.2f sec (%s[,-4]) - Rate : %.2f input/Sec' %
							(year,
							 rowNumber,
							 totalrows,
							 percent,
							 elapsedTime,
							 timeLeftString,
							 rate))		
	print('[INFO] - Elapsed time : %.2f sec' % (time.time() - t0))

# def parseDemographie()


loadDemographie("2016")
loadDemographie("2015")
loadDemographie("2014")
loadDemographie("2013")
loadDemographie("2012")
loadDemographie("2011")
loadDemographie("2010")
loadDemographie("1990")
loadDemographie("1982")
loadDemographie("1975")
loadDemographie("1968")

print (data)


