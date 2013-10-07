from sqlite3 import *

from math import *

#------------------------------------------------
# variables

conn = connect('project2.db')
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
rotation = 0.0
star_rotation = 0.0
systemName = ""
isStar = 1
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
i_Rotation = 17
i_Star_Rotation = 18

starList = ["HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "XO-3", "Kepler-22", "MOA-2007-BLG-192-L", "Kepler-11", "Kepler-10", "GJ 1214", "GL 581", "WASP-33", "30 Ari B", "Kepler-39", "HR 8799", "Kepler-65", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "GL 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]
c.execute("drop table objects")
createTableQuery = "create table if not exists objects (name text, radius real, mass real, period real, rotation real, axis_distance real, eccentricity real, inclination real, discovered_age int, detection_type text, molecules_starType text, isStar int, system_name text)"
c.execute(createTableQuery)
# ----------------------------------------------------------------
# method definitions
list = []

readFromFile = "Select * from exoplanets"
rawDataSet = c.execute(readFromFile)
for singleSet in rawDataSet:
	name = singleSet[i_Name]
	mass = singleSet[i_Mass]
	radius = singleSet[i_Radius]
	period = singleSet[i_Period]
	axis = singleSet[i_Axis]
	eccentricity = singleSet[i_Eccentricity]
	inclination = singleSet[i_Inclination]
	discovered = singleSet[i_Discovered]
	detection_type = singleSet[i_Detection_Type]
	molecules = singleSet[i_Molecules]
	star_name = singleSet[i_Star_Name]
	star_distance = singleSet[i_Star_Distance]
	star_mass = singleSet[i_Star_Mass]
	star_radius = singleSet[i_Star_Radius]
	star_spec_type = singleSet[i_Star_Spec_Type]
	star_age = singleSet[i_Star_Age]
	star_teff = singleSet[i_Star_Teff]
	rotation = singleSet[i_Rotation]
	star_rotation = singleSet[i_Star_Rotation]
	isStar = 0
	if star_name == "The Sun":
		systemName = "Solar System"
		discovered = 0
	else:
		systemName = star_name
	insertQuery = 'insert into objects values("'+name+'",'+str(radius)+','+str(mass)+','+str(period)+','+str(rotation)+','+str(axis)+','+str(eccentricity)+','+str(inclination)+','+str(discovered)+',"'+detection_type+'","'+molecules+'",'+str(isStar)+',"'+systemName+'")'
	list.append(insertQuery)
	
	
readFromFile = "select * from exoplanets group by star_name"
rawDataSet = c.execute(readFromFile)
for singleSet in rawDataSet:
	name = singleSet[i_Name]
	mass = singleSet[i_Mass]
	radius = singleSet[i_Radius]
	period = singleSet[i_Period]
	axis = singleSet[i_Axis]
	eccentricity = singleSet[i_Eccentricity]
	inclination = singleSet[i_Inclination]
	discovered = singleSet[i_Discovered]
	detection_type = singleSet[i_Detection_Type]
	molecules = singleSet[i_Molecules]
	star_name = singleSet[i_Star_Name]
	star_distance = singleSet[i_Star_Distance]
	star_mass = singleSet[i_Star_Mass]
	star_radius = singleSet[i_Star_Radius]
	star_spec_type = singleSet[i_Star_Spec_Type]
	star_age = singleSet[i_Star_Age]
	star_teff = singleSet[i_Star_Teff]
	rotation = singleSet[i_Rotation]
	star_rotation = singleSet[i_Star_Rotation]
	isStar = 1
	if star_name == "The Sun":
		systemName = "Solar System"
		discovered = 0
		inclination = 7.5
	else:
		systemName = star_name
		inclination = 0.0
	insertQuery = 'insert into objects values("'+star_name+'",'+str(star_radius)+','+str(star_mass)+',0.0,'+str(star_rotation)+','+str(star_distance)+',0.0,'+str(inclination)+','+str(star_age)+',"","'+str(star_spec_type)+'",'+str(isStar)+',"'+systemName+'")'
	list.append(insertQuery)
	
for x in list:
	print x
	c.execute(x)
print len(list)
	
conn.commit()
conn.close()