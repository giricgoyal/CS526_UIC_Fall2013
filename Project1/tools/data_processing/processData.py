#-----------------------------------------------
#	"processData.py to process the crime data
#	
#	Author: Giric Goyal
#-----------------------------------------------

# imports
import csv
import sqlite3

# defining variables
#-------------------
# column list to extract
columnList = ["Date", "Block", "Primary Type", "Latitude", "Longitude"]
conn = sqlite3.connect('project1.db')
c = conn.cursor()
# output array to write to new separate csv files
outputList = ""

# column Index list to store the index of the desired columns
columnIndexList = [] 

# Method definitions
#-------------------
# defining a writer method to write to all the 13 files
def updateFile(year, data, type):
	print "Writing to : " + type + ", " + year
	print data
	datenTime = data.strip().split("\t")[0]
	date = datenTime.strip().split(" ")[0]
	time = datenTime.strip().split(" ")[1] + " " + datenTime.strip().split(" ")[2]
	block = data.strip().split("\t")[1]
	lat = data.strip().split("\t")[2]
	lon = data.strip().split("\t")[3]
	c.execute("CREATE TABLE if not exists table"+year+" (type text,date text, time text, block text, lat real, lon real)")
	c.execute("INSERT INTO table"+year+" VALUES('"+type+"','"+date+"','"+time+"','"+block+"',"+lat+","+lon+")")
	#file = open('..\..\data\chicago_data\crime_data\\'+year+'\\'+type+'.txt', 'a+')
	#file.write(data)
	
#------------------------------------------------------------------
# opening the main crime data file
# creating input Stream
# getting selective columnns in list
counter = 0
print "Reading input file"
with open('..\..\data\chicago_data\crimes01to13.csv' , 'rb') as mainInputFile:
	inputReader = csv.reader(mainInputFile)
	for row in inputReader:
		counter += 1
		if counter == 1:
			for columnElement in columnList:
				for rowElement in row:
					if rowElement == columnElement:
						columnIndexList.append(row.index(rowElement))
						#print rowElement + " : " + str(row.index(rowElement))
		else:
			break
	
counter = 0	
with open('..\..\data\chicago_data\crimes01to13.csv' , 'rb') as mainInputFile:
	inputReader = csv.reader(mainInputFile)
	for row in inputReader:
		counter += 1
		outputList = ""
		for columnIndex in columnIndexList:
			if (columnIndex <= len(row)) & (row != ""):
				outputList += row[columnIndex] + "\t"
		outputList = outputList.strip() + "\n"
		if len(outputList.split("\t")) == 5: 
			if counter == 1:
				pass
			else:
				fullDateTime = str(row[2]).strip().split(" ")
				date = fullDateTime[0]
				dateAsArray = date.strip().split("/")
				year = dateAsArray[2]
				type = outputList.strip().split("\t")[2]
				outputListAsArray = outputList.strip().split("\t")
				newOutputList = outputListAsArray[0] + "\t" + outputListAsArray[1] + "\t" + outputListAsArray[3] + "\t" + outputListAsArray[4] + "\n"
				updateFile(year, newOutputList , type)
	conn.commit()
	conn.close()