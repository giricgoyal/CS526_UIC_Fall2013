# ------------------------------------------------------
# 	cameraManager.py for managing camera
#	Author : Giric Goyal
# ------------------------------------------------------

# ------------------------------------------------------
# imports

from math import *
from euclid import *
from omega import *
from cyclops import *
from caveutil import *
from util import *


# ------------------------------------------------------
# variables
cam = None
orient3D = None
pos3D = None
obj = None
currentPos = None
camPos = None

# ------------------------------------------------------
# methods

def initCam():
	print "Initializing Cam"
	global cam, orient3D, pos3D, orient2D, pos2D, obj
	cam = getDefaultCamera()
	#cam.setPosition(Vector3(0,10,0))
	#cam.pitch(-pi/2)
	cam.getController().setSpeed(camSpeed)
	orient3D = cam.getOrientation()
	pos3D = cam.getPosition()
	obj = InterpolActor(cam)
	obj.setDuration(3)
	obj.setOperation(InterpolActor.POSITION | InterpolActor.ORIENT | InterpolActor.SCALE)


	
def setCamPosition(pos):
	global cam, obj, orient3D
	#obj.setTargetPosition(pos * overallScaleFactor + pos3D)
	#obj.setTargetOrientation(orient3D)
	cam.setPosition(pos * overallScaleFactor + pos3D)
	cam.setOrientation(orient3D)
	#obj.startInterpolation()

def setCamPosition2(pos):
	global cam
	cam.setPosition(pos)
	cam.setOrientation(orient3D)

def setCamPos():
	global camPos
	camPos = cam.getPosition()
	
def getCamPosition():
	return camPos
	
def getCam():
	return cam
	
