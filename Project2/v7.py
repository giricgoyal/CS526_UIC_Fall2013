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
from src.system import *
from src.input import *


# ---------------------------------------------------------------
# Variables

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


def onUpdate(frame, t, dt):
	for system in systemList:
		for name,model in allSystemsOrbital[system].iteritems():
			timeF = getTimeFactor()
			activeRotCenters[name].yaw(dt/timeF*(1.0 / allSystemsOrbital[system][name].period)) #revolution (year)
			activeBodies[name].yaw(dt/timeF*365*(1.0 / allSystemsOrbital[system][name].rotation)) #rotation (day) 
	
	for obj in orientObjects:
		obj.setFacingCamera(getCam())
		#caveutil.orientWithHead(getCam(), obj)
		
	if getIsMovingTile() == True:
		setInfoVisible(False)
		caveutil.positionAtWand(getCam(), getIntersectObj(), wandID, getIntersectDist())
		caveutil.orientWithHead(getCam(), getIntersectObj())
		print getIntersectObj().getPosition()
	
	if getIsMovingTile() == False:
		wandPos = caveutil.getWandWorldPosition(getCam(), wandID)
		wandRay = caveutil.getWandRay(getCam(), wandID)
		intersectObj, intersectDist = caveutil.getNearestIntersectingObject(wandPos, wandRay)
		if intersectObj != None:
			name = intersectObj.getName()
			if name.find("RotCenter") != -1:
				print name
				showInfo(name)
				setInfoVisible(True)
				if isCave == True: caveutil.positionAtWand(getCam(), getInfoContainer(), wandID, 3)
			else:
				setInfoVisible(False)
		else:
			setInfoVisible(False)
		

# Main ----------------------------------------------------------
# initialize database
initDB()
getData()


# lights for each system


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
if isCave == True: getDefaultCamera().addChild(thingsOnTheWall)

# initialize the scene
initializeScene()

# initialize and set skybox
setSkyBox()

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

# initialize input
#initInput(scene, cam)

# create info display
createInfoDisplay()


# set update function
setUpdateFunction(onUpdate)