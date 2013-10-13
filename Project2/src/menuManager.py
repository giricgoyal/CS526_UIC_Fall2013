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

# -----------------------------------------------------------------
# variables
visitSystemButtonList = dict()
orbitScaleSlider = None
orbitScaleSlider = None
planetScaleSliderText = None
planetScaleSliderText = None

#------------------------------------------------------------------
# method definitions
def visitSystem():
	##global currentSystem
	for system, button in visitSystemButtonList.iteritems():
		if button.getText() == currentSystem:
			button.setChecked(False)
	for system, button in visitSystemButtonList.iteritems():
		if button.isChecked():
			if button.getText() != currentSystem:
				#currentSystem = button.getText()
				pos = starLocations[system].pos
				#print button.getText()
				setCamPosition(pos)

def setOrbitSlider():
	orbitScaleSliderText.setText("Orbit Scale: " + str(orbitScaleSlider.getValue()))
	updateOrbitScale(orbitScaleSlider.getValue())
	

def setPlanetSlider():
	planetScaleSliderText.setText("Planet Scale: " + str(planetScaleSlider.getValue()))
	#updatePlanetScale(planetScaleSlider.getValue())
	
# -----------------------------------------------------------------
# main

print "Initializing Main Menu"
# create, initialize and get main menu
mm = MenuManager.createAndInitialize()
mainMenu = mm.getMainMenu()

# Level 1
scaleMenu = mainMenu.addSubMenu("Scale Options")
visitSystemMenu = mainMenu.addSubMenu("Visit System")


# level 2
scaleContainer = scaleMenu.addContainer().getContainer()
scaleContainer.setLayout(ContainerLayout.LayoutVertical)

visitSystemContainer = visitSystemMenu.addContainer().getContainer()
visitSystemContainer.setLayout(ContainerLayout.LayoutVertical)



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
		
	# orbit scale slider
	global orbitScaleSlider, orbitScaleSliderText
	orbitScaleSliderText = Label.create(scaleContainer)
	orbitScaleSlider = Slider.create(scaleContainer)
	orbitScaleSlider.setTicks(9)
	orbitScaleSlider.setValue(4)
	orbitScaleSlider.setUIEventCommand('setOrbitSlider()')
	orbitScaleSliderText.setText("Orbit Scale: " + str(orbitScaleSlider.getValue()))
	
	# orbit scale slider
	global planetScaleSlider, planetScaleSliderText
	planetScaleSliderText = Label.create(scaleContainer)
	planetScaleSlider = Slider.create(scaleContainer)
	planetScaleSlider.setTicks(9)
	planetScaleSlider.setValue(4)
	planetScaleSlider.setUIEventCommand('setPlanetSlider()')
	planetScaleSliderText.setText("Planet Scale: " + str(planetScaleSlider.getValue()))
	





