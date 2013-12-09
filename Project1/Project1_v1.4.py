#--------------------------------------------------
#	Project 1
#	CS 526, Computer Graphiccs II
#	University of Illinois at Chicago
#
#	Author: Giric Goyal
#
#--------------------------------------------------

# imports
from math import *
from euclid import *
from omega import *
from cyclops import *
from datetime import datetime
from src import input
from src import util
from src import menuManager
from src import guiManager
from src import cameraManager
from src import manageData

import urllib2
import csv
from xml.dom import minidom

# python utm converter from https://pypi.python.org/pypi/utm
from lib import utm
from tools.geom import geom
#from lib import pykml


#-------------------------------------------------------------------------------------------
# method definitons

# Crime methods -----------------------------------------------------------------------------

def load(crimeSet):
	global geomModel
	for crime in crimeSet:
		c1 = Color(crime.color)
		geomModel.addVertex(Vector3(crime.x, crime.y,0))
		geomModel.addColor(c1)
	geomModel.addPrimitive(PrimitiveType.Points, 0, len(crimeSet))
	
def manageCrimeData():
	addCrimeData() if util.isCrimeEnabled == True else removeCrimeData()

def addCrimeData():
	#scene.addModel(geomModel)
	print "Reading from database"
	crimeSet = []
	lon = 0.0
	lat = 0.0
	type = ""
	color = ""
	for rawData in manageData.getCrimeData():
		if (rawData[0] != "" and rawData[1] != "" and rawData[2] != ""):
			#print rawData
			lon = rawData[0]
			lat = rawData[1]
			type = rawData[2].lower()
			if type == "assault":
				color = "#EE121299"
			elif type == "battery":
				color = "#1aEF1299"
			elif type == "burglary":
				color = "#1111FE99"
			else:
				color = "#000000FF"
			position = utm.from_latlon(lat, lon)
			tempObj = util.MyCrime(util.selectedCrime, position[0], position[1], color, util.selectedYear)
			crimeSet.append(tempObj)
			
	print len(crimeSet)
	load(crimeSet)
	print "geoms added"
	
					
def removeCrimeData():
	print "clearing"
	global geomModel
	geomModel.clear()

def addAndRemoveData():
	if util.isCrimeEnabled == True:
		removeCrimeData()
		addCrimeData()
	if util.isCrimeCountOn == True:
		removeCrimeCount()
		addCrimeCount()

def manageCrimeCount():
	addCrimeCount() if util.isCrimeCountOn == True else removeCrimeCount()
	
def addCrimeCount():
	print "Adding crime count"
	cameraManager.set2DCamera()
	util.isBoundaryOn = True
	util.isCrimeEnabled = False
	manageCrimeData()
	manageCommunities()
	
def removeCrimeCount():
	print "Removing Crime count"
	removeCommunityBoundaries()

def updateTime():
	print "Updating Time"
	print str(util.selectedMonth)+"/"+str(util.selectedDate)+"/"+str(util.selectedYear)+" "+str(util.selectedHour)+":"+str(util.selectedMin)+":"+str(util.selectedP)
	removeCrimeData()
	manageCrimeData()
	
def showRealTime(dtObj):
	removeCrimeData()
	print "showing real time"
	print "Reading from database"
	crimeSet = []
	lon = 0.0
	lat = 0.0
	for rawData in manageData.getRealTimeData(dtObj):
		#print rawDatal
		lon = rawData[0]
		lat = rawData[1]
		position = utm.from_latlon(lat, lon)
		tempObj = util.MyCrime(util.selectedCrime, position[0], position[1], "#FF000088", util.selectedYear)
		crimeSet.append(tempObj)
	print len(crimeSet)
	load(crimeSet)
	
def removeRealTime():
	print "removing real time"
	
def manageRealTime():
	showRealTime() if util.isRealTimeEnabled == True else removeRealTime()
	
# Community methods ------------------------------------------------------------------	
def addCommunityNames():
	for data in manageData.getCommunityLocations():
		name = data[0]
		number = data[1]
		lon = data[2]
		lat = data[3]
		pos = utm.from_latlon(float(lat), float(lon))
		t = Text3D.create('fonts/arial.ttf', 150, str(name))
		t.setPosition(Vector3(float(pos[0]), float(pos[1]), 500))
		t.setFontResolution(1000)
		t.setColor(Color('Black'))
		all.addChild(t)

