import sqlite3 as sql
import util

from math import *
from euclid import *
from omega import *
from cyclops import *

global sqlObj

# method desinitions
def executeQuery(query):
	print "executing : " + query
	dataSet = []
	for temp in sqlObj.execute(query):
		dataSet.append(temp)
	return dataSet

def getCrimeData():	
	crimeClause = ""
	communityClause = ""
	timeClause = ""
	query = ""
	result = []
	if (util.precisionLevel == "Default") or (util.selectedYear == "2001-2013"):
		for i in range(2001,2014):
			query = "select lon, lat, type from year" + str(i)
			if util.selectedCrime != "":
				crimeClause = "type like '" + util.selectedCrime + "' " 
			#if util.selectedComm != "":
			#	query = query + ", communityLocations "
			#	communityClause = "number = area and name like '" + util.selectedComm + "' "
			if (crimeClause != "") or (communityClause != ""):
				query += " where "
			if crimeClause != "":
				query += crimeClause
			if communityClause != "":
				if crimeClause != "":
					query += "and "
				query += communityClause
			for row in executeQuery(query):
				result.append(row)
				
	else:		
		query = "select lon, lat, type from year" + util.selectedYear
	
		if util.selectedCrime != "":
			crimeClause = "type like '" + util.selectedCrime + "' " 
		#if util.selectedComm != "":
		#	query = query + ", communityLocations "
		#	communityClause = "number = area and name like '" + util.selectedComm + "' "
		
		if util.precisionLevel == "Year":
			pass
		else:
			if util.precisionLevel == "Month":
				if util.selectedMonth != 0:
					mon = str(util.selectedMonth)
					if util.selectedMonth < 10:
						mon = "0" + mon
					time1 = mon + "/"
					timeClause = "date like '" + time1 + "%'"
			else:
				if util.precisionLevel == "Day":
					if (util.selectedMonth != 0) and (util.selectedDate != 0):
						mon = str(util.selectedMonth)
						if util.selectedMonth < 10:
							mon = "0" + mon
						date = str(util.selectedDate)
						if util.selectedDate < 10:
							date = "0" + date
						time1 = mon + "/" + date + "/"
						timeClause = "date like '" + time1 + "%'" 
				
				else:
					if util.precisionLevel == "Hour":
						if (util.selectedMonth != 0) and (util.selectedDate != 0) and (util.selectedHour != 0):
							mon = str(util.selectedMonth)
							if util.selectedMonth < 10:
								mon = "0" + mon
							date = str(util.selectedDate)
							if util.selectedDate < 10:
								date = "0" + date
							hour = str(util.selectedHour)
							if util.selectedHour < 10:
								hour = "0" + hour
							time1 = mon + "/" + date + "/" + util.selectedYear
							time1 += " " + hour + ":"
							time2 = " " + util.selectedP
							timeClause = "date like '" + time1 + "%" + time2 +"'"
					
					else:			
						if (util.selectedMonth != 0) and (util.selectedDate != 0) and (util.selectedHour != 0):
							mon = str(util.selectedMonth)
							if util.selectedMonth < 10:
								mon = "0" + mon
							date = str(util.selectedDate)
							if util.selectedDate < 10:
								date = "0" + date
							hour = str(util.selectedHour)
							if util.selectedHour < 10:
								hour = "0" + hour
							min = str(util.selectedMin)
							if util.selectedMin < 10:
								min = "0" + min
							
							time1 = mon + "/" + date + "/" + util.selectedYear
							time1 += " " + hour + ":" + min + ":"
							time2 = " " + util.selectedP
							timeClause = "date like '" + time1 + "%" + time2 +"'"
	
		if (crimeClause != "") or (communityClause != "") or (timeClause != ""):
			query += " where "
		if crimeClause != "":
			query += crimeClause
		if communityClause != "":
			if crimeClause != "":
				query += "and "
			query += communityClause
		if timeClause != "":
			if (communityClause != "") or (crimeClause != ""):
				query += "and "
			query += timeClause
		for row in executeQuery(query):
			result.append(row)
	return result
	
