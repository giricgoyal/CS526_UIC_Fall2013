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
		self.radius = radius * rJupiter #kms
		self.majorA = majorA * AUtoKM #kms
		self.eccentricity = eccentricity
		self.inclination = inclination
		self.period = period * DAYtoYEAR #years
		self.rotation = rotation #days
		self.starType = starType
		self.minorA = getOrbitCoords(eccentricity, majorA) * AUtoKM #kms
		self.isStar = isStar
		
		

class bodyInfo:
	name = ""
	mass = 0.0
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
		self.mass = mass #Jupiter mass
		self.discovered = discovered
		self.detectionType = detectionType
		self.molecules = molecules
		self.isStar = isStar
		self.starType = starType
		self.systemName = systemName
		self.starDistance = starDistance #parsecs
		self.starAge = starAge #Galactic Year
	
# ------------------------------------------------------------------			
# variables
mSun = "1.989E30 kg"

rSun = 695500 # km
rJupiter = 71493.5 # Km
rEarth = 6378 #km

AUtoKM = 149597871

# computer goldilocks zone based on the type of star
# for now setting to the Sun
habInner = 0.95 * AUtoKM
habOuter = 1.4 * AUtoKM
habCenter = 0.5 * (habInner + habOuter)

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

# time 
DAYtoYEAR = 1/365

# data variables
allSystemsOrbital = dict()
allSystemsInfo = dict()
systemList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "XO-3", "Kepler-22", "MOA-2007-BLG-192-L", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "WASP-33", "30 Ari B", "Kepler-39", "HR 8799", "Kepler-65", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]

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
		
