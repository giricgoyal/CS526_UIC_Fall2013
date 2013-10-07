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
from src import input
from src import util
import csv
from src import menuManager
from src import guiManager
from src import cameraManager
import urllib2
from xml.dom import minidom

# python utm converter from https://pypi.python.org/pypi/utm
from lib import utm
#from lib import pykml


markerList = []

#-------------------------------------------------------------------------------------------
# method definitons
def manageCrimeData():
	addCrimeData() if util.isCrimeEnabled == True else removeCrimeData()
	
def addCrimeData():
	print "\n---Reading data from file"
	dataFile = "data/chicago_data/crime_data/"+util.selectedYear+"/" + util.selectedCrime.upper() + ".txt"
	print dataFile
	crimeData = open(dataFile, 'r')
	rawData = crimeData.read()
	counter = 0
	for row in (raw.strip().split("\t") for raw in rawData.split("\n")):
		counter += 1
		if counter == 1:
			pass
		else:
			if len(row) == 5:
				fullDateAsArray = row[0].strip().split(" ")
				util.time = fullDateAsArray[1] + " " + fullDateAsArray[2]
				dateAsArray = fullDateAsArray[0].strip().split("/")
				util.month = dateAsArray[0]
				util.date = dateAsArray[1]
				util.year = dateAsArray[2]
				util.lat = row[3]
				util.lon = row[4]
				util.type = row[2]
				util.block = row[1]
				#print "lat- " + str(util.lat) + " : lon- " + str(util.lon)
				print row[0] + " : " + row[1] + " : " + row[2] + " : " + row[3] + " : " + row[4]
				position = utm.from_latlon(float(util.lat), float(util.lon))
				marker = SphereShape.create(30,2)
				##marker.getMaterial().setProgram('colored')
				##marker.getMaterial().setColor(Color('#00000070'),Color(1,1,1,1))
				##marker.getMaterial().setAlpha(0.5)
				#marker = StaticObject.create("defaultSphere")
				#marker.setScale(Vector3(70,70,70))
				marker.setPosition(Vector3(float(position[0]), float(position[1]), 0))
				marker.setEffect('colored -d #0f01a020')
				all.addChild(marker)
				markerList.append(marker)
		if counter >= 5000:
			break
	print len(markerList)
					
def removeCrimeData():
	for marker in markerList:
		all.removeChildByRef(marker)
	while len(markerList) > 0:
		markerList.pop()
	print "Nodes remaining : " + str(len(markerList))

def addAndRemoveData():
	removeCrimeData()
	addCrimeData()
#------------------------------------------------------------------------
# main variables and statements

scene = getSceneManager()

# initialize Menu
#guiManager.initialize()
print "Gui initialized"

# set background to black
scene.setBackgroundColor(Color(0, 0, 0, 1))

skybox = Skybox()
skybox.loadCubeMap("data/skybox","jpg")
scene.setSkyBox(skybox)

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

# initialize model for crime pointer
print "\n---Creating pointer models"
mi = ModelInfo()
mi.name = "defaultSphere"
mi.path = "data/models/sphere.obj"
scene.loadModel(mi)
	
			
# set EventFunction to handle Event		
setEventFunction(input.handleEvent)

#show all crime data initially
#addCrimeData()



# CTA ----------------------------------------------------------
# variables
url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
key = "8ee032a56ad14a28826c5edeaf5dbde3"
line = ["red", "blue", "brn", "g", "org", "p", "pink", "y"]
railLineKMLFile = "data/chicago_data/cta_data/CTARailLinesParsed.txt"
railStationKMLFile = "data/chicago_data/cta_data/CTARailStationsParsed.txt"
CTADataNodeList = []
CTATrainList = []

# --------------------------------------------------------------
# methods
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
		station = BoxShape.create(20,20,20)
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
					l.setThickness(20)
					line.getMaterial().setColor(Color(color), Color(color))
					#line.setEffect("colored -d "+color)
					all.addChild(line)
					CTADataNodeList.append(line)
	print "CTA line data added"
		

def getRealTimeCTA():
	print "adding real time trains"
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
			#train = BoxShape.create(10,10,10)
			#train.setPosition(Vector3(float(position[0]), float(position[1]), 0))
			#train.setEffect('colored -d black')
			#all.addChild(train)
			ball = SphereShape.create(10,1)
			ball.setPosition(Vector3(float(position[0]), float(position[1]), 15))
			ball.setEffect('colored -d black')
			all.addChild(ball)
			#CTATrainList.append(train)
			CTATrainList.append(ball)
	
		
# Community Data -----------------------------------------------------------------------
communityDataFilePath = "data/chicago_data/community_data/communityData.txt"
communityJumpFilePath = "data/chicago_data/community_data/communityLocation.txt"
readFile = open(communityDataFilePath)
readJumpFile = open(communityJumpFilePath)
communityDataList = []

def addCommunityBoundaries():
	print "Adding community data"
	name = ""
	coord = ""
	lat = []
	lon = []
	areaNum = ""
	for data in (raw.strip().split("\t") for raw in readFile):
		name = data[0]
		coordTemp = data[1].strip().split(",")
		areaNum = data[2]
		coord = data[3].strip().split(",")
		lat = []
		lon = []
		print name + " : " + areaNum
		line = LineSet.create()
		t = Text3D.create('fonts/arial.ttf', 144, name)
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
				l.setThickness(15)
				line.setEffect("colored -d red")
				all.addChild(line)
				communityDataList.append(line)
			i += 2
	print "Boundaries added"

def removeCommunityBoundaries():
	print "removing boundaries"
	for c in communityDataList:
		aal.removeChildByRef(c)
	while len(communityDataList) > 0:
		communityDataList.pop()
		

def manageCommunities():
	addCommunityBoundaries() if util.isBoundaryOn == True else removeCommunityBoundaries()
		

def onUpdate(frame, t, dt):
	if util.isCTAEnabled == True:
		if int(t)%2 ==0:
			#print "removing trains"
			for tempData in CTATrainList:
				all.removeChildByRef(tempData)
			while len(CTATrainList) > 0:
				CTATrainList.pop()
	if util.isCTAEnabled == True:
		if int(t)%1 == 0:
			getRealTimeCTA()
			

			

def jumpToCommunity():
	print util.selectedComm
	name = ""
	number = ""
	coord = ""
	for data in (raw.strip().split("\t") for raw in readJumpFile):
		name = data[0]
		number = data[1]
		coord = data[2]
		if name == util.selectedComm:
			lon = coord.strip().split(",")[0]
			lat = coord.strip().split(",")[1]
			position = utm.from_latlon(float(lat), float(lon))
			cameraManager.jumpToComm(Vector3(float(position[0]), float(position[1]), 2000.0))
			break
		

def overView():
	cameraManager.set3DCamera()
				
setUpdateFunction(onUpdate)
# --------------------------------------------------------------
# main
#addCommunityBoundaries()