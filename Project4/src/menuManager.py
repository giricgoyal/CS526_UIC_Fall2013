#------------------------------------------------------------------
#	menuManager.py for handling Menu
#	author : Giric Goyal
#------------------------------------------------------------------

#------------------------------------------------------------------
# imports
from omegaViewer import *
from omegaToolkit import *
from euclid import *
from util import *
from cameraManager import *
from visualize import *
from system import *

# -----------------------------------------------------------------
# variables
visitSystemButtonList = dict()
orbitScaleSlider = None
orbitScaleSliderText = None
planetScaleSlider = None
planetScaleSliderText = None
sunScaleSlider = None
sunScaleSliderText = None
timeFactorSlider = None
timeFactorSliderText = None
resetButton = None
visualizeButton = None
allSystemsListButton = None
nearestListButton = None
earthLikeListButton = None
habitableListButton = None
sunLikeListButton = None
userDefinedList = None



#------------------------------------------------------------------
# method definitions
def visitSystem(tempSys = "-"):
	if tempSys == "-":
		for system, button in visitSystemButtonList.iteritems():
			lightsDict[system].setEnabled(False)
			if button.isChecked():
				pos = starLocations[system].pos * orbitScaleFactor * userScaleFactor
				setCamPosition(pos)
				lightsDict[system].setEnabled(True)
				setActiveSystem(button.getText())
				visualizeButton.setChecked(False)
				#print activeSystem
	else:
		for system, button in visitSystemButtonList.iteritems():
			if button.getText() == tempSys:
				pos = starLocations[tempSys].pos * orbitScaleFactor * userScaleFactor
				setCamPosition(pos)
				setActiveSystem(button.getText())
				button.setChecked(True)
				visualizeButton.setChecked(False)
			else:
				button.setChecked(False)

def setOrbitSlider():
	orbitScaleSliderText.setText("Orbit Scale: " + str(orbitScaleSlider.getValue() + 1))
	if orbitScaleSlider.getValue() == 5:
		orbitScaleSliderText.setText("Orbit Scale: " + str(orbitScaleSlider.getValue() + 1) + " (default)")
	updateOrbitScale(orbitScaleSlider.getValue())
	

def setPlanetSlider():
	planetScaleSliderText.setText("Planet Scale: " + str(planetScaleSlider.getValue() + 1))
	if planetScaleSlider.getValue() == 2:
		planetScaleSliderText.setText("Planet Scale: " + str(planetScaleSlider.getValue() + 1) + " (default)")
	updatePlanetScale(planetScaleSlider.getValue())
	
def setSunSlider():
	sunScaleSliderText.setText("Sun Scale: " + str(sunScaleSlider.getValue() + 1))
	if sunScaleSlider.getValue() == 3:
		sunScaleSliderText.setText("Sun Scale: " + str(sunScaleSlider.getValue() + 1) + "(default)")
	updateSunScale(sunScaleSlider.getValue())
	
def setTimeFactor():
	timeFactorSliderText.setText("Time: " + str(timeFactorSlider.getValue() + 1))
	if timeFactorSlider.getValue() == 0:
		timeFactorSliderText.setText("Time: " + str(timeFactorSlider.getValue() + 1) + "(default)")
	updateTimeFactor(timeFactorSlider.getValue())
	
def resetSystem():
	print "Reseting the Universe"
	orbitScaleSlider.setValue(5)
	setOrbitSlider()
	planetScaleSlider.setValue(2)
	setPlanetSlider()
	sunScaleSlider.setValue(3)
	setSunSlider()
	timeFactorSlider.setValue(0)
	setTimeFactor()
	
def visitVisualization():
	print "Showing Visualization"
	changeColor()
	if visualizeButton.isChecked():
		setCamPos()
		setCamPosition(vizPos)
	else:
		setCamPosition2(getCamPosition())
	
	
def updateList(number):
	print "Setting systems from new list"
	setDisplayList(number)
	reorderAuto2D()
	changeColor()
	
def setUserDefinedList(val):
	global userDefinedList
	userDefinedList.setChecked(val)
	
