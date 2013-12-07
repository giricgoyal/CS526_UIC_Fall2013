#-------------------------------------------------------
#	util.py file for utility stuff
#-------------------------------------------------------
from math import *
from euclid import *
from omega import *
from cyclops import *
from caveutil import *

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
	habWidth = 0.0
	
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
	def __getitem__(self, habWidth):
		return habWidth
	
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
		self.habWidth = self.habOuter - self.habInner

		
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
skyBox = None
scene = None

isCave = False
isMovingTile = False
show3DSystems = True
show2DSystems = False
showVisualization = True
showGraphs = True
enableSound = True


mSun = "1.989E30 kg"

rSun = 695500 # km
rJupiter = 71493.5 # Km
rEarth = 6378 #km

# conversions
AUtoKM = 149597871
PCtoKM = 3.08567e13
PCtoLY = 3.26163344
HRtoDEG = 15.0
DAYtoDEG = 24.0 * HRtoDEG
MINtoDEG = 15.0/60.0
SECtoDEG = 15.0/3600.0


# computer goldilocks zone based on the type of star
# for now setting to the Sun
habInner = 0.95 * AUtoKM
habOuter = 1.4 * AUtoKM
habCenter = 0.5 * (habInner + habOuter)


#wallLimit = 400000000
wallLimit = - 3 * 48000

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
visualizationScaleFactor = 0.00001
overallScaleFactor = 0.00025
timeFactor = 90

XorbitScaleFactor = 320000.0 / wallLimit
XplanetScaleFactor = 0.25


# time 
DAYtoYEAR = 1.0/365.0

# data variables
# Dictionaries
allSystemsOrbital = dict()
allSystemsInfo = dict()
starLocations = dict()
lightsDict = dict()


# Lists
#systemList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "XO-3", "Kepler-22", "MOA-2007-BLG-192-L", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "WASP-33", "30 Ari B", "Kepler-39", "HR 8799", "Kepler-65", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]

# all main list
systemList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "Kepler-22", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "30 Ari B", "Kepler-39", "HR 8799", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]

# nearest to earth list
nearestToEarthList = ["Solar System", "alf Cen B", "Gliese 876",  "HD 20794",  "Gl 581", "GJ 667C", "Fomalhaut", "61 Vir", "55 Cnc", "HD 69830", "HD 40307", "GJ 1214", "ups And", "47 Uma", "HD 136352", "Gl 163"]

# Earth like list
earthLikeList = ["Solar System", "HD 217107", "HD 20794", "GJ 667C", "HD 40307", "alf Cen B", "Kepler-11", "Kepler-10", "Gl 581", "HD 39194", "Kepler-42", "Kepler-20", "Kepler-68"]

# habitable List
habitableList = ["Solar System", "Gl 581", "Kepler-22", "Gl 163", "HD 40307"]

# sun like List
sunLikeList = ["Solar System", "mu Ara", "Kepler-75", "Kepler-68", "Kepler-22", "Kepler-20", "Kepler-11", "Kepler-10", "HD 96700", "HD 217107", "HD 209458", "HD 20794", "HD 20003", "HD 190360", "HD 142", "HD 136352", "HD 134987", "HD 134060", "HD 10180", "61 Vir", "47 Uma", "24 Sex", "ups And", "14 Her", "55 Cnc", "HD 128311", "HD 215152", "HD 39194", "HD 69830", "alf Cen B", "nu Oph"]

# user list
userList = ["Solar System", "HD 209458", "alf Cen B", "nu Oph", "Kepler-75", "ups And", "CoRoT-11", "Kepler-22", "Kepler-11", "Kepler-10", "GJ 1214", "Gl 581", "30 Ari B", "Kepler-39", "HR 8799", "Fomalhaut", "KOI-142", "HD 10180", "Kepler-68", "Kepler-20", "24 Sex", "Kepler-42", "HD 39194", "HD 134987", "HD 60532", "HD 96700", "HD 142", "HD 134060", "HD 215152", "HD 217107", "HD 99492", "GJ 676A", "HD 20794", "HD 128311", "14 Her", "HD 136352", "HD 113538", "HD 190360", "mu Ara", "47 Uma", "Gl 163", "Gliese 876", "55 Cnc", "HD 20003", "GJ 667C", "61 Vir", "HD 69830", "HD 40307"]

orientObjects = []

# current shown list
displaySystemList = systemList

# Variables
activeSystem = "Solar System"


