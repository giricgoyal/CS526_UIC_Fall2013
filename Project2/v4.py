# ##################################################
#	Project 2: Straight Away to Orion
#	CS526, UIC Fall 2013
#
#	Author: Giric Goyal
#
#
# Some information
# ----------------
# V main sequence (O B A F G K M etc)
# III Giants (G K M)
# I super giants (B A F G K M)
# main sequence stars become brighter and hotter as they age
#
# earth-size < 1.25 Rearth
# super earth-size 1.25 - 2 Rearth
# neptune-size 2 - 6 Rearth
# jupiter-size  6 - 15 Rearth
# larger than jupiter-size > 15 Rearth
#
# 1AU = 149597871 km
#
# ##################################################

# ---------------------------------------------------------------
# imports
from math import *
from euclid import *
from omega import *
from cyclops import *
from src.util import *
from src.manageData import *
from src.cameraManager import *
from src.menuManager import *
from src.visualize import *


# ---------------------------------------------------------------
# Variables

skyBox = None
scene = None


# -------------------------------------------------------------------
# method definitions
def setSkyBox():
	global skyBox
	skyBox = Skybox()
	skyBox.loadCubeMap("data/stars", "png")
	getSceneManager().setSkyBox(skyBox)

def initializeScene():
	global scene
	scene = getSceneManager()
	scene.setBackgroundColor(colorBlack)
	setNearFarZ(0.1, 1000000)

def loadSphereModel():
	global scene
	sphereModel = ModelInfo()
	sphereModel.name = "defaultSphere"
	sphereModel.path = "data/sphere/sphere.obj"
	scene.loadModel(sphereModel)

	
# Calculate habitable zones
def setHabitableZone(system, starName, starType):
	habObj = habZone(starName, starType)
	habObj.calHabitableZone()
	habitableZones[system] = habObj
	
	
def addOrbit(orbit, col, thick, system, name):
	circle = LineSet.create()
	segments = 128
	radius = 1
	thickness = thick
	
	# need to think about elliptical orbit, for now circular based on minorA
	a = 0.0
	while a <= 360:
		x = cos(radians(a)) * radius
		y = sin(radians(a)) * radius
		a += 360.0/segments
		nx = cos(radians(a)) * radius
		ny = sin(radians(a)) * radius
		
		l = circle.addLine()
		l.setStart(Vector3(x, 0, y))
		l.setEnd(Vector3(nx, 0, ny))
		l.setThickness(thickness)
		
		if system == "Solar System":
			circle.setPosition(Vector3(0,0,0))
		else:
			circle.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
		
		if col == 0:
			circle.setEffect('colored -e white')
		else:
			circle.setEffect('colored -e green')
			
        # Squish z to turn the torus into a disc-like shape.

		if col == 0:
			circle.setScale(Vector3(orbit, 1000.0, orbit))
		else:
			circle.setScale(Vector3(orbit, 10.0, orbit)) # 0.1
	orbitDict[name] = circle
	systemNodeDict[system].addChild(circle)



