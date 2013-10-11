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
orient2D = None
pos2D = None
# ------------------------------------------------------
# methods
obj = InterpolActor(cam)
obj.setDuration(3)
obj.setOperation(InterpolActor.POSITION | InterpolActor.ORIENT | InterpolActor.SCALE)

def initCam():
	global cam, orient3D, pos3D, orient2D, pos2D
	cam = getDefaultCamera()
	cam.setPosition(Vector3(0,0,0))
	cam.getController().setSpeed(10000)
	orient3D = cam.getOrientation()
	pos3D = cam.getPosition()
	orient2D = cam.getOrientation()
	pos2D = cam.getPosition()
	
def setCamPosition(pos):
	global cam
	cam.setPosition(pos)