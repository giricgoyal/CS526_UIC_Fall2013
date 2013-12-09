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
isGraphShown = False

x1 = "x1"
x2 = "x2"
x3 = "x3"
x4 = "x4"

xlog0 = "xl0"
xlog1 = "xl1"
xlog2 = "xl2"
xlog3 = "xl3"
xlog4 = "xl4"

y1 = "y1"
y2 = "y2"
y3 = "y3"
y4 = "y4"

ylog0 = "yl0"
ylog1 = "yl1"
ylog2 = "yl2"
ylog3 = "yl3"
ylog4 = "yl4"

color1 = "#FF2222FF"
color2 = "#22FF22FF"
color3 = "#7777DDFF"


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
	global minRadius, minDistFromStar, minPeriod, minEccentricity, minRotation, minInclination, minMass
	global screenCenterGraph, planetList, xAxisDict, yAxisDict, graphContainer

	print "creating graphs"

	# first pane
	outlineBox = BoxShape.create(1.0, 2.3, 0.001)
	outlineBox.setPosition(Vector3(-0.5, 0, 0.01))
	outlineBox.setEffect('colored -e #22222288')
	outlineBox.getMaterial().setTransparent(True)
	outlineBox.setSelectable(True)


	xLine = BoxShape.create(1.0,0.005, 0.001)
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

	for i in range(1,5):
		xLines = BoxShape.create(0.8,0.005,0.001)
		xLines.setPosition(-0.5, -i * 0.1 * 2 + 0.1, 0)
		xLines.setEffect('colored -e #999999DD')
		xLines.getMaterial().setTransparent(True)
		screenCenterGraph.addChild(xLines)


		xLines2 = BoxShape.create(0.8,0.005,0.001)
		xLines2.setPosition(-0.5, i * 0.1 * 2 + 0.1, 0)
		xLines2.setEffect('colored -e #999999DD')
		xLines2.getMaterial().setTransparent(True)
		screenCenterGraph.addChild(xLines2)

		yLines = BoxShape.create(0.005,0.8,0.001)
		yLines.setPosition(-i * 0.1 * 2 - 0.1, 0.5, 0)
		yLines.setEffect('colored -e #999999DD')
		yLines.getMaterial().setTransparent(True)
		screenCenterGraph.addChild(yLines)

		yLines2 = BoxShape.create(0.005,0.8,0.001)
		yLines2.setPosition(-i * 0.1 *2 - 0.1, -0.5, 0)
		yLines2.setEffect('colored -e #999999DD')
		yLines2.getMaterial().setTransparent(True)
		screenCenterGraph.addChild(yLines2)


	x1Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, x1)
	x1Label.setPosition(Vector3(0.2-0.5,-0.94, 0))
	x1Label.getMaterial().setTransparent(False)
	x1Label.getMaterial().setDepthTestEnabled(False)
	x1Label.setColor(colorWhite)
	x1Label.yaw(pi)
	x1Label.setFontResolution(100)

	x2Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, x2)
	x2Label.setPosition(Vector3(-0.5,-0.94, 0))
	x2Label.getMaterial().setTransparent(False)
	x2Label.getMaterial().setDepthTestEnabled(False)
	x2Label.setColor(colorWhite)
	x2Label.yaw(pi)
	x2Label.setFontResolution(100)

	x3Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, x3)
	x3Label.setPosition(Vector3(-0.2-0.5,-0.94, 0))
	x3Label.getMaterial().setTransparent(False)
	x3Label.getMaterial().setDepthTestEnabled(False)
	x3Label.setColor(colorWhite)
	x3Label.yaw(pi)
	x3Label.setFontResolution(100)

	x4Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, x4)
	x4Label.setPosition(Vector3(-0.4-0.5,-0.94, 0))
	x4Label.getMaterial().setTransparent(False)
	x4Label.getMaterial().setDepthTestEnabled(False)
	x4Label.setColor(colorWhite)
	x4Label.yaw(pi)
	x4Label.setFontResolution(100)

	xlog0Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, xlog0)
	xlog0Label.setPosition(Vector3(0.4-0.5,0.06, 0))
	xlog0Label.getMaterial().setTransparent(False)
	xlog0Label.getMaterial().setDepthTestEnabled(False)
	xlog0Label.setColor(colorWhite)
	xlog0Label.yaw(pi)
	xlog0Label.setFontResolution(100)


	xlog1Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, xlog1)
	xlog1Label.setPosition(Vector3(0.2-0.5,0.06, 0))
	xlog1Label.getMaterial().setTransparent(False)
	xlog1Label.getMaterial().setDepthTestEnabled(False)
	xlog1Label.setColor(colorWhite)
	xlog1Label.yaw(pi)
	xlog1Label.setFontResolution(100)

	xlog2Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, xlog2)
	xlog2Label.setPosition(Vector3(-0.5,0.06, 0))
	xlog2Label.getMaterial().setTransparent(False)
	xlog2Label.getMaterial().setDepthTestEnabled(False)
	xlog2Label.setColor(colorWhite)
	xlog2Label.yaw(pi)
	xlog2Label.setFontResolution(100)

	xlog3Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, xlog3)
	xlog3Label.setPosition(Vector3(-0.2-0.5,0.06, 0))
	xlog3Label.getMaterial().setTransparent(False)
	xlog3Label.getMaterial().setDepthTestEnabled(False)
	xlog3Label.setColor(colorWhite)
	xlog3Label.yaw(pi)
	xlog3Label.setFontResolution(100)

	xlog4Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, xlog4)
	xlog4Label.setPosition(Vector3(-0.4-0.5,0.06, 0))
	xlog4Label.getMaterial().setTransparent(False)
	xlog4Label.getMaterial().setDepthTestEnabled(False)
	xlog4Label.setColor(colorWhite)
	xlog4Label.yaw(pi)
	xlog4Label.setFontResolution(100)



	y1Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, y1)
	y1Label.setPosition(Vector3(0.45-0.5,-0.7, 0))
	y1Label.getMaterial().setTransparent(False)
	y1Label.getMaterial().setDepthTestEnabled(False)
	y1Label.setColor(colorWhite)
	y1Label.yaw(pi)
	y1Label.setFontResolution(100)

	y2Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, y2)
	y2Label.setPosition(Vector3(0.45-0.5,-0.5, 0))
	y2Label.getMaterial().setTransparent(False)
	y2Label.getMaterial().setDepthTestEnabled(False)
	y2Label.setColor(colorWhite)
	y2Label.yaw(pi)
	y2Label.setFontResolution(100)

	y3Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, y3)
	y3Label.setPosition(Vector3(0.45-0.5,-0.3, 0))
	y3Label.getMaterial().setTransparent(False)
	y3Label.getMaterial().setDepthTestEnabled(False)
	y3Label.setColor(colorWhite)
	y3Label.yaw(pi)
	y3Label.setFontResolution(100)

	y4Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, y4)
	y4Label.setPosition(Vector3(0.45-0.5,-0.1, 0))
	y4Label.getMaterial().setTransparent(False)
	y4Label.getMaterial().setDepthTestEnabled(False)
	y4Label.setColor(colorWhite)
	y4Label.yaw(pi)
	y4Label.setFontResolution(100)

	ylog0Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, ylog0)
	ylog0Label.setPosition(Vector3(0.45-0.5,0.1, 0))
	ylog0Label.getMaterial().setTransparent(False)
	ylog0Label.getMaterial().setDepthTestEnabled(False)
	ylog0Label.setColor(colorWhite)
	ylog0Label.yaw(pi)
	ylog0Label.setFontResolution(100)


	ylog1Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, ylog1)
	ylog1Label.setPosition(Vector3(0.45-0.5,0.3, 0))
	ylog1Label.getMaterial().setTransparent(False)
	ylog1Label.getMaterial().setDepthTestEnabled(False)
	ylog1Label.setColor(colorWhite)
	ylog1Label.yaw(pi)
	ylog1Label.setFontResolution(100)

	ylog2Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, ylog2)
	ylog2Label.setPosition(Vector3(0.45-0.5,0.5, 0))
	ylog2Label.getMaterial().setTransparent(False)
	ylog2Label.getMaterial().setDepthTestEnabled(False)
	ylog2Label.setColor(colorWhite)
	ylog2Label.yaw(pi)
	ylog2Label.setFontResolution(100)

	ylog3Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, ylog3)
	ylog3Label.setPosition(Vector3(0.45-0.5,0.7, 0))
	ylog3Label.getMaterial().setTransparent(False)
	ylog3Label.getMaterial().setDepthTestEnabled(False)
	ylog3Label.setColor(colorWhite)
	ylog3Label.yaw(pi)
	ylog3Label.setFontResolution(100)

	ylog4Label = Text3D.create('data/fonts/helvetica.ttf', 0.02, ylog4)
	ylog4Label.setPosition(Vector3(0.45-0.5,0.9, 0))
	ylog4Label.getMaterial().setTransparent(False)
	ylog4Label.getMaterial().setDepthTestEnabled(False)
	ylog4Label.setColor(colorWhite)
	ylog4Label.yaw(pi)
	ylog4Label.setFontResolution(100)


	xLine2 = BoxShape.create(1.0,0.005, 0.001)
	xLine2.setPosition(Vector3(-0.5,0.1, 0))
	xLine2.setEffect('colored -e #999999DD')
	xLine2.getMaterial().setTransparent(True)
	xLineLabel2 = Text3D.create('data/fonts/helvetica.ttf', 0.02, xLabel)
	xLineLabel2.setPosition(Vector3(-0.5,0.02, 0))
	xLineLabel2.getMaterial().setTransparent(False)
	xLineLabel2.getMaterial().setDepthTestEnabled(False)
	xLineLabel2.setColor(colorWhite)
	xLineLabel2.yaw(pi)
	xLineLabel2.setFontResolution(100)
	
	yLine = BoxShape.create(0.005, 2.0, 0.001)
	yLine.setPosition(Vector3(-0.5+0.4,0,0))
	yLine.setEffect('colored -e #999999DD')
	yLine.getMaterial().setTransparent(True);

	yLineLabel = Text3D.create('data/fonts/helvetica.ttf', 0.03, yLabel)
	yLineLabel.setPosition(Vector3(-0.5+0.48,-0.3, 0))
	yLineLabel.getMaterial().setTransparent(False)
	yLineLabel.getMaterial().setDepthTestEnabled(False)
	yLineLabel.setColor(colorWhite)
	yLineLabel.roll(pi/2)
	yLineLabel.yaw(pi)
	yLineLabel.setFontResolution(100)

	yLineLabel2 = Text3D.create('data/fonts/helvetica.ttf', 0.03, yLabel)
	yLineLabel2.setPosition(Vector3(-0.5+0.48,0.7, 0))
	yLineLabel2.getMaterial().setTransparent(False)
	yLineLabel2.getMaterial().setDepthTestEnabled(False)
	yLineLabel2.setColor(colorWhite)
	yLineLabel2.roll(pi/2)
	yLineLabel2.yaw(pi)
	yLineLabel2.setFontResolution(100)
	
	screenCenterGraph.addChild(outlineBox)
	screenCenterGraph.addChild(xLine)
	screenCenterGraph.addChild(yLine)
	screenCenterGraph.addChild(xLine2)
	screenCenterGraph.addChild(xLineLabel)
	screenCenterGraph.addChild(xLineLabel2)
	screenCenterGraph.addChild(yLineLabel)
	screenCenterGraph.addChild(yLineLabel2)
	screenCenterGraph.addChild(x1Label);
	screenCenterGraph.addChild(x2Label);
	screenCenterGraph.addChild(x3Label);
	screenCenterGraph.addChild(x4Label);
	screenCenterGraph.addChild(y1Label);
	screenCenterGraph.addChild(y2Label);
	screenCenterGraph.addChild(y3Label);
	screenCenterGraph.addChild(y4Label);
	screenCenterGraph.addChild(xlog0Label);
	screenCenterGraph.addChild(xlog1Label);
	screenCenterGraph.addChild(xlog2Label);
	screenCenterGraph.addChild(xlog3Label);
	screenCenterGraph.addChild(xlog4Label);
	screenCenterGraph.addChild(ylog0Label);
	screenCenterGraph.addChild(ylog1Label);
	screenCenterGraph.addChild(ylog2Label);
	screenCenterGraph.addChild(ylog3Label);
	screenCenterGraph.addChild(ylog4Label);

	graphContainer.addChild(screenCenterGraph)


	hLoc = 6.75
	v = 3.5 * 0.29 + 0.51
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenterGraph.setPosition(Vector3(0,-0.2,1000))
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

		
	graphGlyphDict['xlabel'] = xLineLabel
	graphGlyphDict['ylabel'] = yLineLabel
	graphGlyphDict['x1label'] = x1Label
	graphGlyphDict['x2label'] = x2Label
	graphGlyphDict['x3label'] = x3Label
	graphGlyphDict['x4label'] = x4Label
	graphGlyphDict['y1label'] = y1Label
	graphGlyphDict['y2label'] = y2Label
	graphGlyphDict['y3label'] = y3Label
	graphGlyphDict['y4label'] = y4Label
	


	graphGlyphLogDict['xlabel'] = xLineLabel2
	graphGlyphLogDict['ylabel'] = yLineLabel2
	graphGlyphLogDict['xlog0label'] = xlog0Label
	graphGlyphLogDict['xlog1label'] = xlog1Label
	graphGlyphLogDict['xlog2label'] = xlog2Label
	graphGlyphLogDict['xlog3label'] = xlog3Label
	graphGlyphLogDict['xlog4label'] = xlog4Label
	graphGlyphLogDict['ylog0label'] = ylog0Label
	graphGlyphLogDict['ylog1label'] = ylog1Label
	graphGlyphLogDict['ylog2label'] = ylog2Label
	graphGlyphLogDict['ylog3label'] = ylog3Label
	graphGlyphLogDict['ylog4label'] = ylog4Label
	

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
	global screenCenterGraph, isGraphShown
	screenCenterGraph.setPosition(Vector3(0,1000,0))
	isGraphShown = False


