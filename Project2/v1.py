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


# -------------------------------------------------------------------
# method definitions
def setSkyBox():
	global skyBox
	skyBox = Skybox()
	skyBox.loadCubeMap("data/stars", "png")
	getSceneManager().setSkyBox(skyBox)
	

# Main ----------------------------------------------------------
# initializing database
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
	#light.setPositionVector3(,,)) ----- set position for each to the position of the star
	#light.setColor(Color(,,,)) -------- set color for each to the color of the star
	#light.setEnabled(True)
	
	#add lights to the scene Node "everything"
	everything.addChild(light)

for name,model in lightsDict.iteritems():
	color = Color(1,1,1,1)
	if name == "Solar System":
		type = allSystemsOrbital[name]["The Sun"].starType
	else:
		type = allSystemsOrbital[name][name].starType
	print type
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

	
		
	

# initialize camera
initCam()

# make wall systems static. Add "thingsOnTheWall" to the cam
getDefaultCamera().addChild(thingsOnTheWall)

# initialize and set skybox
setSkyBox()

