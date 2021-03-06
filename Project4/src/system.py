# ------------------------------------------------------------------------------------------
# imports
from math import *
from euclid import *
from omega import *
from cyclops import *
from util import *
from cameraManager import *


# ---------------------------------------------------------------------------------
# main

panelCounter = 0

xMin = sin(6.5 * (36.0/360.0 * 2 * pi)) * 3.25
xMax = sin(4.5 * (36.0/360.0 * 2 * pi)) * 3.25
yMin = 0.41
yMax = 5.8 * 0.29 + 0.41
yMin2 = 6 * 0.29 + 0.41
yMax2 = 7 * 0.29 + 0.41
zMin = cos(6.5 * (36.0/360.0 * 2 * pi)) * 3.25
zMax = cos(4.5 * (36.0/360.0 * 2 * pi)) * 3.25

infoTextList = []
infoContainer = None
infoDisplayBox = None
systemInfo = None
planetInfo = None
midWindow = None

text1 = ""
text2 = ""
text3 = ""
text4 = ""
text5 = ""
text6 = ""
text7 = ""
text8 = ""
text9 = ""
text10 = ""

# --------------------------------------------------------------------------------------
# methods
# Calculate habitable zones
def setHabitableZone(system, starName, starType):
	habObj = habZone(starName, starType)
	habObj.calHabitableZone()
	habitableZones[system] = habObj
	
	
# create orbits for the planets
def addOrbit(orbit, col, thick, system, name):
	circle = LineSet.create()
	if col == 0:
		segments = 128
		radius = 1
	else:
		segments = 256
		radius = 1
	thickness = thick
	
	# need to think about elliptical orbit, for now circular based on minorA
	a = 0.0
	newList = []
	while a <= 360:
		x = float(float(cos(radians(a))) * float(radius))
		y = float(float(sin(radians(a))) * float(radius))
		a += 360.0/segments
		nx = float(float(cos(radians(a))) * float(radius))
		ny = float(float(sin(radians(a))) * float(radius))
		
		l = circle.addLine()
		l.setStart(Vector3(x, 0.0, y))
		l.setEnd(Vector3(nx, 0.0, ny))
		l.setThickness(thickness)
		newList.append(l)
		
		if system == "Solar System":
			circle.setPosition(Vector3(0,0,0))
		else:
			circle.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
		
		if col == 0:
			circle.setEffect('colored -e white')
		else:
			circle.setEffect('colored -e #00BB0033')
			circle.getMaterial().setTransparent(True)
			
        # Squish z to turn the torus into a disc-like shape.

		if col == 0:
			circle.setScale(Vector3(orbit, 1000.0, orbit))
		else:
			circle.setScale(Vector3(orbitScaleFactor * userScaleFactor, 0.1, orbitScaleFactor * userScaleFactor)) # 0.1
	if col == 0:
		orbitDict[name] = circle
	else:
		habiOuterDict[system] = circle
		habiInnerDict[system] = newList
	systemNodeDict[system].addChild(circle)

