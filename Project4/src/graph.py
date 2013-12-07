# #######################################################
# 
# author: giric goyal
# #######################################################

# -------------------------------------------------------
# imports 
from util import *
from math import *
from euclid import *
from omega import *
from cyclops import *
from cameraManager import *
from caveutil import *


screenCenterGraph = SceneNode.create("screenCenter")
	


# ------------------------------------------------------
# methods

def drawCicle(radius, x, y, z, color):
	obj = CylinderShape.create(0.01, radius, radius, 10, 128);
	obj.setEffect('colored -e ' + color)
	obj.setPosition(Vector3(x,y,z))
	obj.getMaterial().setTransparent(True)
	obj.setScale(Vector3(0.5,0.5,1))
	return obj


def createGraphs():
	global planetRadiusDict, planetDistFromStarDict, planetPeriodDict, planetEccentricityDict, planetRotationDict, planetInclinationDict, planetMassDict
	global maxRadius, maxDistFromStar, maxPeriod, maxEccentricity, maxRotation, maxInclination, maxMass
	global screenCenterGraph, planetList, xAxisDict, yAxisDict

	print "creating graphs"

	# first pane
	outlineBox = BoxShape.create(1.0, 2.0, 0.001)
	outlineBox.setPosition(Vector3(-0.5, 0, 0.01))
	outlineBox.setEffect('colored -e #22222288')
	outlineBox.getMaterial().setTransparent(True)
	outlineBox.setSelectable(True)


	xLine = BoxShape.create(1.0,0.01, 0.001)
	xLine.setPosition(Vector3(-0.5,-0.9, 0))
	xLine.setEffect('colored -e #999999DD')
	xLine.getMaterial().setTransparent(True)
	xLineLabel = Text3D.create('data/fonts/helvetica.ttf', 0.03, xLabel)
	xLineLabel.setPosition(Vector3(-0.5,-0.98, 0))
	xLineLabel.getMaterial().setTransparent(False)
	xLineLabel.getMaterial().setDepthTestEnabled(False)
	xLineLabel.setColor(colorWhite)
	xLineLabel.yaw(pi)
	xLineLabel.setFontResolution(100)


	xLine2 = BoxShape.create(1.0,0.01, 0.001)
	xLine2.setPosition(Vector3(-0.5,0.1, 0))
	xLine2.setEffect('colored -e #999999DD')
	xLine2.getMaterial().setTransparent(True)
	xLineLabel2 = Text3D.create('data/fonts/helvetica.ttf', 0.03, xLabel)
	xLineLabel2.setPosition(Vector3(-0.5,0.02, 0))
	xLineLabel2.getMaterial().setTransparent(False)
	xLineLabel2.getMaterial().setDepthTestEnabled(False)
	xLineLabel2.setColor(colorWhite)
	xLineLabel2.yaw(pi)
	xLineLabel2.setFontResolution(100)
	
	yLine = BoxShape.create(0.01, 2.0, 0.001)
	yLine.setPosition(Vector3(-0.5+0.4,0,0))
	yLine.setEffect('colored -e #999999DD')
	yLine.getMaterial().setTransparent(True);
	
	screenCenterGraph.addChild(outlineBox)
	screenCenterGraph.addChild(xLine)
	screenCenterGraph.addChild(yLine)
	screenCenterGraph.addChild(xLine2)
	screenCenterGraph.addChild(xLineLabel)

	hLoc = 6.75
	v = 3.5 * 0.29 + 0.51
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenterGraph.setPosition(Vector3(0,0,1000))
	#screenCenterGraph.setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v, cos(hLoc * degreeConvert) * caveRadius))
	screenCenterGraph.yaw(hLoc * degreeConvert)

	'''
	# Second pane
	outlineBox2 = BoxShape.create(1.0, 2.0, 0.001)
	outlineBox2.setPosition(Vector3(-0.5, 0, 0.01))
	outlineBox2.setEffect('colored -e #22222288')
	outlineBox2.getMaterial().setTransparent(True)
	outlineBox2.setSelectable(True)


	xLine2 = BoxShape.create(1.0,0.01, 0.001)
	xLine2.setPosition(Vector3(-0.5,-0.9, 0))
	xLine2.setEffect('colored -e #999999DD')
	xLine2.getMaterial().setTransparent(True)
	xLineLabel2 = Text3D.create('data/fonts/helvetica.ttf', 0.03, xLabel)
	xLineLabel2.setPosition(Vector3(-0.5,-0.98, 0))
	xLineLabel2.getMaterial().setTransparent(False)
	xLineLabel2.getMaterial().setDepthTestEnabled(False)
	xLineLabel2.setColor(colorWhite)
	xLineLabel2.yaw(pi)
	xLineLabel2.setFontResolution(100)
			
	
	yLine2 = BoxShape.create(0.01, 2.0, 0.001)
	yLine2.setPosition(Vector3(-0.5-0.4,0,0))
	yLine2.setEffect('colored -e #999999DD')
	yLine2.getMaterial().setTransparent(True);
	

	screenCenter2 = SceneNode.create("screenCenter2")
	screenCenter2.addChild(outlineBox2)
	screenCenter2.addChild(xLine2)
	#screenCenter2.addChild(yLine2)
	screenCenter2.addChild(xLineLabel2)

	hLoc = 6.25
	v = 3.5 * 0.29 + 0.51
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenter2.setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v, cos(hLoc * degreeConvert) * caveRadius))
	screenCenter2.yaw(hLoc * degreeConvert)
	'''
	
	maxRadius = max(planetRadiusDict.values())
	maxDistFromStar = max(planetDistFromStarDict.values())
	maxPeriod = max(planetPeriodDict.values())
	maxEccentricity = max(planetEccentricityDict.values())
	maxRotation = max(planetRotationDict.values())
	maxInclination = max(planetInclinationDict.values())
	maxMass = max(planetMassDict.values())

	for i in range(1,len(planetList)+1):
		x_map = translate(i, 0, len(planetDistFromStarDict), -0.5+0.4, -0.5-0.4)
		y_map = translate(i, 0, len(planetDistFromStarDict), -0.9, -0.1)

		objTry = drawCicle(0.01, x_map, y_map, 0, '#FF0000FF')

		graphGlyphDict[planetList[i-1]] = objTry

		screenCenterGraph.addChild(objTry)

		if (i > 0):
			x_logmap = translate(log(i, 10), -log(len(planetDistFromStarDict),10), log(len(planetDistFromStarDict),10), -0.5+0.4, -0.5-0.4)
			y_logmap = translate(log(i, 10), -log(len(planetDistFromStarDict),10), log(len(planetDistFromStarDict),10), 0.1, 0.9)
		
			objTry2 = drawCicle(0.01, x_logmap, y_logmap, 0, '#FF0000FF')
			graphGlyphLogDict[planetList[i-1]] = objTry2
		
			screenCenterGraph.addChild(objTry2)

		

	xAxisDict = getxAxisDict()
	yAxisDict = getyAxisDict()

	for planet in planetList:
		x_Original = planetDistFromStarDict[planet]
		y_Original = planetPeriodDict[planet]

		if (x_Original > 0 and y_Original > 0):

			x_map = translate(x_Original, 0, maxDistFromStar, -0.5+0.4, -0.5-0.4)
			y_map = translate(y_Original, 0, maxPeriod, -0.9, -0.1)
			graphGlyphDict[planet].setPosition(x_map, y_map, 0)

			x_logmap = translate(log(x_Original, 10), -log(maxDistFromStar, 10), log(maxDistFromStar, 10), -0.5+0.4, 0.5-0.4)
			y_logmap = translate(log(y_Original, 10), -log(maxPeriod, 10), log(maxPeriod, 10), 0.1, 0.9)
			graphGlyphLogDict[planet].setPosition(x_logmap, y_logmap, 0)



