#-------------------------------------------------------
#	util.py file for utility stuff
#-------------------------------------------------------
from math import *
from euclid import *
from omega import *
from cyclops import *

# -------------------------------------------------------------
# class definitions
# class for bodyOrbit data
class bodyOrbit:
	name = ""
	radius = 0.0
	minorA = 0.0
	majorA = 0.0
	eccentricity = 0.0
	inclination = 0.0
	period = 0.0
	rotation = 0.0
	starType = ""
	isStar = 0
	texture = ""
	
	# getter methods
	def __getitem__(self, name):
		return name
	def __getitem__(self, radius):
		return radius
	def __getitem__(self, minorA):
		return minorA
	def __getitem__(self, majorA):
		return majorA
	def __getitem__(self, eccentricity):
		return eccentricity
	def __getitem__(self, inclination):
		return inclination
	def __getitem__(self, period):
		return period
	def __getitem__(self, rotation):
		return rotation
	def __getitem__(self, starType):
		return starType
	def __getitem__(self, isStar):
		return isStar
	def __getitem__(self, texture):
		return texture
		
	# constructor
	def __init__(self, name, radius, majorA, eccentricity, inclination, period, rotation, starType, isStar):
		self.name = name
		if isStar == 0:
			self.radius = radius * rJupiter #kms
			self.period = period * DAYtoYEAR #years
		else:
			self.radius = radius * rSun #kms
			self.period = 1.0 #years
		self.majorA = majorA * AUtoKM #kms
		self.eccentricity = eccentricity
		self.inclination = inclination
		self.rotation = rotation #days
		self.starType = starType
		self.minorA = getOrbitCoords(eccentricity, majorA) * AUtoKM #kms
		self.isStar = isStar
		
		

class bodyInfo:
	name = ""
	mass = ""
	discovered = 0
	detectionType = ""
	molecules = ""
	isStar = 0
	systemName = ""
	starDistance = 0.0
	starAge = 0.0
	starType = ""
	
	# getter functions
	def __getitem__(self, name):
		return name
	def __getitem__(self, mass):
		return mass
	def __getitem__(self, discovered):
		return discovered
	def __getitem__(self, detectionType):
		return detectionType
	def __getitem__(self, molecules):
		return molecules
	def __getitem__(self, isStar):
		return isStar
	def __getitem__(self, systemName):
		return systemName
	def __getitem__(self, starDistance):
		return starDistance
	def __getitem__(self, starAge):
		return starAge
	def __getitem__(self, starType):
		return starType
	
	# constructor
	def __init__(self, name, mass, discovered, detectionType, molecules, systemName, starDistance, starAge, starType, isStar):
		self.name = name
		if isStar == 0:
			self.mass = str(mass) + "Jupiter Mass"	# Jupiter mass
		else:
			self.mass = str(mass) + "Sun Mass" # Sun Mass
		self.discovered = discovered
		self.detectionType = detectionType
		self.molecules = molecules
		self.isStar = isStar
		self.starType = starType
		self.systemName = systemName
		self.starDistance = starDistance #parsecs
		self.starAge = starAge #Galactic Year
		
		
class habZone:
	starName = ""
	starType = ""
	habInner = 0.0
	habOuter = 0.0
	habCenter = 0.0
	
	def __getitem__(self, starName):
		return starName
	def __getitem__(self, statType):
		return starType
	def __getitem__(self, habInner):
		return habInner
	def __getitem__(self, habOuter):
		return habOuter
	def __getitem__(self, habCenter):
		return habCenter
	
	def __init__(self, starName, starType):
		self.starName = starName
		self.starType = starType
	
	def calHabitableZone(self):
		if self.starType.find('A') != -1:	
			self.habInner = 8.5 * AUtoKM
			self.habOuter = 12.5 * AUtoKM
		elif self.starType.find('F') != -1:
			self.habInner = 1.5 * AUtoKM
			self.habOuter = 2.2 * AUtoKM
		elif self.starType.find('G') != -1:
			self.habInner = 0.95 * AUtoKM
			self.habOuter = 1.4 * AUtoKM
		elif self.starType.find('K') != -1:
			self.habInner = 0.38 * AUtoKM
			self.habOuter = 0.56 * AUtoKM
		elif self.starType.find('M') != -1:
			self.habInner = 0.08 * AUtoKM
			self.habOuter = 0.12 * AUtoKM
		else:
			self.habInner = 0.0
			self.habOuter = 0.0
			
		self.habCenter = (self.habInner + self.habOuter) * 0.5

		