# create each 2D system
def createEach2DSystem(system, h, v, panelCounter):
	theSystem = allSystemsOrbital[system]
	
	outlineBox = BoxShape.create(2.0, 0.25, 0.001)
	outlineBox.setPosition(Vector3(-0.5, 0, 0.01))
	outlineBox.setEffect('colored -e #111122EE')
	outlineBox.getMaterial().setTransparent(False)
	outlineBox.setSelectable(True)
	outlineBox.setTag(system + " box "+str(panelCounter))
	hitWallDict[system] = outlineBox
	#infoOutlineBox = BoxShape.create(2.0, 2.0, 0.01)
	#infoOutlineBox.setPosition(Vector3(0,0,0))
	#infoOutlineBox.setEffect('colored -e #111111EE')
	#infoOutlineBox.getMaterial().setTransparent(False)
	
	screenCenter = SceneNode.create(system + " box "+str(panelCounter))
	infoBox = SceneNode.create(system + " infoBox")
	sSystem = SceneNode.create("sSystem"+str(panelCounter))
	for name, model in theSystem.iteritems():
		pos = None
		if (48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10) >= wallLimit:
		#if theSystem[name].minorA <= wallLimit:
			pos = Vector3(0.0, 0.0, 48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10)
			pos2 = Vector3(0.0, -10000.0, 48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10)
		else:
			pos = Vector3(0,0,wallLimit)
			pos2 = Vector3(0,-10000, wallLimit)
			#pos = Vector3(0.0, 0.0, - wallLimit * orbitScaleFactor * userScaleFactor * 10)
			#pos2 = Vector3(0.0, -10000.0, - wallLimit * orbitScaleFactor * userScaleFactor * 10)
		
		if theSystem[name].isStar == 0:
			#model = SphereShape.create(0.5, 4)
			model = StaticObject.create("defaultSphere")
			model.setScale(Vector3(theSystem[name].radius * XplanetScaleFactor, theSystem[name].radius * XplanetScaleFactor, theSystem[name].radius * XplanetScaleFactor))
			
			# text 
			text = str(name)
			
			t1 = Text3D.create('data/fonts/helvetica.ttf', 1, text)
			t1.setPosition(pos2)
			t1.yaw(pi/2)
			#t1.setFontResolution(256)
			#t1.setFontSize(64)
			t1.setFontSize(fontSize/1.2)
			t1.setScale(1.0/0.0000001, 1.0/0.00001, 1.0/0.00001)
			t1.getMaterial().setTransparent(False)
			t1.getMaterial().setDepthTestEnabled(False)
			t1.setColor(colorWhite)
			wallSystemTextDict[name] = t1
			sSystem.addChild(t1)
			
			
		else:
			setHabitableZone(system, name, theSystem[name].starType)
			
			# text 
			text = ""
			text = str(allSystemsInfo[system][name].systemName) + " (" + str(allSystemsInfo[system][name].starType) + ")"
			if name != "The Sun":
				text = text + " %.3f light years from you!" % (allSystemsInfo[system][name].starDistance * PCtoLY)
			
			t1 = Text3D.create('data/fonts/helvetica.ttf', 1, text)
			t1.setPosition(Vector3(0.35,0.075,0))
			t1.yaw(pi)
			#t1.setFontResolution(256)
			#t1.setFontSize(64)
			t1.setFontSize(fontSize)
			#t1.setScale(1.0/0.0000001, 1.0/0.00001, 1.0/0.00001)
			t1.getMaterial().setTransparent(False)
			t1.getMaterial().setDepthTestEnabled(False)
			t1.setColor(colorWhite)
			t1.setColor(starColor(theSystem[name]))
			screenCenter.addChild(t1)
			
			model = BoxShape.create(100, 25000, 2000)
			
		model.setPosition(pos)
		
		wallSystemsDict[name] = model
		sSystem.addChild(model)
		
		# set effect for the body spheres
		model.setEffect("textured -v emissive -d "+theSystem[name].texture)
	
	# show habitable zones 
	goldiZone = BoxShape.create(4, 25000, (1.0 * (habitableZones[system].habOuter - habitableZones[system].habInner)) * 10)
	if (48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10) >= wallLimit:
		goldiZone.setPosition(Vector3(0.0, 0.0, 48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10))
	else:
		goldiZone.setPosition(Vector3(0.0,0.0, habitableZones[system].habCenter))
	goldiZone.setEffect('colored -e #00440077')
	goldiZone.setScale(1,1,orbitScaleFactor * userScaleFactor)
	goldiZone.getMaterial().setTransparent(True)
	habiWallDict[system] = goldiZone
	sSystem.addChild(goldiZone)
	
	sSystem.yaw(pi/2.0)
	sSystem.setScale(0.0000001, 0.00001, 0.00001)
	
	# add statistics as well
	#
	
	hLoc = h + 0.5
	degreeConvert = 36.0/360.0 * 2 * pi 
	caveRadius = 3.25
	screenCenter.setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v * 0.29 + 0.41, cos(hLoc * degreeConvert) * caveRadius))
	screenCenter.yaw(hLoc * degreeConvert)
	screenCenter.addChild(sSystem)
	screenCenter.addChild(outlineBox)
	#interactor = ToolkitUtils.setupInteractor("config/interactor")
	#interactor.setSceneNode(screenCenter)
	#screenCenter.setSelectable(True)
	#screenCenter.setBoundingBoxVisible(True)
	screenCenter.setTag(system + " box "+str(panelCounter))
	#screenCenter.setScale(2.0, 0.25, 0.001)
	allSystems.addChild(screenCenter)
	
	
			

