#-----------------------------------------------
#	"processData.py to get useful data from the exoplanet data set 
#	and divide into planets and star data set
#
#	Author: Giric Goyal
#-----------------------------------------------

# imports
import sqlite3
from math import *

# defining variables
#-------------------

conn = sqlite3.connect('project2.db')
c = conn.cursor()

# data structure to store values
name = ""
mass = 0.0
radius = 0.0
period = 0.0
axis = 0.0
eccentricity = 0.0
inclination = 0.0
discovered = 0
detection_type = ""
molecules = ""
star_name = ""
star_distance = 0.0
star_mass = 0.0
star_radius = 0.0
star_spec_type = ""
star_age = 0.0
star_teff = 0.0
star_other_name = ""

# indices
i_Name = 0
i_Mass = 1
i_Radius = 2
i_Period = 3
i_Axis = 4
i_Eccentricity = 5
i_Inclination = 6
i_Discovered = 7
i_Detection_Type = 8
i_Molecules = 9
i_Star_Name = 10
i_Star_Distance = 11
i_Star_Mass = 12
i_Star_Radius = 13
i_Star_Spec_Type = 14
i_Star_Age = 15
i_Star_Teff = 16

starList = ["HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "XO-3", "Kepler-22", "MOA-2007-BLG-192-L", "Kepler-11", "Kepler-10", "GJ 1214", "GL 581", "WASP-33", "30 Ari B", "Kepler-39", "HR 8799", "Kepler-65", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "GL 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]


# -----------------------------------------------
# main
insertList = []
rEarth = (12756/142984)
mEarth = 5.97/1898
for star in starList:
	readFromFile = "Select * from cat1 where star_name like '" + star + "';"
	rawDataSet = c.execute(readFromFile)
	for singleSet in rawDataSet:
		#print singleSet[0]
		name = "" if singleSet[i_Name] == "" else singleSet[i_Name]
		mass = 0.0 if singleSet[i_Mass] == "" else singleSet[i_Mass]
		radius = 0.0 if singleSet[i_Radius] == "" else singleSet[i_Radius]
		if singleSet[i_Radius] == "":
			ratio = mass/mEarth
			if ratio >= 200:
				radius = 22.6 * pow(ratio, -0.08865)
			elif ratio >= 1:
				radius = pow(ratio, 0.5)
			elif ratio < 1:
				radius = pow(ratio,0.3)
			radius = (radius * (12756/2)) / (142984/2)
		period = 0.0 if singleSet[i_Period] == "" else singleSet[i_Period]
		axis = 0.0 if singleSet[i_Axis] == "" else singleSet[i_Axis]
		eccentricity  = 0.0 if singleSet[i_Eccentricity] == "" else singleSet[i_Eccentricity]
		inclination = 0.0 if singleSet[i_Inclination] == "" else singleSet[i_Inclination]
		discovered = 0 if singleSet[i_Discovered] == "" else singleSet[i_Discovered]
		detection_type = "" if singleSet[i_Detection_Type] == "" else singleSet[i_Detection_Type]
		molecules = "" if singleSet[i_Molecules] == "" else singleSet[i_Molecules]
		star_name = "" if singleSet[i_Star_Name] == "" else singleSet[i_Star_Name]
		star_distance = 0.0 if singleSet[i_Star_Distance] == "" else singleSet[i_Star_Distance]
		star_mass = 0.0 if singleSet[i_Star_Mass] == "" else singleSet[i_Star_Mass]
		star_radius = 0.0 if singleSet[i_Star_Radius] == "" else singleSet[i_Star_Radius]
		star_spec_type = "" if singleSet[i_Star_Spec_Type] == "" else singleSet[i_Star_Spec_Type]
		if singleSet[i_Star_Radius] == "":
			star_radius = pow(star_mass, 0.8)
		if (star_radius == 0.0) and (star_mass == 0.0):
			if star_spec_type.find("G0") != -1:
				star_radius = 1.05
				star_mass = 1.10
			if star_spec_type.find("G4") != -1:
				star_radius = 0.93
				star_mass = 0.93
			if star_spec_type.find("G8") != -1:
				star_radius = 0.98
				star_mass = 0.98
			if star_spec_type.find("K0") != -1:
				star_radius = 0.85
				star_mass = 0.78
		star_age = 0.0 if singleSet[i_Star_Age] == "" else singleSet[i_Star_Age]
		star_teff = 0.0 if singleSet[i_Star_Teff] == "" else singleSet[i_Star_Teff]
		insertPlanetQuery = "insert into exoplanets(name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("
		insertPlanetQuery += "\""+name+"\","+str(mass)+","+str(radius)+","+str(period)+","+str(axis)+","+str(eccentricity)+","+str(inclination)+","+str(discovered)+","+"\""+detection_type+"\",\""+molecules+"\",\""+star_name+"\","+str(star_distance)+","+str(star_mass)+","+str(star_radius)+",\""+star_spec_type+"\","+str(star_age)+", 0.0, 1.0, 24.0);"
		insertList.append(insertPlanetQuery)

insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Mercury", 0.0001738, 0.03412, 88.0, 0.3871, 0.206, 0.0, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 58.65, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Venus", 0.00256585, 0.08645, 225, 0.7233, 0.007, 177.3, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, -243.00, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Earth", 0.003145, 0.08921, 365, 1.0, 0.017, 23.4, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 1.0, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Mars", 0.00033825, 0.047501, 687, 1.5273, 0.093, 25.2, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 1.03, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Jupiter", 1, 1, 4331, 5.2028, 0.048, 3.1, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 0.41, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Saturn", 0.29926, 0.843, 10747, 9.5388, 0.056, 26.7, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 0.44, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Uranus", 0.04573, 0.357508, 30589, 19.1914, 0.046, 97.9, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, -0.72, 24.27);')
insertList.append('insert into exoplanets (name, mass, radius, period, axis, eccentricity, inclination, discovered, detection_type, molecules, star_name, star_distance, star_mass, star_radius, star_spec_type, star_age, star_teff, rotation, star_rotation) values("Neptune", 0.05374, 0.34638, 59800, 30.0611, 0.010, 29.6, "", "", "", "The Sun", 0.0, 1.0, 1.0, "G2", 18.4, 0.0, 0.72, 24.27);')
for insert in insertList:
	#continue
	print insert
	c.execute(insert)
print len(starList)
conn.commit()
conn.close()