def create2DSystems():
	panelCounter = 0
	systemCounter = len(systemList)-1
	for h in xrange(1, 10):
		if (h>=4) and (h<=6):
			continue
		for v in xrange(0, 8):
		#for system in systemList:
			system = systemList[systemCounter]
			systemCounter -= 1
			
			theSystem = allSystemsOrbital[system]
			
			outlineBox = BoxShape.create(2.0, 0.25, 0.001)
			outlineBox.setPosition(Vector3(-0.5, 0, 0.01))
			outlineBox.setEffect('colored -e #111111EE')
			outlineBox.getMaterial().setTransparent(False)
			screenCenter = SceneNode.create("box"+str(panelCounter))
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
					model = StaticObject.create("defaultSphere")
					model.setScale(Vector3(theSystem[name].radius * XplanetScaleFactor, theSystem[name].radius * XplanetScaleFactor, theSystem[name].radius * XplanetScaleFactor))
					
					# text 
					text = str(name)
					
					t1 = Text3D.create('fonts/verdana.ttf', 1, text)
					t1.setPosition(pos2)
					t1.yaw(pi/2)
					t1.setFontResolution(256)
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
					
					t1 = Text3D.create('fonts/verdana.ttf', 1, text)
					t1.setPosition(Vector3(0.35,0.075,0))
					t1.yaw(pi)
					t1.setFontResolution(256)
					t1.setFontSize(fontSize)
					t1.getMaterial().setTransparent(True)
					t1.getMaterial().setDepthTestEnabled(False)
					t1.setColor(starColor(theSystem[name]))
					screenCenter.addChild(t1)
					
					model = BoxShape.create(100, 25000, 2000)
					
				model.setPosition(pos)
				
				wallSystemsDict[name] = model
				sSystem.addChild(model)
				
				# set effect for the body spheres
				model.setEffect("textured -v emissive -d "+theSystem[name].texture)
				
				panelCounter += 1
			
			# show habitable zones 
			goldiZone = BoxShape.create(4, 25000, (1.0 * (habitableZones[system].habOuter - habitableZones[system].habInner)) * 10)
			if (48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10) >= wallLimit:
				goldiZone.setPosition(Vector3(0.0, 0.0, 48000 - habitableZones[system].habCenter *  orbitScaleFactor * userScaleFactor  * 10))
			sSystem.addChild(goldiZone)
			goldiZone.setEffect('colored -e #00440077')
			goldiZone.setScale(1,1,orbitScaleFactor * userScaleFactor)
			goldiZone.getMaterial().setTransparent(True)
			habiWallDict[system] = goldiZone
			
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
			allSystems.addChild(screenCenter)
			
			#if v == 8:
			#	h += 1
			#	v = 0
			#v += 1
		
# method for creating all the systems in 3D
def create3DSystems():
	theSystem = dict()
	for system in systemList:
		# set the system name 
		#lightsDict[system].setEnabled = True
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
			model = StaticObject.create("defaultSphere")
			if theSystem[name].isStar == 0:
				# set the model position depending on the system
				pos = ((Vector3(0.0, 0.0, -theSystem[name].minorA  * orbitScaleFactor * userScaleFactor)))
				model.setPosition(pos)
				model.setScale(Vector3(theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor))
			elif theSystem[name].isStar == 1:
				setHabitableZone(system, name, theSystem[name].starType)
				model.setPosition(Vector3(0,0,0))
				model.setScale(Vector3(theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor))
				sunDot = StaticObject.create("defaultSphere")
				sunDot.setPosition(pos)
				sunDot.setScale(Vector3(1, 1, 1))
				systemNodeDict[system].addChild(sunDot)
				
				sunLine = LineSet.create()
				l = sunLine.addLine()
				l.setStart(Vector3(0,0,0))
				l.setEnd(Vector3(0,1000,0))
				l.setThickness(1)
				sunLine.setEffect('colored -e white')
				systemNodeDict[system].addChild(sunLine)
			
			# set textures
			model.getMaterial().setProgram("textured")
			model.setEffect("textured -v emissive -d "+theSystem[name].texture)
			activeBodies[name] = model
			
			
			planetCenter = SceneNode.create(str(name) + "PlanetCenter")
			
			
			# deal with the axial tilt of the bodies
			tiltCenter = SceneNode.create(str(name) + "TiltCenter")
			planetCenter.addChild(tiltCenter)
			tiltCenter.addChild(model)
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
			rotCenter = SceneNode.create(str(name) + "RotCenter")
			rotCenter.setPosition(pos2)
			rotCenter.addChild(planetCenter)
			
			activeRotCenters[name] = rotCenter
			systemNodeDict[system].addChild(rotCenter)
			
			# add orbit
			addOrbit(theSystem[name].minorA*orbitScaleFactor*userScaleFactor, 0, 0.001, system, name)
			
			# deal with labelling everything
			v = Text3D.create('fonts/verdana.ttf', 1, str(name))
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
			v.setFontResolution(120)
			v.setFontSize(180)
			v.getMaterial().setDoubleFace(1)
			v.setFixedSize(False)
			v.setColor(Color('white'))
			planetCenter.addChild(v)
			textDict[name] = v
			
		# deal with the goldilocks zones
		inner = CylinderShape.create(1, habitableZones[system].habInner, habitableZones[system].habInner, 10, 128)
		inner.setEffect('colored -e #FF000044')
		inner.getMaterial().setTransparent(True)
		inner.pitch(-pi * 0.5)
		inner.setScale(Vector3(orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor))
		habiInnerDict[system] = inner
		
		outer = CylinderShape.create(1, habitableZones[system].habOuter, habitableZones[system].habOuter, 10, 128)
		outer.setEffect('colored -e #00FF0044')
		outer.getMaterial().setTransparent(True)
		outer.pitch(-pi * 0.5)
		outer.setScale(Vector3(orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor,orbitScaleFactor * userScaleFactor))
		habiOuterDict[system] = outer
		
		if system != "Solar System":
			inner.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
			outer.setPosition(starLocations[system].pos * orbitScaleFactor * userScaleFactor)
			
		gZone = SceneNode.create("GZone")
		gZone.addChild(outer)
		gZone.addChild(inner)
		
		systemNodeDict[system].addChild(gZone)
		systemNodeDict[system].addChild(lightsDict[system])
		
	universe.setScale(Vector3(overallScaleFactor, overallScaleFactor, overallScaleFactor))
	universe.setPosition(Vector3(0, 1.5, 1))
	

	