# Create the 2D systems for the wall
def create2DSystems():
	global panelCounter
	panelCounter = 0
	systemCounter = len(systemList)-1
	systemList.sort()
	for h in xrange(1, 10):
		if (h>=4) and (h<=6):
			continue
		for v in xrange(0, 8):
		#for system in systemList:
			system = systemList[systemCounter]
			systemCounter -= 1
			createEach2DSystem(system, h, v, panelCounter)
			panelCounter += 1
		
# remove the systems from the wall
def reorderAuto2D():
	global allSystems
	list =  getDisplayList()
	t1 = allSystems.numChildren()
	tempList = []
	
	for i in range (0, t1):
		node = allSystems.getChildByIndex(i)
		name = node.getName().strip().split("box")[0]
		if findInList(name, list) == True:
			tempList.append(node)
		else:
			node.setPosition(0,100,10)
	
	counter = len(tempList)-1
	for h in xrange(1, 10):
		if (h>=4) and (h<=6):
			continue
		for v in xrange(0, 8):
			hLoc = h + 0.5
			degreeConvert = 36.0/360.0 * 2 * pi 
			caveRadius = 3.25
			tempList[counter].resetOrientation()
			tempList[counter].setPosition(Vector3(sin(hLoc * degreeConvert) * caveRadius, v * 0.29 + 0.41, cos(hLoc * degreeConvert) * caveRadius))
			tempList[counter].yaw(hLoc * degreeConvert)
			counter = counter - 1
			if counter < 0:
				break
		if counter < 0:
			break
		
# create all the systems in 3D
def create3DSystems():
	theSystem = dict()
	for system in systemList:
		# set the system name 
		#lightsDict["Solar System"].setEnabled(True)
		
		if system == "Solar System":
			star = "The Sun"
		else:
			star = system
			
		# create the objects
		theSystem = allSystemsOrbital[system]
		pos2 = starLocations[system].pos * orbitScaleFactor * userScaleFactor
		#print system + " : " + str(pos2)
		for name, model in theSystem.iteritems():
			pos = Vector3(0,0,0)
			#model = SphereShape.create(1, 4)
			model = StaticObject.create("defaultSphere")
			if theSystem[name].isStar == 0:
				# set the model position depending on the system
				pos = ((Vector3(0.0, 0.0, -theSystem[name].minorA  * orbitScaleFactor * userScaleFactor)))
				model.setPosition(pos)
				# set textures
				model.getMaterial().setProgram("textured")
				model.setEffect("textured -v emissive -d "+theSystem[name].texture)
				model.setScale(Vector3(theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor))
			elif theSystem[name].isStar == 1:
				setHabitableZone(system, name, theSystem[name].starType)
				model.setPosition(Vector3(0,0,0))
				model.setScale(Vector3(theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor))
				sunDot = StaticObject.create("defaultSphere")
				sunDot.setPosition(pos)
				sunDot.setScale(Vector3(1, 1, 1))
				systemNodeDict[system].addChild(sunDot)
				#lightsDict[system].setPosition(pos2)
				# set textures
				model.getMaterial().setProgram("textured")
				model.setEffect("textured -v emissive -d "+theSystem[name].texture)
				
				'''
				sunLine = LineSet.create()
				l = sunLine.addLine()
				l.setStart(Vector3(0,0,0))
				l.setEnd(Vector3(0,1000,0))
				l.setThickness(1)
				sunLine.setEffect('colored -e white')
				systemNodeDict[system].addChild(sunLine)
				'''
				
			model.setTag(str(system) + " : " + str(name) + " RotCenter")
			model.setSelectable(True)
			
			activeBodies[name] = model
			
			planetCenter = SceneNode.create(str(name) + "PlanetCenter")
			
			# deal with the axial tilt of the bodies
			tiltCenter = SceneNode.create(str(name) + "TiltCenter")
			planetCenter.addChild(tiltCenter)
			tiltCenter.addChild(model)
