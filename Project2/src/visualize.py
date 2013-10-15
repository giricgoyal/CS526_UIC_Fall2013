# #######################################################
# create the systems in 3D,
# create the wall systems
#
# author: giric goyal
# #######################################################

# -------------------------------------------------------
# imports 
from util import *
from math import *
from euclid import *
from omega import *
from cyclops import *


# -------------------------------------------------------
# variables


# -------------------------------------------------------
# method definitions
def createVisualization():
	theSystem = dict()
	
	for system in systemList:
		# set the system name
		# create the objects
		theSystem = allSystemsOrbital[system]
		pos = starLocations[system].pos * orbitScaleFactor * userScaleFactor * 0.0000000001
		for name, model in theSystem.iteritems():
			if theSystem[name].isStar == 1:
				dot = StaticObject.create("defaultSphere")
				dot.setPosition(pos)
				dot.setScale(Vector3(10.0/70, 10.0/70, 10.0/70))
				if name == "The Sun":
					dot.setEffect("colored -e red")
				else:
					if findInList(system, displaySystemList) == True:
						dot.setEffect("colored -e #0000CCCC")
					else:
						dot.setEffect("colored -e white")
				vizContainer.addChild(dot)
				visualizeDict[system] = dot
				
				t1 = Text3D.create('fonts/verdana.ttf', 1, str(name))
				t1.setPosition(Vector3(pos.x, pos.y, pos.z))
				t1.yaw(pi)
				t1.setFontResolution(256)
				t1.setFontSize(fontSize)
				t1.getMaterial().setTransparent(False)
				t1.getMaterial().setDepthTestEnabled(False)
				t1.setColor(colorWhite)
				vizContainer.addChild(t1)
				
	
	vizContainer.setPosition(vizPos * overallScaleFactor)
	
	
	
def changeColor():
	activeSystem = getActiveSystem()
	for system, model in visualizeDict.iteritems():
		visualizeDict[system].setEffect("colored -e white")
		if system == activeSystem:
			visualizeDict[system].setEffect("colored -e red")
		else:
			if findInList(system, displaySystemList) == True:
				visualizeDict[system].setEffect("colored -e #0000CCCC")
			else:
				visualizeDict[system].setEffect("colored -e white")
		