def showGraph(xAD, yAD, xL, yL):
	global screenCenterGraph
	global screenCenterGraph, planetList
	global isGraphShown
	global x1, x2, x3, x4, y1, y2, y3, y4, xlog0, xlog1, xlog2, xlog3, xlog4, ylog0, ylog1, ylog2, ylog3, ylog4
	global xLabel, yLabel
	isGraphShown = True
	
	print "showingGraphs"

	maxRadius, maxDistFromStar, maxPeriod, maxEccentricity, maxRotation, maxInclination, maxMass = getMaxs()

	x1, x2, x3, x4, y1, y2, y3, y4, xlog0, xlog1, xlog2, xlog3, xlog4, ylog0, ylog1, ylog2, ylog3, ylog4 = setLabels(xLabel, yLabel)

	xLabel = getxLabel()
	yLabel = getyLabel()

	xAxisDict = xAD.copy()
	yAxisDict = yAD.copy()

	print xLabel + " : " + yLabel
	xLabelN = xLabel
	yLabelN = yLabel
	if xLabel == "Distance from its Star":
		xLabelN = xLabel + " x10^9Kms"
		x1 = str(float(x1)/1000000000)
		x2 = str(float(x2)/1000000000)
		x3 = str(float(x3)/1000000000)
		x4 = str(float(x4)/1000000000)
	if yLabel == "Distance from its Star":
		yLabelN = yLabel + " x10^9Kms"
		y1 = str(float(y1)/1000000000)
		y2 = str(float(y2)/1000000000)
		y3 = str(float(y3)/1000000000)
		y4 = str(float(y4)/1000000000)
	if xLabel == "Radius":
		xLabelN = xLabel + " x10^4kms"
		x1 = str(float(x1)/10000)
		x2 = str(float(x2)/10000)
		x3 = str(float(x3)/10000)
		x4 = str(float(x4)/10000)
	if yLabel == "Radius":
		yLabelN = yLabel + " x10^4kms"
		y1 = str(float(y1)/10000)
		y2 = str(float(y2)/10000)
		y3 = str(float(y3)/10000)
		y4 = str(float(y4)/10000)
	if xLabel == "Revolution Period":
		xLanelN = xLabel + " years"
	if yLabel == "Revolution Period":
		yLabelN = yLabel + " years"
	if xLabel == "Rotation":
		xLabelN = xLabel + " days"
	if yLabel == "Rotation":
		yLabelN = yLabel + " days"
	if xLabel == "Eccentricity":
		xLabelN = xLabel + ""
	if yLabel == "Eccentricity":
		yLabelN = yLabel + ""
	if xLabel == "Inclination":
		xLabelN = xLabel + ""
	if yLabel == "Inclination":
		yLabelN = yLabel + ""
	if xLabel == "Mass":
		xLabelN = xLabel + ""
	if yLabel == "Mass":
		yLabelN = yLabel + ""

	graphGlyphDict['xlabel'].setText(xLabelN)
	graphGlyphDict['ylabel'].setText(yLabelN)
	graphGlyphDict['x1label'].setText(x1)
	graphGlyphDict['x2label'].setText(x2)
	graphGlyphDict['x3label'].setText(x3)
	graphGlyphDict['x4label'].setText(x4)
	graphGlyphDict['y1label'].setText(y1)
	graphGlyphDict['y2label'].setText(y2)
	graphGlyphDict['y3label'].setText(y3)
	graphGlyphDict['y4label'].setText(y4)
	


	graphGlyphLogDict['xlabel'].setText(xLabel + " (log(n)")
	graphGlyphLogDict['ylabel'].setText(yLabel + " (log(n))")
	graphGlyphLogDict['xlog0label'].setText(xlog0)
	graphGlyphLogDict['xlog1label'].setText(xlog1)
	graphGlyphLogDict['xlog2label'].setText(xlog2)
	graphGlyphLogDict['xlog3label'].setText(xlog3)
	graphGlyphLogDict['xlog4label'].setText(xlog4)
	graphGlyphLogDict['ylog0label'].setText(ylog0)
	graphGlyphLogDict['ylog1label'].setText(ylog1)
	graphGlyphLogDict['ylog2label'].setText(ylog2)
	graphGlyphLogDict['ylog3label'].setText(ylog3)
	graphGlyphLogDict['ylog4label'].setText(ylog4)
	

	for planet in planetList:


		x_Original = xAxisDict[planet]
		y_Original = yAxisDict[planet]

		color = color1

		if (x_Original > 0 and y_Original > 0):
			if checkInDisplayList(planet) == True:
				if checkInSolarSystem(planet) == True:
					color = color2

				if checkInActiveSystem(planet, getActiveSystem()) == True:
					color = color3


				x_map = translate(x_Original, 0, xAxisDict['max'], 0.0, 0.8)
				y_map = translate(y_Original, 0, yAxisDict['max'], -0.9, -0.1)
				graphGlyphDict[planet].setPosition(-0.1-x_map, y_map, 0)
				graphGlyphDict[planet].setEffect('colored -e ' + color)
				
				x_logmap = translate(log(x_Original, 10), floor(log(xAxisDict['min'], 10)), ceil(log(xAxisDict['max'], 10)), 0.0, 0.8)
				y_logmap = translate(log(y_Original, 10), floor(log(yAxisDict['min'], 10)), ceil(log(yAxisDict['max'], 10)), 0.1, 0.9)
				graphGlyphLogDict[planet].setPosition(-0.1-x_logmap, y_logmap, 0)
				graphGlyphLogDict[planet].setEffect('colored -e ' + color)
			
			else:
				graphGlyphDict[planet].setPosition(-0.1, 0, -10)
				graphGlyphLogDict[planet].setPosition(-0.1, 0, -10)


		else:
			graphGlyphDict[planet].setEffect('colored -e #22222288')
			graphGlyphLogDict[planet].setEffect('colored -e #22222288')
			graphGlyphDict[planet].setPosition(-0.1, 0, -10)
			graphGlyphLogDict[planet].setPosition(-0.1, 0, -10)
		


	hLoc = 6.75
	v = 3.5 * 0.29 + 0.51
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenterGraph.setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v, cos(hLoc * degreeConvert) * caveRadius))



