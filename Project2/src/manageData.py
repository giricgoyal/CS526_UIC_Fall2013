# #######################################################
# managing data, populating data structures
#
# author: giric goyal
# #######################################################


from sqlite3 import *
from util import *
from math import *
from euclid import *
from omega import *
from cyclops import *


#------------------------------------------------
# variables
# Sql object
c = ""


# data structure to store values
name = ""
radius = 0.0
mass = 0.0
period = 0.0
rotation = 0.0
axis_distance = 0.0
eccentricity = 0.0
inclination = 0.0
discovered_age = 0
detection_type = ""
molecules_starType = ""
isStar = 0
system_name = ""

# indices
i_Name = 0
i_Radius = 1
i_Mass = 2
i_Period = 3
i_Rotation = 4
i_Axis_Distance = 5
i_Eccentricity = 6
i_Inclination = 7
i_Discovered_Age = 8
i_Detection_Type = 9
i_Molecules_StarType = 10
i_IsStar = 11
i_System_Name = 12


# ----------------------------------------------------------------
# method definitions
def getData():
	for system in systemList:
		readFromFile = "Select * from objects where system_name like '"+system+"'"
		rawDataSet = c.execute(readFromFile)
		data = dict()
		data2 = dict()
		for singleSet in rawDataSet:
			name = singleSet[i_Name]
			radius = singleSet[i_Radius]
			mass = singleSet[i_Mass]
			period = singleSet[i_Period]
			rotation = singleSet[i_Rotation]
			axis_distance = singleSet[i_Axis_Distance]
			eccentricity = singleSet[i_Eccentricity]
			inclination = singleSet[i_Inclination]
			discovered_age = singleSet[i_Discovered_Age]
			detection_type = singleSet[i_Detection_Type]
			molecules_starType = singleSet[i_Molecules_StarType]
			isStar = singleSet[i_IsStar]
			system_name = singleSet[i_System_Name]
			if isStar == 0:
				bodyInfoObj = bodyInfo(name, mass, discovered_age, detection_type, molecules_starType, system_name, 0.0, 0.0, "-", isStar)
				bodyOrbitObj = bodyOrbit(name, radius, axis_distance, eccentricity, inclination, period, rotation, "-", isStar)
			else:
				bodyInfoObj = bodyInfo(name, mass, "", "", "", system_name, axis_distance, discovered_age, molecules_starType, isStar)
				bodyOrbitObj = bodyOrbit(name, radius, 0.0, 0.0, inclination, 365, rotation, molecules_starType, isStar)
			data[name] = bodyOrbitObj
			data2[name] = bodyInfoObj
		allSystemsOrbital[system] = data
		allSystemsInfo[system] = data2
		
	for system in systemList:
		readFromFile = "Select * from starLoc"
		rawDataSet = c.execute(readFromFile)
		name = ""
		ra = ""
		sec = ""
		dist = 0.0
		for data in rawDataSet:
			name = data[0]
			ra = data[1]
			dec = data[2]
			dist = data[3]
			starLocObj = starLoc(name, ra, dec, dist)
			starLocations[name] = starLocObj
	
def initDB():
	print "initializing db"
	global c
	conn = connect("data/project2.db")
	c = conn.cursor()