#			if theSystem[name].isStar == 1:
#				tiltCenter.addChild(lightsDict[system])
			tiltCenter.roll(theSystem[name].inclination/180.0*pi)
			
			
			if name == "Saturn":
				rings = CylinderShape.create(1, 80000, 80000, 10, 128)
				rings.setEffect('colored -e #88888866')
				rings.setScale(planetScaleFactor, planetScaleFactor, planetScaleFactor)
				rings.getMaterial().setTransparent(True)
				rings.setPosition(Vector3(0,0,-theSystem[name].minorA * orbitScaleFactor*userScaleFactor))
				rings.pitch((-pi * 0.5))
				otherObjectsDict[name] = rings
				tiltCenter.addChild(rings)
			
			
			
			#deal with rotating the planets around the sun
			rotCenter = SceneNode.create(str(system) + " : " + str(name) + " RotCenter")
			rotCenter.setTag(str(system) + " : " + str(name) + " RotCenter")
			rotCenter.setPosition(pos2)
			rotCenter.addChild(planetCenter)
			#rotCenter.setSelectable(True)
			
			activeRotCenters[name] = rotCenter
			systemNodeDict[system].addChild(rotCenter)
			
			# add orbit
			addOrbit(theSystem[name].minorA * orbitScaleFactor * userScaleFactor, 0, 0.001, system, name)
			
			# deal with labelling everything
			v = Text3D.create('data/fonts/helvetica.ttf', 1, str(name))
			if system == "Solar System":
				if theSystem[name].isStar == 0:
					pos1 = Vector3(0, theSystem[name].radius * planetScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
				else:
					pos1 = Vector3(0, theSystem[name].radius * sunScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			else:
				if theSystem[name].isStar == 0:
					pos1 = Vector3(0, theSystem[name].radius * planetScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
				else:
					pos1 = Vector3(0, theSystem[name].radius * sunScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			v.setPosition(pos1)
			#v.setFontResolution(120)
			v.setFontSize(180)
			v.getMaterial().setDoubleFace(1)
			v.setFixedSize(False)
			v.setColor(Color('white'))
			planetCenter.addChild(v)
			textDict[name] = v
			orientObjects.append(v)
			
		# deal with the goldilocks zones
		
		#if habitableZones[system].habCenter != 0:
		#	addOrbit(habitableZones[system].habCenter, 1, habitableZones[system].habWidth, system, system)
		#else:
		#	addOrbit(habitableZones[system].habCenter * orbitScaleFactor * userScaleFactor, 1, (habitableZones[system].habWidth) * orbitScaleFactor * userScaleFactor, system, system)
		#print str(habitableZones[system].habCenter * orbitScaleFactor * userScaleFactor) + " : " + str(habitableZones[system].habWidth * orbitScaleFactor * userScaleFactor)
		#for l in habiInnerDict[system]:
		#	if habitableZones[system].habCenter != 0:
			#print habitableZones[system].habWidth / habitableZones[system].habCenter
			#l.setThickness(1)
		
		inner = CylinderShape.create(1, habitableZones[system].habInner, habitableZones[system].habInner, 10, 128)
		inner.setEffect('colored -e #FF000044')
		inner.getMaterial().setTransparent(True)
		inner.pitch(-pi * 0.5)
		inner.setScale(Vector3(orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor,0.5))
		habiInnerDict[system] = inner
		
		outer = CylinderShape.create(1, habitableZones[system].habOuter, habitableZones[system].habOuter, 10, 128)
		outer.setEffect('colored -e #00FF0044')
		outer.getMaterial().setTransparent(True)
		outer.pitch(-pi * 0.5)
		outer.setScale(Vector3(orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor,0.1))
		habiOuterDict[system] = outer
		
		
		if system != "Solar System":
			inner.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
			outer.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
		
		gZone = SceneNode.create("GZone")
		gZone.addChild(outer)
		gZone.addChild(inner)
		
		systemNodeDict[system].addChild(gZone)
		#systemNodeDict[system].addChild()
		
	universe.setScale(Vector3(overallScaleFactor, overallScaleFactor, overallScaleFactor))
	universe.setPosition(Vector3(0, 1.5, 1))

	
def updateOrbitScale(scale):
	global orbitScaleFactor
	orbitScaleFactor = 1.0/pow(10, scale)

	for system in systemList:
		theSystem = allSystemsOrbital[system]
		for name, model in theSystem.iteritems():
			pos = Vector3(0.0, 0.0, -theSystem[name].minorA  * orbitScaleFactor * userScaleFactor)
			pos2 = starLocations[system].pos  * orbitScaleFactor * userScaleFactor
			pos3 = habitableZones[system].habCenter * orbitScaleFactor * userScaleFactor
			pos1 = habitableZones[system].habWidth * orbitScaleFactor * userScaleFactor * 0.00015
			pos2_1 = theSystem[name].minorA * orbitScaleFactor * userScaleFactor
			if theSystem[name].isStar == 0:
				pos4 = Vector3(0, theSystem[name].radius * planetScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			else:
				pos4 = Vector3(0, theSystem[name].radius * sunScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
			if (48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10) >= wallLimit:
				pos5 = Vector3(0.0, 0.0, 48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10)
				pos6 = Vector3(0.0, -10000.0, 48000 - theSystem[name].minorA * orbitScaleFactor * userScaleFactor * 10)
			else:
				pos5 = Vector3(0.0, 0.0, wallLimit)
				pos6 = Vector3(0.0, -10000.0,wallLimit)
			if (48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10) >= wallLimit:
				pos7 = Vector3(0.0, 0.0, 48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10)
			else:
				pos7 = Vector3(0.0,0.0, habitableZones[system].habCenter)
			#pos7 = Vector3(0.0, 0.0, 48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10)
			pos8 = starLocations[system].pos * orbitScaleFactor * userScaleFactor * 0.000000001
			
			#activeRotCenters[name].setPosition(pos2)
			orbitDict[name].setScale(Vector3(pos2_1, 10.0, pos2_1))
			textDict[name].setPosition(pos4)
			wallSystemsDict[name].setPosition(pos5)
			if theSystem[name].isStar == 0:
				wallSystemTextDict[name].setPosition(pos6)
				activeBodies[name].setPosition(pos)
			if name == "Saturn":
				otherObjectsDict[name].setPosition(pos)
			habiInnerDict[system].setScale(orbitScaleFactor * userScaleFactor, orbitScaleFactor * userScaleFactor, 0.3)
			habiOuterDict[system].setScale(orbitScaleFactor * userScaleFactor, orbitScaleFactor * userScaleFactor, 0.001)
			habiWallDict[system].setPosition(pos7)
			habiWallDict[system].setScale( 1,1 ,  orbitScaleFactor * userScaleFactor )
			visualizeDict[system].setPosition(pos8)
			visualizeTextDict[system].setPosition(pos8)
			
def updatePlanetScale(scale):
	global planetScaleFactor
	planetScaleFactor = 1.0/pow(10, scale)
	
	for system in systemList:
		theSystem = allSystemsOrbital[system]
		for name, model in theSystem.iteritems():
			if theSystem[name].isStar == 0:
				activeBodies[name].setScale(Vector3(theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor))
				pos = Vector3(0, theSystem[name].radius * planetScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
				textDict[name].setPosition(pos)
			if name == "Saturn":
				otherObjectsDict[name].setScale(planetScaleFactor, planetScaleFactor, planetScaleFactor)
				
	
def updateSunScale(scale):
	global sunScaleFactor
	sunScaleFactor = 1.0/pow(10, scale)
	
	for system in systemList:
		theSystem = allSystemsOrbital[system]
		for name, model in theSystem.iteritems():
			if theSystem[name].isStar == 1:
				activeBodies[name].setScale(Vector3(theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor))
				pos = Vector3(0, theSystem[name].radius * sunScaleFactor, - theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
				textDict[name].setPosition(pos)

def setInfoVisible(val, name):
	global infoContainer, planetInfo
	infoContainer.setVisible(val)
	infoContainer.setChildrenVisible(val)
	caveutil.orientWithHead(getCam(), infoContainer)
	
	if val == True:
		planetInfo = SceneNode.create("Planet info")
		planetInfo.setPosition(Vector3(0,0,0))
		infoContainer.addChild(planetInfo)
		showInfo(name)
		list = getTexts()
		counter = 0
		for text in list:
			tObj = Text3D.create('data/fonts/helvetica.ttf', 1, text)
			tObj.setPosition(0,counter,0)
			tObj.yaw(pi/2)
			tObj.setFontResolution(256)
			tObj.setFontSize(fontSize/1.2)
			tObj.setScale(1.0/0.0000001, 1.0/0.00001, 1.0/0.00001)
			tObj.getMaterial().setTransparent(False)
			tObj.getMaterial().setDepthTestEnabled(False)
			tObj.setColor(colorWhite)
			planetInfo.addChild(tObj)
			counter = counter + 1
	else:
		pass
		#if infoContainer.getChildByName("Planet info") != None:
		#	infoContainer.removeChildByName("Planet info")
		
def getInfoContainer():
	global infoContainer
	return infoContainer
	
def createInfoDisplay():
	global infoContainer, infoDisplayBox, planetInfo, systemInfo
	global text1, text2, text3, text4, text5, text6, text7, text8, text9, text10
	
	infoDisplayBox = BoxShape.create(1.0, 1.0, 0.001)
	infoDisplayBox.setPosition(Vector3(0,0,0))
	infoDisplayBox.setEffect('colored -e #111111EE')
	infoDisplayBox.getMaterial().setTransparent(False)
	
	systemInfo = SceneNode.create("system info")
	systemInfo.setPosition(Vector3(0,0,0))
	
	infoContainer = SceneNode.create("Info Container")
	infoContainer.addChild(infoDisplayBox)
	
	infoContainer.setPosition(xMin, yMax, zMin)
	allSystems.addChild(infoContainer)
	#infoContainer.yaw(6.5 * 36.0/360.0 * 2 * pi)
	
	
		
	

def showInfo(name):
	global planetInfo, systemInfo
	global text1, text2, text3, text4, text5, text6, text7, text8, text9, text10
	print "Step show Info  : " + str(name)
	if name.find("RotCenter") != -1:
		print name
		bodyName = name.strip().split("RotCenter")[0].strip().split(":")[1].strip()
		bodyName = bodyName.strip()
		systemName = name.strip().split("RotCenter")[0].strip().split(":")[0].strip()
		systemName = systemName.strip()
		radius = allSystemsOrbital[systemName][bodyName].radius
		mass = allSystemsInfo[systemName][bodyName].mass
		majorA = allSystemsOrbital[systemName][bodyName].majorA
		minorA = allSystemsOrbital[systemName][bodyName].minorA
		period = allSystemsOrbital[systemName][bodyName].period
		rot = allSystemsOrbital[systemName][bodyName].rotation
		discovered = allSystemsInfo[systemName][bodyName].discovered
		detection = allSystemsInfo[systemName][bodyName].detectionType
		molecules = allSystemsInfo[systemName][bodyName].molecules
		starType = allSystemsInfo[systemName][bodyName].starType
		starAge = allSystemsInfo[systemName][bodyName].starAge
		starDistance = allSystemsInfo[systemName][bodyName].starDistance
		planetInfo.setVisible(True)
		planetInfo.setChildrenVisible(True)
		systemInfo.setVisible(False)
		systemInfo.setChildrenVisible(False)
		if allSystemsOrbital[systemName][bodyName].isStar == 0: 
			if minorA != 0.0: 
				text4 = "Distance to Star: %.3f AU" % (minorA/AUtoKM)
				infoTextList.append(text4)
			if rot != 0.0: 
				text5 = "Rotation Period: " + str(rot) + " days"
				infoTextList.append(text5)
			if period != 0.0: 
				text6 = "Revolution Period: " + str(period) + " years"
				infoTextList.append(text6)
		else:
			text4 = "Star type: " + str(starType)
			if starAge != 0.0: text5 = "Star Age: " + str(starAge)
		text1 = bodyName + " ( " + systemName + " System )"
		infoTextList.append(text1)
		if radius != 0.0: 
			text2 = "Radius: %.2f AU" % (radius/AUtoKM)
			infoTextList.append(text2)
		if mass != "": 
			text3 = "Mass: " + str(mass)
			infoTextList.append(text3)
		if discovered != 0: 
			text7 = "Discovered: " + str(discovered)
			infoTextList.append(text7)
		if detection != "": 
			text8 = "Detection Type: " + str(detection)
			infoTextList.append(text8)
		if molecules != "": 
			text9 = "Molecules: " + str(molecules)
			infoTextList.append(text9)
		
	
def getTexts():
	global infoTextList
	return infoTextList
	
'''
def drawMidWindowOutline():
	print "drawing mid window outline"
	
	# initialize mid Window outline when dragged
	midWindowOutline = BoxShape.create(xMax-xMin, yMax-yMin, 0.01)
	midWindowOutline.setPosition(Vector3(xMin + (xMax-xMin)/2, yMin + (yMax - yMin)/2, -2))
	midWindowOutline.setEffect('colored -e #DDDDAA44')
	midWindowOutline.getMaterial().setTransparent(True)
	allSystems.addChild(midWindowOutline)

	deleteWindowOutline = BoxShape.create(xMax-xMin, yMax2-yMin2, 0.01)
	deleteWindowOutline.setPosition(Vector3(xMin + (xMax-xMin)/2, yMin2 + (yMax2 - yMin2)/2, -2))
	deleteWindowOutline.setEffect('colored -e #DD333344')
	deleteWindowOutline.getMaterial().setTransparent(True)
	allSystems.addChild(deleteWindowOutline)

	
def removeMidWindowOutline():
	global midWindow
	midWindow - SceneNode.create("mid window")

'''

def setWallTilePosAfterMove(wandRay, wandPos, objectPos, objectOrient, intersectObj):
	global xMin, xMax, yMix, yMax, yMin2, yMax2, zMin, zMax
	
	print "positioning obj"
	print "Wand Ray : " + str(wandRay)
	print "wandPos : " + str(wandPos)
	name = intersectObj.getName().strip().split("box")[0].strip()
	
	if (intersectObj.getPosition().x >= xMin) and (intersectObj.getPosition().x <= xMax):
		if (intersectObj.getPosition().y >= yMin) and (intersectObj.getPosition().y <= yMax):
			print "visiting system"
			intersectObj.setPosition(objectPos)
			intersectObj.setOrientation(objectOrient)
			visitSystem(name.strip())
		
		if (intersectObj.getPosition().y >= yMin2) and (intersectObj.getPosition().y <= yMax2):
			displaySystemList.remove(name)
			userList = displaySystemList
			updateList(5)
	