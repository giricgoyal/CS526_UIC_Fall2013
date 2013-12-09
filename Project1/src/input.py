from omega import *
import util


#handle events from the wand

def handleEvent():
	global userScaleFactor
	e = getEvent()
	if (e.isButtonDown(EventFlags.ButtonRight)):
		print "\nLeft Button Pressed"
		counter = 0
		for val in util.cityMapList:
			if val == True:
				util.cityMapList[counter] = False
				if counter == 2:
					counter = 0
				else:
					counter += 1
				util.cityMapList[counter] = True
				break
			else:
				counter += 1
		handleCityMaps()
		
	if (e.isButtonDown(EventFlags.ButtonLeft)):
		print "\nRight Button Pressed"
		counter = 0
		for val in util.cityMapList:
			if val == True:
				util.cityMapList[counter] = False
				if counter == 0:
					counter = 2
				else:
					counter -= 1
				util.cityMapList[counter] = True
				break
			else:
				counter += 1
		handleCityMaps()

# method to change maps
def handleCityMaps():
	if util.cityMapList[0] == True:
		print "\ncity1"
		util.city1.setVisible(True)
		util.city2.setVisible(False)
		util.city3.setVisible(False)
	elif util.cityMapList[1] == True:
		print "\ncity2"
		util.city1.setVisible(False)
		util.city2.setVisible(True)
		util.city3.setVisible(False)
	elif util.cityMapList[2] == True:
		print "\ncity3"
		util.city1.setVisible(False)
		util.city2.setVisible(False)
		util.city3.setVisible(True)
		