# dicts to change when scaling 
activeBodies = dict()
activeRotCenters = dict() # do not scale these
habitableZones = dict()
systemNodeDict = dict()
orbitDict = dict()
textDict = dict()
otherObjectsDict = dict()
wallSystemsDict = dict()
wallSystemTextDict = dict()
visualizeDict = dict()
visualizeTextDict = dict()
habiInnerDict = dict()
habiOuterDict = dict()
habiWallDict = dict()
systemInfoDict = dict()
hitWallDict = dict()




# Colors
colorBlack = Color("#000000FF") # Black
colorWhite = Color("#FFFFFFFF") # white
# starColors
colorO = Color("#3E94D1AA") # blue
colorB = Color("#A5E5FFAA") # deep blue white
colorA = Color("#CAF0FFAA") # blue white
colorF = Color("#FFFFFFAA") # white
colorG = Color("#FFEFC0AA") # yellowish white
colorK = Color("#FFD36BAA") # pale yellow orange
colorM = Color("#FFBF86AA") # yellow orange red


currentSystem = "Solar System"

# setting up initial scene hierarchy
# level 1
allSystems = SceneNode.create('allSystems')
vizContainer = SceneNode.create('vizContainer')
graphContainer = SceneNode.create('graphContainer')

# level 2
universe = SceneNode.create('universe')
thingsOnTheWall = SceneNode.create('thingsOnTheWall')
visualization = SceneNode.create('visualization')
graph = SceneNode.create('graph')

# level 3
everything = SceneNode.create('everything')


# Camera Properties
camSpeed = 25

# Cave dependent scaling 
# font
fontSize = 0.04

# Visualization parameters
vizPos = Vector3(10000000000,10000000000,100000000000)

midWindowX = sin(5.25 * (36.0/360.0 * 2 * pi)) * 3.25
midWindowY = 3.5 * 0.29 + 0.41
midWindowW = 1
midWindowH = 1

# Graph Parameters
xLabel = "test"
yLabel = "test"

maxRadius = 0.0
maxDistFromStar = 0.0
maxPeriod = 0.0
maxEccentricity = 0.0
maxRotation = 0.0
maxInclination = 0.0
maxMass = 0.0

minRadius = 0.0
minDistFromStar = 0.0
minPeriod = 0.0
minEccentricity = 0.0
minRotation = 0.0
minInclination = 0.0
minMass = 0.0


CONSTANT_RADIUS = "Radius"
CONSTANT_DISTFROMSTAR = "Distfromstar"
CONSTANT_PERIOD = "Period"
CONSTANT_ECCENTRICITY = "Eccentricity"
CONSTANT_ROTATION = "Rotation"
CONSTANT_INCLINATION = "Inclination"
CONSTANT_MASS = "Mass"


# graph dict
planetRadiusDict = dict()
planetDistFromStarDict = dict()
planetPeriodDict = dict()
planetEccentricityDict = dict()
planetRotationDict = dict()
planetInclinationDict = dict()
planetMassDict = dict()

graphGlyphDict = dict()
graphGlyphLogDict = dict()

xAxisDict = dict()
yAxisDict = dict()

xAxisConstant = CONSTANT_DISTFROMSTAR
yAxisConstant = CONSTANT_PERIOD

planetList = []


# -----------------------------------------------------------------
# method definitions
# get length of semi major axis using eccentricity and semi major axis

def initSceneNodes():
	for system in systemList:
		temp = SceneNode.create(system)
		systemNodeDict[system] = temp
	for system in systemList:
		universe.addChild(systemNodeDict[system])
	
	graph.addChild(graphContainer)
	visualization.addChild(vizContainer)
	thingsOnTheWall.addChild(allSystems)
	everything.addChild(graph)
	everything.addChild(universe)
	everything.addChild(thingsOnTheWall)
	everything.addChild(visualization)

def starColor(star):
	if star.starType.find('A') != -1:
		return colorA
	elif star.starType.find('B') != -1:
		return colorB
	elif star.starType.find('G') != -1:
		return colorG
	elif star.starType.find('K') != -1:
		return colorK
	elif star.starType.find('F') != -1:
		return colorF
	elif star.starType.find('M') != -1:
		return colorM
	elif star.starType.find('O') != -1:
		return colorO


def getOrbitCoords(e, a):
	ra = (1.0 + e) * a
	rp = (1.0 - e) * a
	b = pow((ra*rp), 0.5)
	return b


def updateTimeFactor(factor):
	global timeFactor
	timeFactor = (9 - factor) * 10 if (9 - factor) != 0 else 1
	
def updateTextSize(factor):
	global fontSize
	fontSize = factor
	

def getTimeFactor():
	return timeFactor
	
def setActiveSystem(name):
	global activeSystem
	activeSystem = name
	
def getActiveSystem():
	return activeSystem
	
