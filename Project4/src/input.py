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
from menuManager import *
from datetime import datetime


# -----------------------------------------------------------------------------------------
# variables
e = None
sourceId = None
wandPos = None
wandRay = None
wandID = caveutil.WAND1
intersectObj = None
intersectDist = None
objectPos = None
objectOrient = None
counter = None

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

def setIntersectObj(obj):
	global intersectObj
	intersectObj = obj
	
def setIntersectDist(dist):
	global intersectDist
	intersectDist = dist

def getIntersectDist():
	global intersectDist
	return intersectDist
	
def getObjectPosition():
	global objectPos
	return objectPos
	
def getObjectOrientation():
	global objectOrient
	return objectOrient
	
def setWandID(val):
	global wandID
	wandID = val
	
def getWandID():
	global wandID
	return wandID
	
def getCounter():
	global counter
	return counter

def setCounter(c):
	global counter
	counter = c
	
def handleEvent():
	global e, sourceId, wandPos, wandRay, intersectObj, intersectDist, wandID
	global objectPos, objectOrient
	
	e = getEvent()
	sourceId = e.getSourceId()
	#setWandID(sourceId)
	'''
	if e.isButtonDown(EventFlags.Button5):
		print "moving tile YES"
		#drawMidWindowOutline()
		wandPos = caveutil.getWandWorldPosition(getCam(), getWandID())
		wandRay = caveutil.getWandRay(getCam(), getWandID())
		intersectObj, intersectDist = caveutil.getNearestIntersectingObject(wandPos, wandRay)
		if (intersectObj != None):
			print intersectObj.getTag()
			if intersectObj.getTag().find("box") != -1:
				setIntersectObj(allSystems.getChildByName(intersectObj.getTag()))
				setIntersectDist(intersectDist)
				objectPos = getIntersectObj().getPosition()
				objectOrient = getIntersectObj().getOrientation()
				setIsMovingTile(True)
		
	if e.isButtonUp(EventFlags.Button5):
		#removeMidWindowOutline()
		print "stopped moving tile NO"
		wandPos = caveutil.getWandWorldPosition(getCam(), getWandID())
		wandRay = caveutil.getWandRay(getCam(), getWandID())
		setIsMovingTile(False)
		if getIntersectObj() != None:
			setWallTilePosAfterMove(wandRay, wandPos, getObjectPosition(), getObjectOrientation(), getIntersectObj()) 
			setIntersectObj(None)
	'''
	
	r = getRayFromEvent(e)
	for system, model in hitWallDict.iteritems():
		node = hitWallDict[system]
		hitData = hitNode(node, r[1], r[2])
		if hitData[0]:
			print system
			hitWallDict[system].setEffect('colored -e #CCCCCCEE')
			setIntersectObj(system)
			if e.isButtonDown(EventFlags.Button5):
				#setCounter(datetime.now().time())
				setCounter(False)
				setIsMovingTile(True)
				if e.isButtonDown(EventFlags.Button3):
					print "removing"
					getUserList().remove(getIntersectObj())
					#userList = displaySystemList
					updateList(5)
					setUserDefinedList(True)
					setAllSystemsList(False)
					setNearesrList(False)
					setEarthLikeList(False)
					setHabitableList(False)
					setSunLikeList(False)
					setCounter(True)
					
			if e.isButtonUp(EventFlags.Button5):
				if getCounter() == False:
					visitSystem(getIntersectObj())
		else:
			if getIntersectObj() != None:
				hitWallDict[getIntersectObj()].setEffect('colored -e #111122EE')
				setIntersectObj(None)
setEventFunction(handleEvent)
