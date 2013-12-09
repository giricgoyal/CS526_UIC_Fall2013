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

# python utm converter from https://pypi.python.org/pypi/utm
from lib import utm


#-------------------------------------------------------------------------------------------
# method definitons
def crimeData():
	print "\n---Reading data from file"
	for crime in util.selectedCrime:
		dataFile = "data\chicago_data\crime_data\\"+util.selectedYear+"\\" + crime.upper() + ".txt"
		print dataFile
		crimeData = open(dataFile, 'r')
		counter = 0
		for row in (rawData.strip().split("\t") for rawData in crimeData):
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
					print "lat- " + str(util.lat) + " : lon- " + str(util.lon)
					print row[0] + " : " + row[1] + " : " + row[2] + " : " + row[3] + " : " + row[4]
					position = utm.from_latlon(float(util.lat), float(util.lon))
					marker = StaticObject.create("defaultSphere")
					marker.setScale(Vector3(50,50,50))
					marker.setPosition(Vector3(float(position[0]), float(position[1]), 0))
					marker.setEffect('colored -d red')
					all.addChild(marker)

#------------------------------------------------------------------------
# main variables and statements

scene = getSceneManager()

# set background to black
scene.setBackgroundColor(Color(0, 0, 0, 1))

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
cam = getDefaultCamera()
cam.setPosition(util.city1.getBoundCenter() + Vector3(7768.82, 2281.18, 2034.08))
cam.getController().setSpeed(1000)
cam.pitch(3.14159*0.45) #pitch up to start off flying over the city

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
crimeData()

