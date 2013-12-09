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
from src import caveutil
import util

# ------------------------------------------------------
# variables
cam3D = getDefaultCamera()
posx = 7768.82
posy = 2281.18
posz = 5034.08
pos = Vector3(posx, posy, posz)
orient3D = cam3D.getOrientation()
pos3D = cam3D.getPosition()
orient2D = cam3D.getOrientation()
pos2D = cam3D.getPosition()
# ------------------------------------------------------
# methods
obj = caveutil.InterpolActor(cam3D)
obj.setDuration(3)
obj.setOperation(caveutil.InterpolActor.POSITION | caveutil.InterpolActor.ORIENT | caveutil.InterpolActor.SCALE)

def init():
	cam3D.setPosition(util.city1.getBoundCenter() + pos)
	cam3D.getController().setSpeed(1000)
	cam3D.setPitchYawRoll(Vector3(radians(45), 0, 0))
	
def set3DCamera(pos = Vector3(posx, posy, posz)):
	obj.setTargetPosition(Vector3(cam3D.getPosition().x,cam3D.getPosition().y,pos3D.z))
	obj.setTargetOrientation(orient3D)
	obj.setOperation(caveutil.InterpolActor.POSITION | caveutil.InterpolActor.ORIENT | caveutil.InterpolActor.SCALE)
	obj.startInterpolation()
	'''
	cam3D.setPosition(util.city1.getBoundCenter() + pos)
	cam3D.getController().setSpeed(1000)
	cam3D.setPitchYawRoll(Vector3(radians(70), 0, 0))
	'''
	
	
def set2DCamera(pos = Vector3(posx, posy, posz)):
	print pos
	global orient2D
	obj.setTargetPosition( Vector3(cam3D.getPosition().x,cam3D.getPosition().y,15000))
	if orient2D != None:
		obj.setTargetOrientation(orient2D)
	obj.setOperation(caveutil.InterpolActor.ORIENT | caveutil.InterpolActor.POSITION | caveutil.InterpolActor.SCALE)
	obj.startInterpolation()
	orient2D = cam3D.getOrientation()
	'''
	cam3D.setPosition(util.city1.getBoundCenter() + pos + Vector3(0,0,15000))
	cam3D.getController().setSpeed(1000)
	cam3D.setPitchYawRoll(Vector3(radians(0), 0, 0))
	'''
	

def jumpToComm(pos = Vector3(posx, posy, posz)):
	print pos
	global orient2D
	obj.setTargetPosition(pos)
	if orient2D != None:
		obj.setTargetOrientation(orient2D)
	obj.setOperation(caveutil.InterpolActor.POSITION | caveutil.InterpolActor.ORIENT | caveutil.InterpolActor.SCALE)
	obj.startInterpolation()
	#cam3D.setPosition(pos + Vector3(0,0,8000))
	#cam3D.getController().setSpeed(1000)
	#cam3D.setPitchYawRoll(Vector3(radians(0), 0, 0))
	
	
def onUpdate(frame, time, dt):
	if util.is3DEnabled == True:
		global orient3D
		global pos3D
		orient3D = cam3D.getOrientation()
		pos3D = cam3D.getPosition()
	else:
		global orient2D
		global pos2D
		orient2D = cam3D.getOrientation()
		pos2D = cam3D.getPosition()
	
		
setUpdateFunction(onUpdate)