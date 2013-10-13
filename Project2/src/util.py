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
		if isStar == 1:
			if name == "The Sun":
				self.texture = "data/textures/stars/sol.png"
			if starType.find('A') != -1:
				self.texture = "data/textures/stars/astar.jpg"
			elif starType.find('B') != -1:
				self.texture = "data/textures/stars/bstar.png"
			elif starType.find('G') != -1:
				self.texture = "data/textures/stars/gstar.png"
			elif starType.find('K') != -1:
				self.texture = "data/textures/stars/kstar.png"
			elif starType.find('F') != -1:
				self.texture = "data/textures/stars/fstar.png"
			elif starType.find('M') != -1:
				self.texture = "data/textures/stars/mstar.png"
			elif starType.find('O') != -1:
				self.texture = "data/textures/stars/ostar.png"
		else:
			if name == "Mercury":
				self.texture = "data/textures/planets/mercury.jpg"
			elif name == "Venus":
				self.texture = "data/textures/planets/venus.jpg"
			elif name == "Earth":
				self.texture = "data/textures/planets/earth.jpg"
			elif name == "Mars":
				self.texture = "data/textures/planets/mars.jpg"
			elif name == "Jupiter":
				self.texture = "data/textures/planets/jupiter.jpg"
			elif name == "Saturn":
				self.texture = "data/textures/planets/saturn.jpg"
			elif name == "Uranus":
				self.texture = "data/textures/planets/uranus.jpg"
			elif name == "Neptune":
				self.texture = "data/textures/planets/neptune.jpg"
			elif self.radius/rEarth > 15:
				self.texture = "data/textures/planets/jupiter.jpg"
			elif self.radius/rEarth > 6:
				self.texture = "data/textures/planets/jupiter.jpg"
			elif self.radius/rEarth > 2:
				self.texture = "data/textures/planets/neptune.jpg"
			elif self.radius/rEarth > 1.25:
				self.texture = "data/textures/planets/earth.jpg"
			else:
				self.texture = "data/textures/planets/earth.jpg"
				

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
		ahr = float(part[0])
		amin = float(part[1])
		asec = float(part[2])
		part = d.strip().split(":")
		sign = part[0][0]
		dday = float(part[0][1:])
		dmin = float(part[1])
		dsec = float(part[2])
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
starLocations = dict()

activeBodies = dict()
activeRotCenters = dict()
habitableZones = dict()
systemNodeDict = dict()
orbitDict = dict()
textDict = dict()
otherObjectsDict = dict()


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



currentSystem = "Solar System"




# setting up initial scene hierarchy
# level 1
allSystems = SceneNode.create('allSystems')

# level 2
universe = SceneNode.create('universe')
thingsOnTheWall = SceneNode.create('thingsOnTheWall')

# level 3
everything = SceneNode.create('everything')


# Camera Properties
camSpeed = 25


# -----------------------------------------------------------------
# method definitions
# get length of semi major axis using eccentricity and semi major axis

def initSceneNodes():
	for system in systemList:
		temp = SceneNode.create(system)
		systemNodeDict[system] = temp
	for system in systemList:
		universe.addChild(systemNodeDict[system])
	
	thingsOnTheWall.addChild(allSystems)
	everything.addChild(universe)
	everything.addChild(thingsOnTheWall)



def getOrbitCoords(e, a):
	ra = (1.0 + e) * a
	rp = (1.0 - e) * a
	b = pow((ra*rp), 0.5)
	return b

def resetSystem():
	global allSystems, universe, thinsOnTheWall, everything
	activeBodies = dict()
	activeRotCenters = dict()
	habitableZones = dict()
	systemNodeDict = dict()
	
	#everything.removeChildByRef(universe)

	# level 1
	allSystems = None
	allSystems = SceneNode.create('allSystems')

	# level 2
	universe = None
	thingsOnTheWall = None
	universe = SceneNode.create('universe')
	thingsOnTheWall = SceneNode.create('thingsOnTheWall')

	# level 3
	everything = None
	everything = SceneNode.create('everything')

	# initialize the scene nodes again
	initSceneNodes()


def updateOrbitScale(scale):
	global orbitScaleFactor
	orbitScaleFactor = pow(0.1, 9 - scale)

	for system in systemList:
		theSystem = allSystemsOrbital[system]
		for name, model in theSystem.iteritems():
			pos = ((Vector3(0.0, 0.0, -theSystem[name].minorA  * orbitScaleFactor * userScaleFactor)))
			pos2 = starLocations[system].pos  * orbitScaleFactor * userScaleFactor
			pos3 = theSystem[name].minorA*orbitScaleFactor*userScaleFactor
			if theSystem[name].isStar == 0:
				pos4 = Vector3(0, theSystem[name].radius * planetScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			else:
				pos4 = Vector3(0, theSystem[name].radius * sunScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			activeBodies[name].setPosition(pos)
			activeRotCenters[name].setPosition(pos2)
			orbitDict[name].setScale(Vector3(pos3, 10.0, pos3))
			textDict[name].setPosition(pos4)
			if name == "Saturn":
				otherObjectsDict[name].setPosition(pos)
	