def addCommunityBoundaries(show,countList):
	print "Adding community data "
	name = ""
	coord = ""
	lat = []
	lon = []
	areaNum = 0
	dataList = manageData.getCommunityData()
	max = 0
	min = 10000
	for a in countList:
		if a[1] >= max:
			max = a[1]
		if a[1] <= min:
			min = a[1]
	for data in dataList:
		name = data[0]
		coordTemp = data[1].strip().split(",")
		areaNum = data[2]
		coord = data[3].strip().split(",")
		lat = []
		lon = []
		value = 0
		colorVar = ""
		for element in countList:
			if element[0].lower() == str(name).lower():
				value = element[1]
				break
		colorVar = util.getColor(max, value, min)
		print name + " : " + str(areaNum)
		line = LineSet.create()
		t = Text3D.create('fonts/arial.ttf', 150, str(name))
		if show == True:
			t = Text3D.create('fonts/arial.ttf', 150, str(name)+"\n"+str(value))
					
		pos = utm.from_latlon(float(coord[1]), float(coord[0]))
		t.setPosition(Vector3(float(pos[0]), float(pos[1]), 100))
		t.setFontResolution(100)
		t.setColor(Color('red'))
		all.addChild(t)
		communityDataList.append(t)
		i = 3
		while i <len(coordTemp):
			lat1 = float(coordTemp[i-2])
			lon1 = float(coordTemp[i-3])
			lat2 = float(coordTemp[i])
			lon2 = float(coordTemp[i-1])
			if (lat1 != lat2) or (lon1 != lon2):
				position1 = utm.from_latlon(lat1, lon1)
				position2 = utm.from_latlon(lat2, lon2)
				l = line.addLine()
				l.setStart(Vector3(float(position1[0]), float(position1[1]), 0))
				l.setEnd(Vector3(float(position2[0]), float(position2[1]), 0))
				l.setThickness(45)
				line.getMaterial().setColor(Color(colorVar),Color(colorVar))
				line.getMaterial().setLit(True)
				#line.setEffect("colored -d #88881188")
				all.addChild(line)
				communityDataList.append(line)
			i += 2
	print "Boundaries added"

def removeCommunityBoundaries():
	print "removing boundaries"
	for c in communityDataList:
		all.removeChildByRef(c)
	while len(communityDataList) > 0:
		communityDataList.pop()
		

def manageCommunities():
	if util.isCrimeCountOn == False:
		addCommunityBoundaries(False,manageData.getCrimeCount()) if util.isBoundaryOn == True else removeCommunityBoundaries()
	else:
		addCommunityBoundaries(True,manageData.getCrimeCount()) if util.isBoundaryOn == True else removeCommunityBoundaries()

def jumpToCommunity():
	#util.isBoundaryOn = True
	#manageCommunities()
	#cameraManager.set2DCamera()
	print util.selectedComm
	name = ""
	number = ""
	coord = ""
	for data in manageData.getCommunityLocationByName():
		name = data[0]
		number = data[1]
		lon = data[2]
		lat = data[3]
		position = utm.from_latlon(float(lat), float(lon))
		print position
		cameraManager.jumpToComm(Vector3(float(position[0]), float(position[1]), 0))
		

def overView():
	cameraManager.set3DCamera()
				
				
				
# CTA methods -----------------------------------------------------------------------------------------				
def manageCTAData():
	addCTAData() if util.isCTAEnabled == True else removeCTAData()
	
	
def addCTAData():
	print "adding CTA data"
	addCTAStationsData()
	addCTALinesData()
	getRealTimeCTA()
	
	
def removeCTAData():
	print "removing CTA data"
	for cta in CTADataNodeList:
		all.removeChildByRef(cta)
	while len(CTADataNodeList) > 0:
		CTADataNodeList.pop()
	
def addCTAStationsData():
	print "adding CTA station data"
	readFile = open(railStationKMLFile)
	stationName = ""
	lat = ""
	lon = ""
	elev = ""
	color = ""
	for data in (raw.strip().split("\t") for raw in readFile):
		stationName = data[0]
		lon = data[1].strip().split(",")[0]
		lat = data[1].strip().split(",")[1]
		elev = data[1].strip().split(",")[2]
		color = data[2]
		#print stationName + " : " + lat + " : " + lon + " : " + elev + " : " + color
		position = utm.from_latlon(float(lat), float(lon))
		station = BoxShape.create(40,40,40)
		station.setPosition(Vector3(float(position[0]), float(position[1]), 0))
		station.setEffect('colored -d gray')
		station.getMaterial().setColor(Color('#89898989'), Color('#89898900'))
		all.addChild(station)
		CTADataNodeList.append(station)
	print "CTA station Data Added"
		
		