def setAllSystemsList(val):
	global allSystemsListButton
	allSystemsListButton.setChecked(val)

def setNearesrList(val):
	global nearestListButton
	nearestListButton.setChecked(val)
	
def setEarthLikeList(val):
	global earthLikeListButton
	earthLikeListButton.setChecked(val)

def setHabitableList(val):
	global habitableListButton
	habitableListButton.setChecked(val)

def setSunLikeList(val):
	global sunLikeListButton
	sunLikeListButton.setChecked(val)
	
# -----------------------------------------------------------------
# main

print "Initializing Main Menu"
# create, initialize and get main menu
mm = MenuManager.createAndInitialize()
mainMenu = mm.getMainMenu()

# Level 1
scaleMenu = mainMenu.addSubMenu("Scale")
visitSystemMenu = mainMenu.addSubMenu("Visit")
listsMenu = mainMenu.addSubMenu("Lists")
optionsMenu = mainMenu.addSubMenu("Options")


# level 2
scaleContainer = scaleMenu.addContainer().getContainer()
scaleContainer.setLayout(ContainerLayout.LayoutVertical)
#scaleContainer.setHorizontalAlign(HAlign.AlignLeft)

visitSystemContainer = visitSystemMenu.addContainer().getContainer()
visitSystemContainer.setLayout(ContainerLayout.LayoutVertical)
#visitSystemContainer.setHorizontalAlign(HAlign.AlignLeft)

listsContainer1 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer2 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer3 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer4 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer5 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer6 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer7 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)
listsContainer8 = Container.create(ContainerLayout.LayoutHorizontal, visitSystemContainer)


optionsMenuContainer = optionsMenu.addContainer().getContainer()
optionsMenuContainer.setLayout(ContainerLayout.LayoutVertical)

listsContainer = listsMenu.addContainer().getContainer()
listsContainer.setLayout(ContainerLayout.LayoutVertical)