class starLoc:
	alpha = 0.0 # right ascension in hh:mm:ss convert to degrees
	delta = 0.0 # declination in dd:mm:ss convert to degrees
	distance = 0.0 # distance to star from earth
	pos = Vector3(0.0,0.0,0.0)
	name = ""
	
	def __getitem__(self, pos):
		return pos
	def __getitem__(self, name):
		return name
	
	def __init__(self, name, a, d, dist):
		self.name = name
		ahr = 0.0
		amin = 0.0
		asec = 0.0
		dday = 0.0
		dmin = 0.0
		dsec = 0.0
		part = a.strip().split(":")
		ahr = part[0]
		amin = part[1]
		asec = part[2]
		part = d.strip().split(":")
		sign = part[0][0]
		dday = part[0][1:]
		dmin = part[1]
		dsec = part[2]
		if sign == "-":
			dday = -(float(dday))
			dmin = -(float(dmin))
			dsec = -(float(dsec))
		self.alpha = (float(ahr) * float(HRtoDEG)) + (float(amin) * float(MINtoDEG)) + (float(asec) * float(SECtoDEG))
		self.delta = (float(dday) * float(DAYtoDEG)) + (float(dmin) * float(MINtoDEG)) + (float(dsec) * float(SECtoDEG))
		self.distance = dist
		x = float(self.distance) * float(cos(radians(self.alpha))) * float(cos(radians(self.delta)))
		y = float(self.distance) * float(cos(radians(self.delta))) * float(sin(radians(self.alpha)))
		z = float(self.distance) * float(sin(radians(self.delta)))
		self.pos = Vector3(x * PCtoKM, y * PCtoKM, z * PCtoKM)
		
		
		
# ------------------------------------------------------------------			
# variables
mSun = "1.989E30 kg"

rSun = 695500 # km
rJupiter = 71493.5 # Km
rEarth = 6378 #km

# conversions
AUtoKM = 149597871
PCtoKM = 3.08567e13
HRtoDEG = 15.0
DAYtoDEG = 24.0 * HRtoDEG
MINtoDEG = 15.0/60.0
SECtoDEG = 15.0/3600.0


# computer goldilocks zone based on the type of star
# for now setting to the Sun
habInner = 0.95 * AUtoKM
habOuter = 1.4 * AUtoKM
habCenter = 0.5 * (habInner + habOuter)


wallLimit = 400000000

# scaling
#scale factor for 3d system in the cave
userScaleFactor = 4
# 4 for kepler 11
# 1 for sol

#scale factor for the systems on the walls
user2ScaleFactor = 1
# 30 for kepler 11

orbitScaleFactor = 0.00001
planetScaleFactor = 0.01
sunScaleFactor = 0.001
overallScaleFactor = 0.00025

XorbitScaleFactor = 320000.0 / wallLimit
XplanetScaleFactor = 0.2

# time 
DAYtoYEAR = 1.0/365.0

# data variables
allSystemsOrbital = dict()
allSystemsInfo = dict()
#systemList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "XO-3", "Kepler-22", "MOA-2007-BLG-192-L", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "WASP-33", "30 Ari B", "Kepler-39", "HR 8799", "Kepler-65", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]
systemList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "Kepler-22", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "30 Ari B", "Kepler-39", "HR 8799", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]
activeSystem = None
activeBodies = dict()
activeRotCenters = dict()
habitableZones = dict()
starLocations = dict()

# Colors
colorBlack = Color("#000000FF") # Black
colorWhite = Color("#FFFFFFFF") # white
# starColors
colorO = Color("#3E94D1EE") # blue
colorB = Color("#A5E5FFEE") # deep blue white
colorA = Color("#CAF0FFEE") # blue white
colorF = Color("#FFFFFFEE") # white
colorG = Color("#FFEFC0EE") # yellowish white
colorK = Color("#FFD36BEE") # pale yellow orange
colorM = Color("#FFBF86EE") # yellow orange red




# -----------------------------------------------------------------
# method definitions
# get length of semi major axis using eccentricity and semi major axis
def getOrbitCoords(e, a):
	ra = (1.0 + e) * a
	rp = (1.0 - e) * a
	b = pow((ra*rp), 0.5)
	return b
		