def onUpdate(frame, t, dt):
	for system in systemList:
		for name,model in allSystemsOrbital[system].iteritems():
			timeF = getTimeFactor()
			activeRotCenters[name].yaw(dt/timeF*(1.0 / allSystemsOrbital[system][name].period)) #revolution (year)
			activeBodies[name].yaw(dt/timeF*365*(1.0 / allSystemsOrbital[system][name].rotation)) #rotation (day) 
			
	
# Main ----------------------------------------------------------
# initialize database
initDB()
getData()


# lights for each system

lightsDict = dict()
for system in systemList:
	light = Light.create()
	light.setLightType(LightType.Point)
	lightsDict[system] = light
	# call these while creating the systems
	#light.setPosition(Vector3(0,0,0))
	#light.setPositionVector3(,,)) ----- set position for each to the position of the star
	#light.setColor(Color(,,,)) -------- set color for each to the color of the star
	#light.setEnabled(True)
	
	#add lights to the scene Node "everything"
	#everything.addChild(light)

# set light color for each star type
for name,model in lightsDict.iteritems():
	color = Color(1,1,1,1)
	if name == "Solar System":
		type = allSystemsOrbital[name]["The Sun"].starType
	else:
		type = allSystemsOrbital[name][name].starType
	if type.find('O') != -1:
		color = colorO
	if type.find('B') != -1:
		color = colorB
	if type.find('A') != -1:
		color = colorA
	if type.find('F') != -1:
		color = colorF
	if type.find('G') != -1:
		color = colorG
	if type.find('K') != -1:
		color = colorK
	if type.find('M') != -1:
		color = colorK
	lightsDict[name].setColor(color)


# initialize camera
initCam()

# initialize scene nodes
initSceneNodes()

# make wall systems static. Add "thingsOnTheWall" to the cam
#getDefaultCamera().addChild(thingsOnTheWall)


# initialize the scene
initializeScene()

# initialize and set skybox
#setSkyBox()

# load sphere into the scene
loadSphereModel()

# now create the systems in 3D space
create3DSystems()

# create the systems in 2D space
create2DSystems()

# create visualization of stars 
createVisualization()

# initialize menu 
initButtons()

# set update function
setUpdateFunction(onUpdate)