# buttons
def initButtons():

	# scale slider
	scaleText = Label.create(scaleContainer)
	scaleText.setText("Scaling Factor (n): 1/10^n")
	
	# orbit
	global orbitScaleSlider, orbitScaleSliderText
	orbitScaleSliderText = Label.create(scaleContainer)
	orbitScaleSlider = Slider.create(scaleContainer)
	orbitScaleSlider.setTicks(9)
	orbitScaleSlider.setValue(5)
	orbitScaleSlider.setUIEventCommand('setOrbitSlider()')
	orbitScaleSliderText.setText("Orbit Scale: " + str(orbitScaleSlider.getValue() + 1) + " (default)" )
	
	# planet
	global planetScaleSlider, planetScaleSliderText
	planetScaleSliderText = Label.create(scaleContainer)
	planetScaleSlider = Slider.create(scaleContainer)
	planetScaleSlider.setTicks(5)
	planetScaleSlider.setValue(2)
	planetScaleSlider.setUIEventCommand('setPlanetSlider()')
	planetScaleSliderText.setText("Planet Scale: " + str(planetScaleSlider.getValue() + 1) + " (default)" )
	
	# sun
	global sunScaleSlider, sunScaleSliderText
	sunScaleSliderText = Label.create(scaleContainer)
	sunScaleSlider = Slider.create(scaleContainer)
	sunScaleSlider.setTicks(5)
	sunScaleSlider.setValue(3)
	sunScaleSlider.setUIEventCommand('setSunSlider()')
	sunScaleSliderText.setText("Sun Scale: " + str(sunScaleSlider.getValue() + 1) + " (default)" )
	
	# time slider
	timeText = Label.create(scaleContainer)
	timeText.setText("Timing Factor (n): nx")
	
	global timeFactorSlider, timeFactorSliderText
	timeFactorSliderText = Label.create(scaleContainer)
	timeFactorSlider = Slider.create(scaleContainer)
	timeFactorSlider.setTicks(10)
	timeFactorSlider.setValue(0)
	timeFactorSlider.setUIEventCommand('setTimeFactor()')
	timeFactorSliderText.setText("Time: " + str(timeFactorSlider.getValue() + 1) + " (default)" )
	
	
	# visit system buttons
	counter = 0
	for i in range(0,6):
		button = Button.create(listsContainer1)
		button.setText(systemList[i])
		button.setCheckable(True)
		button.setRadio(True)
		visitSystemButtonList[systemList[i]] = button
		button.setUIEventCommand('visitSystem()')
		
	for i in range(6,11):
		system = systemList[i]
		button = Button.create(listsContainer2)
		button.setText(system)
		button.setCheckable(True)
		button.setRadio(True)
		visitSystemButtonList[system] = button
		button.setUIEventCommand('visitSystem()')

	for system in systemList:
		'''
		if (counter >= 0) and (counter <= 5):
			button = Button.create(listsContainer1)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
			
		if (counter >= 6) and (counter <= 11):
			button = Button.create(listsContainer2)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
			'''
		if (counter >= 12) and (counter <= 17):
			button = Button.create(listsContainer3)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		if (counter >= 18) and (counter <= 23):
			button = Button.create(listsContainer4)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		if (counter >= 24) and (counter <= 29):
			button = Button.create(listsContainer5)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		if (counter >= 30) and (counter <= 35):
			button = Button.create(listsContainer6)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		if (counter >= 36) and (counter <= 41):
			button = Button.create(listsContainer7)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		if (counter >= 42) and (counter <= 47):
			button = Button.create(listsContainer8)
			button.setText(system)
			button.setCheckable(True)
			button.setRadio(True)
			visitSystemButtonList[system] = button
			button.setUIEventCommand('visitSystem()')
		counter += 1
	
	# Lists Buttons
	# four Lists
	
	# all systems
	global allSystemsListButton
	allSystemsListButton = Button.create(listsContainer)
	allSystemsListButton.setText("All Systems")
	allSystemsListButton.setCheckable(True)
	allSystemsListButton.setRadio(True)
	allSystemsListButton.setChecked(True)
	allSystemsListButton.setUIEventCommand('updateList(0)')
	
	# nearest to the earth 
	global nearestListButton
	nearestListButton = Button.create(listsContainer)
	nearestListButton.setText("Nearest to the Earth")
	nearestListButton.setCheckable(True)
	nearestListButton.setRadio(True)
	nearestListButton.setUIEventCommand('updateList(1)')
	
	# Earth like
	global earthLikeListButton
	earthLikeListButton = Button.create(listsContainer)
	earthLikeListButton.setText("Earth Like")
	earthLikeListButton.setCheckable(True)
	earthLikeListButton.setRadio(True)
	earthLikeListButton.setUIEventCommand('updateList(2)')
	
	# Habitable 
	global habitableListButton
	habitableListButton = Button.create(listsContainer)
	habitableListButton.setText("Likely to be Habitable")
	habitableListButton.setCheckable(True)
	habitableListButton.setRadio(True)
	habitableListButton.setUIEventCommand('updateList(3)')
	
	# Sun like stars
	global sunLikeListButton
	sunLikeListButton = Button.create(listsContainer)
	sunLikeListButton.setText("Sun Like")
	sunLikeListButton.setCheckable(True)
	sunLikeListButton.setRadio(True)
	sunLikeListButton.setUIEventCommand('updateList(4)')
	
	# user list
	global userDefinedList
	userDefinedList = Button.create(listsContainer)
	userDefinedList.setText("User Defined")
	userDefinedList.setCheckable(True)
	userDefinedList.setRadio(True)
	userDefinedList.setUIEventCommand('updateList(5)')
	
	# reset button
	global resetButton
	resetButton = Button.create(optionsMenuContainer)
	resetButton.setText("Reset System")
	resetButton.setUIEventCommand('resetSystem()')
	
	# See Visualization
	global visualizeButton
	visualizeButton = Button.create(optionsMenuContainer)
	visualizeButton.setText("Stellar View")
	visualizeButton.setCheckable(True)
	visualizeButton.setUIEventCommand('visitVisualization()')


