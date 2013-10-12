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
planetScaleSlider = None

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

def setPlanetSlider():
	print planetScaleSlider.getValue()
	updateOrbitScale(planetScaleSlider.getValue())
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
		
	# planet scale slider
	global planetScaleSlider
	planetScaleSlider = Slider.create(scaleContainer)
	planetScaleSlider.setTicks(9)
	planetScaleSlider.setValue(4)
	planetScaleSlider.setUIEventCommand('setPlanetSlider()')
	






