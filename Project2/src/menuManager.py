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

#------------------------------------------------------------------
# method definitions
def visitSystem():
	for system, button in visitSystemButtonList.iteritems():
		if button.isChecked():
			pos = starLocations[system].pos * orbitScaleFactor * userScaleFactor
			setCamPosition(pos)
			setActiveSystem(button.getText())
			visualizeButton.setChecked(False)
			#print activeSystem

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
	
# -----------------------------------------------------------------
# main

print "Initializing Main Menu"
# create, initialize and get main menu
mm = MenuManager.createAndInitialize()
mainMenu = mm.getMainMenu()

# Level 1
scaleMenu = mainMenu.addSubMenu("Scale Options")
visitSystemMenu = mainMenu.addSubMenu("Visit System")
optionsMenu = mainMenu.addSubMenu("Options")

# level 2
scaleContainer = scaleMenu.addContainer().getContainer()
scaleContainer.setLayout(ContainerLayout.LayoutVertical)
#scaleContainer.setHorizontalAlign(HAlign.AlignLeft)

visitSystemContainer = visitSystemMenu.addContainer().getContainer()
visitSystemContainer.setLayout(ContainerLayout.LayoutVertical)
#visitSystemContainer.setHorizontalAlign(HAlign.AlignLeft)

optionsMenuContainer = optionsMenu.addContainer().getContainer()
optionsMenuContainer.setLayout(ContainerLayout.LayoutVertical)

# buttons
def initButtons():
	
	# visit system buttons
	for system in systemList:
		button = Button.create(visitSystemContainer)
		button.setText(system)
		button.setCheckable(True)
		button.setRadio(True)
		visitSystemButtonList[system] = button
		button.setUIEventCommand('visitSystem()')
		
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
	
	# reset button
	global resetButton
	resetButton = Button.create(optionsMenuContainer)
	resetButton.setText("Reset System")
	resetButton.setUIEventCommand('resetSystem()')
	
	# See Visualization
	global visualizeButton
	visualizeButton = Button.create(optionsMenuContainer)
	visualizeButton.setText("Show Relative Position")
	visualizeButton.setCheckable(True)
	visualizeButton.setUIEventCommand('visitVisualization()')


