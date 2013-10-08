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
	scene.setBackgroundColor(colorWhite)
	setNearFarZ(0.1, 1000000)

def loadSphereModel():
	global scene
	sphereModel = ModelInfo()
	sphereModel.name = "defaultSphere"
	sphereModel.path = "data/sphere/sphere.obj"
	scene.loadModel(sphereModel)


# method for creating all the systems in 3D
def create3DSystems():
	for system in systemList:
		if system == "Solar System":
			lightsDict[system].setEnabled = True
			star = "The Sun"
			theSystem = allSystemsOrbital[system]
			for name, model in theSystem.iteritems():
				pos = Vector3(0,0,0)
				model = StaticObject.create("defaultSphere")
				if theSystem[name].isStar == 0:
					model.setPosition(Vector3(0.0, 0.0, -theSystem[name].minorA * orbitScaleFactor * userScaleFactor))
					model.setScale(Vector3(theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor, theSystem[name].radius * planetScaleFactor))
				else:
					# setHabitableZone() ????
					pos = Vector3(0.0, 0.0, -theSystem[name].minorA * orbitScaleFactor * userScaleFactor)
					lightsDict[system].setPosition(pos)
					model.setPosition(pos)
					model.setScale(Vector3(theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor, theSystem[name].radius * sunScaleFactor))
					sunDot = StaticObject.create("defaultSphere")
					sunDot.setPosition(Vector3(0.0, 0.0, -theSystem[name].minorA * orbitScaleFactor * userScaleFactor))
					sunDot.setScale(Vector3(1, 1, 1))
					systemNodeDict[system].addChild(sunDot)
					
					sunLine = LineSet.create()
					l = sunLine.addLine()
					l.setStart(Vector3(0,0,0))
					l.setEnd(Vector3(0,1000,0))
					l.setThickness(1)
					sunLine.setEffect('colored -e white')
					systemNodeDict[system].addChild(sunLine)
					
				model.getMaterial().setProgram("textured")
				if theSystem[name].isStar == 0:
					model.setEffect("textured -v emissive -d data/textures/planets/"+str(theSystem[name].name.lower())+".jpg")
				else:
					model.setEffect("textured -v emissive -d data/textures/stars/sol.png")
				activeBodies[name] = model
				
				planetCenter = SceneNode.create(str(name) + "PlanetCenter")
				# deal with the axial tilt of the bodies
				tiltCenter = SceneNode.create(str(name) + "TiltCenter")
				planetCenter.addChild(tiltCenter)
				tiltCenter.addChild(model)
				tiltCenter.roll(theSystem[name].inclination/180.0*pi)
				
				#deal with rotating the planets around the sun
				rotCenter = SceneNode.create(str(name) + "RotCenter")
				rotCenter.setPosition(pos)
				rotCenter.addChild(planetCenter)
				
				activeRotCenters[name] = rotCenter
				#systemNodeDict[system].addChild(rotCenter)
				
				
				
	
		else:
			star = system
			
	allSystems.setScale(Vector3(overallScaleFactor, overallScaleFactor, overallScaleFactor))
	allSystems.setPosition(Vector3(0, 1.5, 1))
	
def onUpdate(frame, t, dt):
    for name,model in allSystemsOrbital["Solar System"].iteritems():
		activeRotCenters[name].yaw(dt/40*(1.0 / allSystemsOrbital["Solar System"][name].period)) #revolution (year)
		activeBodies[name].yaw(dt/40*365*(1.0 / allSystemsOrbital["Solar System"][name].rotation)) #rotation (day) 

	
# Main ----------------------------------------------------------
# initialize database
initDB()
getData()

# setting up initial scene hierarchy
# level 1
allSystems = SceneNode.create('allSystems')
systemNodeDict = dict()
for system in systemList:
	temp = SceneNode.create(system)
	systemNodeDict[system] = temp

# level 2
universe = SceneNode.create('universe')
for system in systemList:
	universe.addChild(systemNodeDict[system])
thingsOnTheWall = SceneNode.create('thingsOnTheWall')
thingsOnTheWall.addChild(allSystems)

# level 3
everything = SceneNode.create('everything')
everything.addChild(universe)
everything.addChild(thingsOnTheWall)

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
	everything.addChild(light)

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

# make wall systems static. Add "thingsOnTheWall" to the cam
getDefaultCamera().addChild(thingsOnTheWall)

# initialize the scene
initializeScene()

# initialize and set skybox
setSkyBox()

# load sphere into the scene
loadSphereModel()

# now create the systems in 3D space
create3DSystems()

# set update function
setUpdateFunction(onUpdate)