def setLabels(xLabel, yLabel):
	global x1, x2, x3, x4, y1, y2, y3, y4, xlog0, xlog1, xlog2, xlog3, xlog4, ylog0, ylog1, ylog2, ylog3, ylog4
	global maxRadius, maxDistFromStar, maxPeriod, maxEccentricity, maxRotation, maxInclination, maxMass
	global minRadius, minDistFromStar, minPeriod, minEccentricity, minRotation, minInclination, minMass

	minX = 0.0
	maxX = 0.0
	minY = 0.0
	maxY = 0.0

	maxRadius, maxDistFromStar, maxPeriod, maxEccentricity, maxRotation, maxInclination, maxMass = getMaxs()
	minRadius, minDistFromStar, minPeriod, minEccentricity, minRotation, minInclination, minMass = getMins()

	xLabel = getxLabel()
	yLabel = getyLabel()
	print xLabel + " : " + yLabel
	if xLabel == "Radius":
		minX = minRadius
		maxX = maxRadius
	elif xLabel == "Distance from its Star":
		minX = minDistFromStar
		maxX = maxDistFromStar
	elif xLabel == "Revolution Period":
		minX = minPeriod
		maxX = maxPeriod
	elif xLabel == "Eccentricity":
		minX = minEccentricity
		maxX = maxEccentricity
	elif xLabel == "Rotation":
		minX = minRotation
		maxX = maxRotation
	elif xLabel == "Inclination":
		minX = minInclination
		maxX = maxInclination
	elif xLabel == "Mass":
		minX = minMass
		maxX = maxMass

	if yLabel == "Radius":
		minY = minRadius
		maxY = maxRadius
	elif yLabel == "Distance from its Star":
		minY = minDistFromStar
		maxY = maxDistFromStar
	elif yLabel == "Revolution Period":
		minY = minPeriod
		maxY = maxPeriod
	elif yLabel == "Eccentricity":
		minY = minEccentricity
		maxY = maxEccentricity
	elif yLabel == "Rotation":
		minY = minRotation
		maxY = maxRotation
	elif yLabel == "Inclination":
		minY = minInclination
		maxY = maxInclination
	elif yLabel == "Mass":
		minY = minMass
		maxY = maxMass

	# for xlabels
	xMinO = minX
	xMaxO = maxX
	xMinL = floor(log(minX, 10))
	xMaxL = ceil(log(maxX, 10))

	print str(pow(10, floor(xMinL))) + " : " + str(floor(xMinL))
	print str(pow(10, ceil(xMaxL))) + " : " + str(ceil(xMaxL))

	xdo = (xMaxO)/4
	xdl = (xMaxL - xMinL)/4

	x1 = str('%.2f' %xdo)
	x2 = str('%.2f' %(xdo*2))
	x3 = str('%.2f' %(xdo*3))
	x4 = str('%.2f' %(xdo*4))

	xlog0 = str('%.2f' %pow(10,xMinL))
	xlog1 = str('%.2f' %pow(10,(xMinL + xdl)))
	xlog2 = str('%.2f' %pow(10,(xMinL + xdl*2)))
	xlog3 = str('%.2f' %pow(10,(xMinL + xdl*3)))
	xlog4 = str('%.2f' %pow(10,(xMinL + xdl*4)))

	# for ylabels
	yMinO = minY
	yMaxO = maxY
	yMinL = floor(log(minY, 10))
	yMaxL = ceil(log(maxY, 10))

	ydo = (yMaxO)/4
	ydl = (yMaxL - yMinL)/4

	y1 = str('%.2f' %ydo)
	y2 = str('%.2f' %(ydo*2))
	y3 = str('%.2f' %(ydo*3))
	y4 = str('%.2f' %(ydo*4))

	ylog0 = str('%.2f' %pow(10,yMinL))
	ylog1 = str('%.2f' %pow(10,(yMinL + ydl)))
	ylog2 = str('%.2f' %pow(10,(yMinL + ydl*2)))
	ylog3 = str('%.2f' %pow(10,(yMinL + ydl*3)))
	ylog4 = str('%.2f' %pow(10,(yMinL + ydl*4)))

	return x1, x2, x3, x4, y1, y2, y3, y4, xlog0, xlog1, xlog2, xlog3, xlog4, ylog0, ylog1, ylog2, ylog3, ylog4


def updateGraphColors(c1, c2, c3):
	global color1, color2, color3

	color1 = c1
	color2 = c2
	color3 = c3

	
			
			
def getIsGraphShown():
	return isGraphShown
	

def updateGlyphScale(val):
	factor = 1.0/pow(2, 2-val)
	for planet in planetList:
		graphGlyphDict[planet].setScale(factor, factor, factor)
		graphGlyphLogDict[planet].setScale(factor, factor, factor)

