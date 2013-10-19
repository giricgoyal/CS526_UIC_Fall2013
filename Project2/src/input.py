# ------------------------------------------------------------------------------------------
# imports
from math import *
from euclid import *
from omega import *
from cyclops import *
from util import *
from wandaid import *
from system import *
from cameraManager import *


# -----------------------------------------------------------------------------------------
# variables
e = None
sourceId = None
wandPos = None
wandRay = None
wandID = caveutil.WAND1
intersectObj = None
intersectDist = None



# ---------------------------------------------------------------------------------------
# methods
'''
def initInput(scene, cam):
	wandaid.init(scene, cam)
	wandaid.setJoystickLabel("Drive")
	wandaid.setShoulderLabel("Rotate")
	wandaid.setTriggerLabel("Fly")
	wandaid.setLeftButtonLabel("Menu Select")
	wandaid.setRightButtonLabel("Menu Open")
	wandaid.setDPADUpLabel("Scale Up")
	wandaid.setDPADDownLabel("Scale Down")
	wandaid.setDPADLeftLabel("Left")
	wandaid.setDPADRightLabel("Right")
	wandID = 1
	'''
	

def getIntersectObj():
	global intersectObj
	return intersectObj

def getIntersectDist():
	global intersectDist
	return intersectDist
	
def handleEvent():
	global e, sourceId, wandPos, wandRay, intersectObj, intersectDist
	
	objectPos = None
	objectOrient = None
	
	e = getEvent()
	#sourceId = getSourceId()
	
	if e.isButtonDown(EventFlags.Button5):
		drawMidWindowOutline()
		wandPos = caveutil.getWandWorldPosition(getCam(), wandID)
		wandRay = caveutil.getWandRay(getCam(), wandID)
		intersectObj, intersectDist = caveutil.getNearestIntersectingObject(wandPos, wandRay)
		if (intersectObj != None):
			if intersectObj.getName().find("box") != -1:
				objectPos = intersectObj.getPosition()
				objectOrient = interctObj.getOrientation()
				setIsMovingTile(True)
		
	if e.isButtonUp(EventFlags.Button5):
		removeMidWindowOutline()
		wandPos = caveutil.getWandWorldPosition(getCam(), wandID)
		wandRay = caveutil.getWandRay(getCam(), wandID)
		setIsMovingTile(False)
		setWallTilePosAfterMove(wandRay, wandPos, objectPos, objectOrient, intersectObj) 
		

setEventFunction(handleEvent)