def getCrimeCount():
	#query = "select name,count(*) from year" + util.selectedYear + ", communityLocations where number = area "
	#if util.selectedCrime != "":
	#	query += "and type like '" + util.selectedCrime + "' "
	#if util.selectedComm != "":
	#	query += "and name like '" + util.selectedComm + "'" 
	#if util.selectedComm == "":
	#	query += "group by name"
	#return executeQuery(query)
	groupBy = "group by name"
	crimeClause = ""
	communityClause = ""
	timeClause = ""
	query = ""
	result = []
	if (util.precisionLevel == "Default") or (util.selectedYear == "2001-2013"):
		for i in range(2001,2014):
			query = "select name,count(*) from year" + str(i)
			query = query + ", communityLocations where number = area "
			if util.selectedCrime != "":
				crimeClause = "and type like '" + util.selectedCrime + "' " 
			#if util.selectedComm != "":
			#	communityClause = "and name like '" + util.selectedComm + "' "
			if crimeClause != "":
				query += crimeClause
			if communityClause != "":
				query += communityClause
			if util.selectedComm == "":
				query += groupBy
			for row in executeQuery(query):
				result.append(row)
				
	else:		
		query = "select name,count(*) from year" + util.selectedYear
		query = query + ", communityLocations where number = area "
		if util.selectedCrime != "":
			crimeClause = "and type like '" + util.selectedCrime + "' " 
		#if util.selectedComm != "":
		#	communityClause = "and name like '" + util.selectedComm + "' "
		
		if util.precisionLevel == "Year":
			pass
		else:
			if util.precisionLevel == "Month":
				if util.selectedMonth != 0:
					mon = str(util.selectedMonth)
					if util.selectedMonth < 10:
						mon = "0" + mon
					time1 = mon + "/"
					timeClause = "and date like '" + time1 + "%' "
			else:
				if util.precisionLevel == "Day":
					if (util.selectedMonth != 0) and (util.selectedDate != 0):
						mon = str(util.selectedMonth)
						if util.selectedMonth < 10:
							mon = "0" + mon
						date = str(util.selectedDate)
						if util.selectedDate < 10:
							date = "0" + date
						time1 = mon + "/" + date + "/"
						timeClause = "and date like '" + time1 + "%' " 
				
				else:
					if util.precisionLevel == "Hour":
						if (util.selectedMonth != 0) and (util.selectedDate != 0) and (util.selectedHour != 0):
							mon = str(util.selectedMonth)
							if util.selectedMonth < 10:
								mon = "0" + mon
							date = str(util.selectedDate)
							if util.selectedDate < 10:
								date = "0" + date
							hour = str(util.selectedHour)
							if util.selectedHour < 10:
								hour = "0" + hour
							time1 = mon + "/" + date + "/" + util.selectedYear
							time1 += " " + hour + ":"
							time2 = " " + util.selectedP
							timeClause = "and date like '" + time1 + "%" + time2 +"' "
					
					else:			
						if (util.selectedMonth != 0) and (util.selectedDate != 0) and (util.selectedHour != 0):
							mon = str(util.selectedMonth)
							if util.selectedMonth < 10:
								mon = "0" + mon
							date = str(util.selectedDate)
							if util.selectedDate < 10:
								date = "0" + date
							hour = str(util.selectedHour)
							if util.selectedHour < 10:
								hour = "0" + hour
							min = str(util.selectedMin)
							if util.selectedMin < 10:
								min = "0" + min
							
							time1 = mon + "/" + date + "/" + util.selectedYear
							time1 += " " + hour + ":" + min + ":"
							time2 = " " + util.selectedP
							timeClause = "and date like '" + time1 + "%" + time2 +"' "
	
		if crimeClause != "":
			query += crimeClause
		if communityClause != "":
			query += communityClause
		if timeClause != "":
			query += timeClause
		if util.selectedComm == "":
				query += groupBy
		for row in executeQuery(query):
			result.append(row)
	return result
	
def __init__():
	print "initializing db"
	global sqlObj
	conn = sql.connect("data/chicago_data/project1.db")
	sqlObj = conn.cursor()
	
def getCommunityData():
	query = "select * from communityBounds"
	return executeQuery(query)

def getCommunityLocations():
	query = "select * from communityLocations"
	return executeQuery(query)
	
def getCommunityLocationByName():
	query = "select * from communityLocations where name like '" + util.selectedComm + "'"
	return executeQuery(query)
	
def getMaxMinCount():
	query = "select MAX(c), MIN(c) from ( select count(*) as c from year" + util.selectedYear + ", communityLocations where number = area "
	if util.selectedCrime != "":
		query += "and type like '" + util.selectedCrime + "' "
	if util.selectedComm != "":
		query += "and name like '" + util.selectedComm + "'" 
	if util.selectedComm == "":
		query += "group by name)"
	return executeQuery(query) 

def getRealTimeData(dtObj):
	date = dtObj.mm + "/" + dtObj.dd + "/2012 " + dtObj.hr + ":" + dtObj.min + ":% " + dtObj.p
	crimeClause = ""
	if util.selectedCrime != "":
		crimeClause = "and type like '" + util.selectedCrime + "'"
	query = "select lon, lat from year2012 where date like '" + date + "' "
	return executeQuery(query)
	
#---------------------------------------------------------------------------------	
# variables
sqlObj = ""