def addCTALinesData():
	print "adding CTA line data"
	readFile = open(railLineKMLFile)
	lineName = ""
	lat = []
	lon = []
	elev = []
	for data in (raw.strip().split("\t") for raw in readFile):
		lineName = data[0].strip().split(",")
		flag = 0
		coord = data[1].strip().split(" ")
		lat = []
		lon = []
		elev = []
		for tri in (temp.strip().split(",") for temp in coord):
			lon.append(tri[0])
			lat.append(tri[1])
			elev.append(tri[2])
		#print lineName + " : " + color + " : " + str(len(lon)) + " : " + str(len(lat))
		line = LineSet.create()
		for tempLine in lineName:
			tempLine = tempLine.strip()
			#print tempLine
			if tempLine == " ":
				#print "------------------------------"
				pass
			elif tempLine == "\n":
				#print "------------------------------"
				pass
			elif tempLine == "":
				#print "-----------------------------------"
				pass
			else:
				color = ""
				if tempLine == "Brown":
					color = "#A63E0078"
				elif tempLine == "Pink":
					color = "#D5006588" 
				elif tempLine == "Red":
					color = "#AA000078"
				elif tempLine == "Purple":
					color = "#9303A777"
				elif tempLine == "Blue":
					color = "#0000AA88"
				elif tempLine == "Orange":
					color = "#FF620088"
				elif tempLine == "Green":
					color = "#00AA0088"
				elif tempLine == "Yellow":
					color = "#FFFF0088"
				#print color
				for i in range(1,len(lon)):
					position1 = utm.from_latlon(float(lat[i-1]), float(lon[i-1]))
					position2 = utm.from_latlon(float(lat[i]), float(lon[i]))
					l = line.addLine()
					l.setStart(Vector3(float(position1[0]), float(position1[1]), 0))
					l.setEnd(Vector3(float(position2[0]), float(position2[1]),0))
					l.setThickness(40)
					line.getMaterial().setColor(Color(color), Color(color))
					line.getMaterial().setTransparent(True)
					#line.setEffect("colored -d "+color)
					all.addChild(line)
					CTADataNodeList.append(line)
	print "CTA line data added"
		

def getRealTimeCTA():
	print "adding real time trains"
	trainSet = []
	for lineColor in line:
		f = urllib2.urlopen(url+"?key="+key+"&rt="+lineColor)
		#writeToFile = open("data/chicago_data/cta_data/CTATrainData.xml", "w")
		lat = []
		lon = []
		for text in (raw.strip().split("<") for raw in f):
			for l in text:
				if "/lat>" in l:
					pass
				elif "/lon>" in l:
					pass
				elif "lat>" in l:
					lat.append(l[l.index(">")+1:])
				elif "lon>" in l:
					lon.append(l[l.index(">")+1:])
		for i in range(0,len(lat)):
			position = utm.from_latlon(float(lat[i]), float(lon[i]))
			tempObj = util.MyTrain(float(position[0]), float(position[1]), "#00000089")
			trainSet.append(tempObj)
			CTATrainList[i].setPosition(Vector3(float(position[0]), float(position[1]), 15))
	#load(trainSet, trainGeomModel)
	

# -------------------------------------------------------------------------------

def getSysDateTime():
	time = datetime.now().time()
	date = datetime.now().date()
	obj = util.SysDateTime(date, time)
	return obj
	
def onUpdate(frame, t, dt):
	if util.isRealTimeEnabled == True:
		dtObj = getSysDateTime()
		showRealTime(dtObj)
		
	
#	if util.isCTAEnabled == True:
#		if int(t)%2 ==0:
#			#print "removing trains"
#			for tempData in CTATrainList:
#				all.removeChildByRef(tempData)
#			while len(CTATrainList) > 0:
#				CTATrainList.pop()
	if util.isCTAEnabled == True:
#		if int(t)%1 == 0:
		#trainGeomModel.clear()
		getRealTimeCTA()
	else:
		for ctaTrain in CTATrainList:
			ctaTrain.setPosition(Vector3(0,0,-1000))
			
	
#------------------------------------------------------------------------
# main variables and statements

scene = getSceneManager()

# initialize Menu
#guiManager.initialize()
print "Gui initialized"

# set background to black
scene.setBackgroundColor(Color(0, 0, 0, 1))