def findInList(object, list):
	for temp in list:
		if object.strip() == temp.strip():
			return True
	return False
			
def setDisplayList(listNo):
	global displaySystemList
	if listNo == 0: displaySystemList = systemList 
	elif listNo == 1: displaySystemList = nearestToEarthList
	elif listNo == 2: displaySystemList = earthLikeList
	elif listNo == 3: displaySystemList = habitableList
	elif listNo == 4: displaySystemList = sunLikeList
	elif listNo == 5: displaySystemList = userList
	
def getDisplayList():
	return displaySystemList
	
def getUserList():
	global userList
	return userList
	
def getScene():
	global scene
	return scene
	
def setIsMovingTile(val):
	global isMovingTile
	isMovingTile = val
	
def getIsMovingTile():
	global isMovingTile
	return isMovingTile


def createDictsForGraph():
	global planetRadiusDict, planetDistFromStarDict, planetPeriodDict, planetEccentricityDict, planetRotationDict, planetInclinationDict, planetMassDict
	global maxRadius, maxDistFromStar, maxPeriod, maxEccentricity, maxRotation, maxInclination, maxMass
	global planetList

	for system in systemList:
		systemOrbit = allSystemsOrbital[system]
		systemInfo = allSystemsInfo[system]
		systemLoc = starLocations[system]

		for name, model in systemOrbit.iteritems():
			if systemOrbit[name].isStar == 0:
				radius_Original = systemOrbit[name].radius * planetScaleFactor 
				distFromStar_Original = systemOrbit[name].minorA * userScaleFactor * orbitScaleFactor
				period_Original = systemOrbit[name].period
				eccentricity_Original = systemOrbit[name].eccentricity
				inclination_Original = systemOrbit[name].inclination
				rotation_Original = systemOrbit[name].rotation
				mass_Original = systemInfo[name].mass
				
				planetRadiusDict[name] = radius_Original
				planetDistFromStarDict[name] = distFromStar_Original
				planetPeriodDict[name] = period_Original
				planetEccentricityDict[name] = eccentricity_Original
				planetRotationDict[name] = rotation_Original
				planetInclinationDict[name] = inclination_Original
				planetMassDict[name] = mass_Original

				planetList.append(name)

	
	maxRadius = max(planetRadiusDict.values())
	minRadius = min(value for value in planetRadiusDict.values() if value > 0.0)
	planetRadiusDict['max'] = maxRadius
	planetRadiusDict['min'] = minRadius
	
	maxDistFromStar = max(planetDistFromStarDict.values())
	minDistFromStar = min(value for value in planetDistFromStarDict.values() if value > 0.0)
	planetDistFromStarDict['max'] = maxDistFromStar
	planetDistFromStarDict['min'] = minDistFromStar

	maxPeriod = max(planetPeriodDict.values())
	minPeriod = min(value for value in planetPeriodDict.values() if value > 0.0)
	planetPeriodDict['max'] = maxPeriod
	planetPeriodDict['min'] = minPeriod

	maxEccentricity = max(planetEccentricityDict.values())
	minEccentricity = min(value for value in planetEccentricityDict.values() if value > 0.0) 
	planetEccentricityDict['max'] = maxEccentricity
	planetEccentricityDict['min'] = minEccentricity

	maxRotation = max(planetRotationDict.values())
	minRotation = min(value for value in planetRotationDict.values() if value > 0.0)
	planetRotationDict['max'] = maxRotation
	planetRotationDict['min'] = minRotation

	maxInclination = max(planetInclinationDict.values())
	minInclination = min(value for value in planetInclinationDict.values() if value > 0.0)
	planetInclinationDict['max'] = maxInclination
	planetInclinationDict['min'] = minInclination

	maxMass = max(planetMassDict.values())
	minMass = min(value for value in planetMassDict.values() if value > 0.0)
	planetMassDict['max'] = maxMass
	planetMassDict['min'] = minMass

	global xAxisDict, yAxisDict

	xAxisDict = planetDistFromStarDict.copy()
	yAxisDict = planetDistFromStarDict.copy()


	print "planets added "




def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)



def getxAxisDict():
	global xAxisDict
	return xAxisDict

def getyAxisDict():
	global yAxisDict
	return yAxisDict


def checkInSolarSystem(planet):
	if planet == "Mercury":
		return True
	if planet == "Venus":
		return True
	if planet == "Earth":
		return True
	if planet == "Mars":
		return True
	if planet == "Jupiter":
		return True
	if planet == "Saturn":
		return True
	if planet == "Uranus":
		return True
	if planet == "Neptune":
		return True
	return False