def removeGraph():
	global screenCenterGraph
	screenCenterGraph.setPosition(Vector3(0,1000,0))


def showGraph(xAxisDict, yAxisDict):
	global screenCenterGraph
	global screenCenterGraph, planetList
	
	print "showingGraphs"

	maxRadius = max(planetRadiusDict.values())
	maxDistFromStar = max(planetDistFromStarDict.values())
	maxPeriod = max(planetPeriodDict.values())
	maxEccentricity = max(planetEccentricityDict.values())
	maxRotation = max(planetRotationDict.values())
	maxInclination = max(planetInclinationDict.values())
	maxMass = max(planetMassDict.values())

	for planet in planetList:
		x_Original = xAxisDict[planet]
		y_Original = yAxisDict[planet]

		color = '#FF7777FF'
		if checkInSolarSystem(planet) == True:
			color = '#8888FFFF'
		if (x_Original > 0 and y_Original > 0):

			x_map = translate(x_Original, 0, xAxisDict['max'], 0.0, 0.8)
			y_map = translate(y_Original, 0, yAxisDict['max'], -0.9, -0.1)
			graphGlyphDict[planet].setPosition(-0.1-x_map, y_map, 0)
			graphGlyphDict[planet].setEffect('colored -e ' + color)
			
			x_logmap = translate(log(x_Original, 10), log(xAxisDict['min'], 10), log(xAxisDict['max'], 10), 0.0, 0.8)
			y_logmap = translate(log(y_Original, 10), log(yAxisDict['min'], 10), log(yAxisDict['max'], 10), 0.1, 0.9)
			graphGlyphLogDict[planet].setPosition(-0.1-x_logmap, y_logmap, 0)
			graphGlyphLogDict[planet].setEffect('colored -e ' + color)
			

		else:
			graphGlyphDict[planet].setEffect('colored -e #00000000')
			graphGlyphLogDict[planet].setEffect('colored -e #00000000')
			


	hLoc = 6.75
	v = 3.5 * 0.29 + 0.51
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenterGraph.setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v, cos(hLoc * degreeConvert) * caveRadius))


	