#skybox = Skybox()
#skybox.loadCubeMap("data/skybox","jpg")
#scene.setSkyBox(skybox)

#initialize db
manageData.__init__()

# initializing Geom
global geomModel
geomModel = ModelGeometry.create('geoms')
scene.addModel(geomModel)
trainGeomModel = ModelGeometry.create('geomsTrain')
scene.addModel(trainGeomModel)
# create the geom shader
geomProgram = ProgramAsset()
geomProgram.name = "geoms"
geomProgram.vertexShaderName = "tools/geom/geom.vert"
geomProgram.fragmentShaderName = "tools/geom/geom.frag"
geomProgram.geometryShaderName = "tools/geom/geom.geom"
geomProgram.geometryOutVertices = 4
geomProgram.geometryInput = PrimitiveType.Points
geomProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(geomProgram)
# create the geoms
sky = StaticObject.create('geoms')
sky.getMaterial().setProgram('geoms')
sky.getMaterial().setTransparent(False)
sky.getMaterial().setAdditive(True)
sky.getMaterial().setDepthTestEnabled(True)
	
# Create a directional light  
print "\n---Creating lighting"                                                      
util.light1 = Light.create()
util.light1.setLightType(LightType.Directional)
util.light1.setLightDirection(Vector3(-1.0, -1.0, -1.0))
util.light1.setColor(Color(0.5, 0.5, 0.5, 0.5))
util.light1.setAmbient(Color(0.2, 0.2, 0.2, 1.0))
util.light1.setEnabled(True)

# Load a static osgearth 'model'
print "\n---Loading city models"
cityModel1 = ModelInfo()
cityModel1.name = "city1"
cityModel1.path = "data/map_data/chicago_yahoo.earth"
scene.loadModel(cityModel1)

# Create a scene object using the loaded model
util.city1 = StaticObject.create("city1")
util.city1.getMaterial().setLit(False)

setNearFarZ(1, 2 * util.city1.getBoundRadius())

# add another version with a different type of map
cityModel2 = ModelInfo()
cityModel2.name = "city2"
cityModel2.path = "data/map_data/chicago_flat.sat.earth"
scene.loadModel(cityModel2)

# Create a scene object using the second loaded model
util.city2 = StaticObject.create("city2")
util.city2.getMaterial().setLit(False)

# add another version with a different type of map
cityModel3 = ModelInfo()
cityModel3.name = "city3"
cityModel3.path = "data/map_data/chicago_flat.map.earth"
scene.loadModel(cityModel3)

# Create a scene object using the third loaded model
util.city3 = StaticObject.create("city3")
util.city3.getMaterial().setLit(False)

# deal with the camera
print "\n---Setting Camera"
cameraManager.set3DCamera()

# set up the scene
all = SceneNode.create("everything")
all.addChild(util.city1)
all.addChild(util.city2)
all.addChild(util.city3)

# Turn off two/three maps
util.city1.setVisible(False)
util.city2.setVisible(False)
#util.city3.setVisible(False)

# initialize model for crime pointer
print "\n---Creating pointer models"
#mi = ModelInfo()
#mi.name = "defaultSphere"
#mi.path = "data/models/sphere.obj"
#scene.loadModel(mi)
			
# set EventFunction to handle Event		
setEventFunction(input.handleEvent)
setUpdateFunction(onUpdate)


#show all crime data initially
addCommunityNames()
addCrimeData()


# CTA ----------------------------------------------------------

url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
key = "8ee032a56ad14a28826c5edeaf5dbde3"
line = ["red", "blue", "brn", "g", "org", "p", "pink", "y"]
railLineKMLFile = "data/chicago_data/cta_data/CTARailLinesParsed.txt"
railStationKMLFile = "data/chicago_data/cta_data/CTARailStationsParsed.txt"
CTADataNodeList = []
CTATrainList = []

# Community Data -----------------------------------------------------------------------
communityDataFilePath = "data/chicago_data/community_data/communityData.txt"
communityJumpFilePath = "data/chicago_data/community_data/communityLocation.txt"
readFile = open(communityDataFilePath)
readJumpFile = open(communityJumpFilePath)
communityDataList = []


# --------------------------------------------------------------------
for i in range (1, 2500):
	ball = SphereShape.create(30,1)
	ball.setPosition(Vector3(0, 0, -1000))
	ball.setEffect('colored -d black')
	all.addChild(ball)
	CTATrainList.append(ball)
