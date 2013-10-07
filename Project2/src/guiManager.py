#------------------------------------------------------------------
#	guiManager.py for Managing GUI
#	author : Giric Goyal
#------------------------------------------------------------------

#------------------------------------------------------------------
# imports
from omegaViewer import *
from omegaToolkit import *
from euclid import *
from math import *
from euclid import *
from omega import *
from cyclops import *
from datetime import datetime
import util
import cameraManager

#------------------------------------------------------------------
# variables
global ui
global wf
global uiRoot
global windowMain
global uiOptionsButton
global ui3DButton

uiSizeMinX = 150*util.cave
uiSizeMinY = 270*util.cave
uiSizeMaxX = 750*util.cave
uiSizeMaxY = 270*util.cave


#------------------------------------------------------------------
# method definitions

# method to initialize main menu
def toggleOptionsMenu():
	print "Options Menu On"
	uiRoot.removeChild(uiOptionsButton)
	uiRoot.addChild(windowMain)
	
def closeOptionsMenu():
	print "Options Menu Off"
	#uiRoot.addChild(uiOptionsButton)
	#uiRoot.removeChild(windowMain)
	#uiRoot.removeChild(windowYear)
	#uiRoot.removeChild(windowType)
	windowMain.removeChild(windowMain)
	

def view(button):
	print "3D view : " + str(button.isChecked())
	util.is3DEnabled = not(util.is3DEnabled)
	button.setText(('Disable' if util.is3DEnabled else 'Enable') + ' 3D')
	if util.is3DEnabled == True:
		print "Enabled"
		cameraManager.set3DCamera()
		hide()
		#cameraManager.jumpToComm()
		
	else:
		print "Disabled"
		cameraManager.set2DCamera()
		hide()
		#cameraManager.jumpToComm(util.city1.getBoundCenter() + cameraManager.pos + Vector3(0,0,15000))
	#uiRoot.removeChild(windowMain)
	#uiRoot.addChild(uiOptionsButton)
	
def manageYear(button):
	print "Managing year : " + button.getText() + " : " + util.selectedYear

def updateYear():
	print "updating"
	print len(yearButtonList)
	for button in yearButtonList:
		if button.isChecked():
			if button.getText() != util.selectedYear:
				print button.getText()
				util.selectedYear = button.getText()
				#windowMain.removeChild(windowComm)
				break
	print "New selected Year : " + util.selectedYear + ", Updating"
	
def updateType():
	for button in crimeTypeButtonList:
		if button.isChecked():
			if button.getText() != util.selectedCrime:
				util.selectedCrime = button.getText()
				#windowMain.removeChild(windowComm)
				break
				
def updateComm():
	for button in commButtonList:
			if button.isChecked():
				if button.getText() != util.selectedComm:
					util.selectedComm = button.getText()
					#windowMain.removeChild(windowComm)
					break
					
def updateTime():
	for button in precisionList:
		if button.isChecked():
			if button.getText() != util.precisionLevel:
				util.precisionLevel = button.getText()
				break
				
	util.isTypeMenuOn = False
	util.isYearMenuOn = False
	util.isCommunityMenuOn = False
	util.isTimeMenuOn = False

def manageType():
	print "managing Type : " + util.selectedCrime
	for button in crimeTypeButtonList:
		if button.getText() == util.selectedCrime:
			button.setChecked(False)
		
def satellite(button):
	print "Satellite Mode : " + str(button.isChecked())
	if button.isChecked() == True:
		util.city1.setVisible(True)
		util.city3.setVisible(False)
	else:
		util.city1.setVisible(False)
		util.city3.setVisible(True)
	#uiRoot.removeChild(windowMain)
	#uiRoot.addChild(uiOptionsButton)
	

def crime(button):
	print "Crime : " + str(button.isChecked())
	util.isCrimeEnabled = button.isChecked()

def cta(button):
	print "cta : " + str(button.isChecked())
	util.isCTAEnabled = button.isChecked()
		
		
def boundary(button):
	print "boundary " + str(button.isChecked())
	util.isBoundaryOn = button.isChecked()

def crimeCount(button):
	print "crime COunt" + str(button.isChecked())
	util.isCrimeCountOn = button.isChecked()
	
def realTime(button):
	print "real time" + str(button.isChecked())
	util.isRealTimeEnabled = button.isChecked()

def manageCommunity():
	print "managing Community : " + util.selectedComm
	for button in commButtonList:
		if button.getText() == util.selectedComm:
			button.setChecked(False)
			
	
					
def addList():
	#overViewButton.setChecked(False)
	windowComm.removeChild(listComm1)
	windowComm.removeChild(listComm2)
	windowComm.removeChild(listComm3)
	windowComm.removeChild(listComm4)
	windowComm.removeChild(listComm5)
	windowComm.removeChild(listComm6)
	windowComm.removeChild(listComm7)
	for comm in commButtonList:
		comm.setChecked(False)
	if displayListNo == 1:
		windowComm.addChild(listComm1)
	elif displayListNo == 2:
		windowComm.addChild(listComm2)	
	elif displayListNo == 3:
		windowComm.addChild(listComm3)
	elif displayListNo == 4:
		windowComm.addChild(listComm4)
	elif displayListNo == 5:
		windowComm.addChild(listComm5)
	elif displayListNo == 6:
		windowComm.addChild(listComm6)
	elif displayListNo == 7:
		windowComm.addChild(listComm7)

def overView():
	util.selectedComm = ""
	util.isCommunityMenuOn = False
	util.isYearMenuOn = False
	util.isTypeMenuOn = False
	util.isTimeMenuOn = False
	for button in commButtonList:
		button.setChecked(False)
		
			
def manageTime(button):
	print "Managing time : " + button.getText() + " : " + util.selectedTime
	
		

def inc(string):
	if string == "mm":
		util.selectedMonth += 1
		if util.selectedMonth > 12:
			util.selectedMonth = 1
		mmButton.setText(str(util.selectedMonth))
	if string == "dd":
		util.selectedDate += 1
		if util.selectedDate > 31:
			util.selectedDate = 1
		ddButton.setText(str(util.selectedDate))
	if string == "yyyy":
		util.selectedYear = str(int(util.selectedYear) + 1)
		if int(util.selectedYear) > 2013:
			util.selectedYear = "2001"
		yyyyButton.setText(str(util.selectedYear))
	if string == "hr":
		util.selectedHour += 1
		if util.selectedHour > 12:
			util.selectedHour = 1
		hrButton.setText(str(util.selectedHour))
	if string == "min":
		util.selectedMin += 1
		if util.selectedMin  > 59:
			util.selectedMin = 0
		minButton.setText(str(util.selectedMin))
	if string == "p":
		if util.selectedP == "PM":
			util.selectedP = "AM" 
		else:
			util.selectedP = "PM"
		pButton.setText(str(util.selectedP))
			
# ------------------------------------------------------------------
# MAIN


mm = MenuManager.createAndInitialize()
sysMenu = mm.getMainMenu().addSubMenu("Options")


ui = UiModule.createAndInitialize()
wf = ui.getWidgetFactory()
uiRoot = ui.getUi()


uiOptionsLabel = sysMenu.addLabel("Options Menu")
#uiOptionsLabel.setColor(Color('Yellow'))
#uiOptionsLabel.setFont('fonts/arial.ttf 14')


ui3DButton = sysMenu.addButton(('Disable' if util.is3DEnabled else 'Enable') + ' 3D', 'guiManager.view(guiManager.ui3DButton)')


# Year Selection-----------------------------------------------------------------------------
# create select year option menu
yearMenu = sysMenu.addSubMenu("Select Year")
windowYear = yearMenu.addContainer().getContainer()
windowYear.setLayout(ContainerLayout.LayoutVertical)
windowYear.setMargin(1*util.cave)
windowYear.setPadding(1*util.cave)


yearButtonList = []
# create year radio button
ui2013Button = Button.create(windowYear)
ui2013Button.setText('2013')
ui2013Button.setPosition(Vector2(0*util.cave,0*util.cave))
ui2013Button.setCheckable(True)
ui2013Button.setRadio(True)
ui2013Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2013Button)')
yearButtonList.append(ui2013Button)

ui2012Button = Button.create(windowYear)
ui2012Button.setText('2012')
ui2012Button.setPosition(Vector2(80*util.cave,0*util.cave))
ui2012Button.setCheckable(True)
ui2012Button.setRadio(True)
ui2012Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2012Button)')
yearButtonList.append(ui2012Button)

ui2011Button = Button.create(windowYear)
ui2011Button.setText('2011')
ui2011Button.setPosition(Vector2(160*util.cave,0*util.cave))
ui2011Button.setCheckable(True)
ui2011Button.setRadio(True)
ui2011Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2011Button)')
yearButtonList.append(ui2011Button)

ui2010Button = Button.create(windowYear)
ui2010Button.setText('2010')
ui2010Button.setPosition(Vector2(240*util.cave,0*util.cave))
ui2010Button.setCheckable(True)
ui2010Button.setRadio(True)
ui2010Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2010Button)')
yearButtonList.append(ui2010Button)

ui2009Button = Button.create(windowYear)
ui2009Button.setText('2009')
ui2009Button.setPosition(Vector2(320*util.cave,0*util.cave))
ui2009Button.setCheckable(True)
ui2009Button.setRadio(True)
ui2009Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2009Button)')
yearButtonList.append(ui2009Button)


ui2008Button = Button.create(windowYear)
ui2008Button.setText('2008')
ui2008Button.setPosition(Vector2(0*util.cave,25*util.cave))
ui2008Button.setCheckable(True)
ui2008Button.setRadio(True)
ui2008Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2008Button)')
yearButtonList.append(ui2008Button)

ui2007Button = Button.create(windowYear)
ui2007Button.setText('2007')
ui2007Button.setPosition(Vector2(80*util.cave,25*util.cave))
ui2007Button.setCheckable(True)
ui2007Button.setRadio(True)
ui2007Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2007Button)')
yearButtonList.append(ui2007Button)

ui2006Button = Button.create(windowYear)
ui2006Button.setText('2006')
ui2006Button.setPosition(Vector2(160*util.cave,25*util.cave))
ui2006Button.setCheckable(True)
ui2006Button.setRadio(True)
ui2006Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2006Button)')
yearButtonList.append(ui2006Button)

ui2005Button = Button.create(windowYear)
ui2005Button.setText('2005')
ui2005Button.setPosition(Vector2(240*util.cave,25*util.cave))
ui2005Button.setCheckable(True)
ui2005Button.setRadio(True)
ui2005Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2005Button)')
yearButtonList.append(ui2005Button)

ui2004Button = Button.create(windowYear)
ui2004Button.setText('2004')
ui2004Button.setPosition(Vector2(320*util.cave,25*util.cave))
ui2004Button.setCheckable(True)
ui2004Button.setRadio(True)
ui2004Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2004Button)')
yearButtonList.append(ui2004Button)


ui2003Button = Button.create(windowYear)
ui2003Button.setText('2003')
ui2003Button.setPosition(Vector2(0*util.cave,50*util.cave))
ui2003Button.setCheckable(True)
ui2003Button.setRadio(True)
ui2003Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2003Button)')
yearButtonList.append(ui2003Button)

ui2002Button = Button.create(windowYear)
ui2002Button.setText('2002')
ui2002Button.setPosition(Vector2(80*util.cave,50*util.cave))
ui2002Button.setCheckable(True)
ui2002Button.setRadio(True)
ui2002Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2002Button)')
yearButtonList.append(ui2002Button)

ui2001Button = Button.create(windowYear)
ui2001Button.setText('2001')
ui2001Button.setPosition(Vector2(160*util.cave,50*util.cave))
ui2001Button.setCheckable(True)
ui2001Button.setRadio(True)
ui2001Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2001Button)')
yearButtonList.append(ui2001Button)

uiAllYearsButton = Button.create(windowYear)
uiAllYearsButton.setText('2001-2013')
uiAllYearsButton.setPosition(Vector2(240*util.cave,50*util.cave))
uiAllYearsButton.setCheckable(True)
uiAllYearsButton.setRadio(True)
uiAllYearsButton.setUIEventCommand('guiManager.manageYear(guiManager.uiAllYearsButton)')
yearButtonList.append(uiAllYearsButton)

# update button
uiUpdateButton1 = Button.create(windowYear)
uiUpdateButton1.setText('Update')
uiUpdateButton1.setUIEventCommand('guiManager.updateYear()\naddAndRemoveData()')
uiUpdateButton1.setPosition(Vector2(0*util.cave, 80*util.cave))



# type of crime------------------------------------------------------------------------------
# select type option menu

typeMenu = sysMenu.addSubMenu("Select Type")
windowType = typeMenu.addContainer().getContainer()
windowType.setLayout(ContainerLayout.LayoutVertical)
windowType.setMargin(1*util.cave)
windowType.setPadding(1*util.cave)

# View Menu ------------------------------------------------------------------	
# Create button for view Menu

counter = 0
crimeTypeButtonList = []
x = 0
y = 0
for type in util.crimeList:
	counter += 1
	crimeOption = Button.create(windowType)
	crimeOption.setText(type)
	crimeOption.setCheckable(True)
	crimeOption.setRadio(True)
	crimeTypeButtonList.append(crimeOption)
	crimeOption.setUIEventCommand('guiManager.manageType()')
	crimeOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 120
	if counter % 4 == 0:
		x = 0*util.cave
		y += 25

# update button

uiUpdateButton2 = Button.create(windowType)
uiUpdateButton2.setText('Update')
uiUpdateButton2.setUIEventCommand('guiManager.updateType()\naddAndRemoveData()')
uiUpdateButton2.setPosition(Vector2(0*util.cave, 80*util.cave))



# Time, day, date, month, year selector
timeButtonList = []
timeMenu = sysMenu.addSubMenu("Select Time")
windowTime = timeMenu.addContainer().getContainer()
windowTime.setLayout(ContainerLayout.LayoutFree)
windowTime.setMargin(1*util.cave)
windowTime.setPadding(1*util.cave)


dateLabel = Label.create(windowTime)
dateLabel.setText("MM/DD/YYYY")
dateLabel.setColor(Color("#AD9F23FF"))
dateLabel.setFont('fonts/arial.ttf 14')
dateLabel.setPosition(Vector2(82*util.cave, 5*util.cave))

timeLabel = Label.create(windowTime)
timeLabel.setText("hh:mm AM/PM")
timeLabel.setColor(Color("#AD9F23FF"))
timeLabel.setFont('fonts/arial.ttf 14')
timeLabel.setPosition(Vector2(80*util.cave, 55*util.cave))

mmButton = Button.create(windowTime)
mmButton.setText(str(util.selectedMonth))
mmButton.setPosition(Vector2(80*util.cave, 30*util.cave))
mmButton.setUIEventCommand('guiManager.inc(\'mm\')')

label1 = Label.create(windowTime)
label1.setText("/")
label1.setColor(Color("#AD9F23FF"))
label1.setFont('fonts/arial.ttf 14')
label1.setPosition(Vector2(100*util.cave, 30*util.cave))

ddButton = Button.create(windowTime)
ddButton.setText(str(util.selectedDate))
ddButton.setPosition(Vector2(120*util.cave, 30*util.cave))
ddButton.setUIEventCommand('guiManager.inc(\'dd\')')

label2 = Label.create(windowTime)
label2.setText("/")
label2.setColor(Color("#AD9F23FF"))
label2.setFont('fonts/arial.ttf 14')
label2.setPosition(Vector2(140*util.cave, 30*util.cave))

yyyyButton = Button.create(windowTime)
yyyyButton.setText(str(util.selectedYear))
yyyyButton.setPosition(Vector2(160*util.cave, 30*util.cave))
yyyyButton.setUIEventCommand('guiManager.inc(\'yyyy\')')

hrButton = Button.create(windowTime)
hrButton.setText(str(util.selectedHour))
hrButton.setPosition(Vector2(90*util.cave, 80*util.cave))
hrButton.setUIEventCommand('guiManager.inc(\'hr\')')

label3 = Label.create(windowTime)
label3.setText(":")
label3.setColor(Color("#AD9F23FF"))
label3.setFont('fonts/arial.ttf 14')
label3.setPosition(Vector2(110*util.cave, 80*util.cave))


minButton = Button.create(windowTime)
minButton.setText(str(util.selectedMin))
minButton.setPosition(Vector2(130*util.cave, 80*util.cave))
minButton.setUIEventCommand('guiManager.inc(\'min\')')

pButton = Button.create(windowTime)
pButton.setText(str(util.selectedP))
pButton.setPosition(Vector2(150*util.cave, 80*util.cave))
pButton.setUIEventCommand('guiManager.inc(\'p\')')

precisionLabel = Label.create(windowTime)
precisionLabel.setText("Precision Level:")
precisionLabel.setPosition(Vector2(90*util.cave, 110*util.cave))
precisionLabel.setColor(Color("#AD9F23FF"))
precisionLabel.setFont('fonts/arial.ttf 12')

precisionList = []
yearWindow = Button.create(windowTime)
yearWindow.setText("Year")
yearWindow.setCheckable(True)
yearWindow.setRadio(True)
yearWindow.setPosition(Vector2(60*util.cave, 130*util.cave))
precisionList.append(yearWindow)
monthWindow = Button.create(windowTime)
monthWindow.setText("Month")
monthWindow.setCheckable(True)
monthWindow.setRadio(True)
monthWindow.setPosition(Vector2(60 *util.cave, 170*util.cave))
precisionList.append(monthWindow)
dayWindow = Button.create(windowTime)
dayWindow.setText("Day")
dayWindow.setCheckable(True)
dayWindow.setRadio(True)
dayWindow.setPosition(Vector2(60*util.cave, 210*util.cave))
precisionList.append(dayWindow)
hourWindow = Button.create(windowTime)
hourWindow.setText("Hour")
hourWindow.setCheckable(True)
hourWindow.setRadio(True)
hourWindow.setPosition(Vector2(140 *util.cave, 130*util.cave))
precisionList.append(hourWindow)
minWindow = Button.create(windowTime)
minWindow.setText("Minute")
minWindow.setCheckable(True)
minWindow.setRadio(True)
minWindow.setPosition(Vector2(140 *util.cave, 170*util.cave))
precisionList.append(minWindow)
defaultWindow = Button.create(windowTime)
defaultWindow.setText("Default")
defaultWindow.setCheckable(True)
defaultWindow.setRadio(True)
defaultWindow.setPosition(Vector2(140 *util.cave, 210*util.cave))
precisionList.append(defaultWindow)

# update button
uiUpdateButton3 = Button.create(windowTime)
uiUpdateButton3.setText('Update')
uiUpdateButton3.setUIEventCommand('guiManager.updateTime()\nupdateTime()')
uiUpdateButton3.setPosition(Vector2(110*util.cave, 260*util.cave))


# Check Buttons---------------------------------------------------
# Toggle Satellite


uiMapButton = sysMenu.addButton("Satellite",'guiManager.satellite(guiManager.uiMapButton.getButton())')
uiMapButton.getButton().setCheckable(True)


# Toggle Crime Data ----------------------------------------------------
uiCrimeToggleButton = sysMenu.addButton('Crime Data','guiManager.crime(guiManager.uiCrimeToggleButton.getButton())\nmanageCrimeData()')
uiCrimeToggleButton.getButton().setCheckable(True)
uiCrimeToggleButton.getButton().setChecked(True)

# Toggle CTA data ------------------------------------------------------
uiCTAButton = sysMenu.addButton('CTA Data', 'guiManager.cta(guiManager.uiCTAButton.getButton())\nmanageCTAData()')
uiCTAButton.getButton().setCheckable(True)


# Boundaries ----------------------------------------------------------
uiBoundaryButton = sysMenu.addButton('Regionalize','guiManager.boundary(guiManager.uiBoundaryButton.getButton())\nmanageCommunities()')
uiBoundaryButton.getButton().setCheckable(True)
		
# Show Crime Count --------------------------------------------------------------------------
uiCrimeCountButton = sysMenu.addButton('Crime Count', 'guiManager.crimeCount(guiManager.uiCrimeCountButton.getButton())\nmanageCrimeCount()')
uiCrimeCountButton.getButton().setCheckable(True)

# Go real time -------------------------------------------------------------------------
uiRealTimeButton = sysMenu.addButton('Real Time Tracking','guiManager.realTime(guiManager.uiRealTimeButton.getButton())\nmanageRealTime()')
uiRealTimeButton.getButton().setCheckable(True)
		
# overview button/ Reset -------------------------------------------------------------------
overViewButton = sysMenu.addButton("Reset Cam", 'guiManager.overView()\noverView()')



# Community buttons ----------------------------------------------------------
# select type option menu

CommunitySection = sysMenu.addLabel("Options Menu")
CommunitySection.getLabel().setColor(Color("#DEDE12AE"))

page1C = sysMenu.addSubMenu("Community Page 1")
page1 = page1C.addContainer().getContainer()
page1.setLayout(ContainerLayout.LayoutVertical)

commButtonList = []
counter = 0
x = 0
y = 0
for comm in util.communityList1:
	counter += 1
	commOption = Button.create(page1)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()\nguiManager.updateComm()\njumpToCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25


page2C = sysMenu.addSubMenu("Community Page 2")
page2 = page2C.addContainer().getContainer()
page2.setLayout(ContainerLayout.LayoutVertical)


counter = 0		
x = 0
y = 0
for comm in util.communityList2:
	counter += 1
	commOption = Button.create(page2)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()\nguiManager.updateComm()\njumpToCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25


page3C = sysMenu.addSubMenu("Community Page 3")
page3 = page3C.addContainer().getContainer()
page3.setLayout(ContainerLayout.LayoutVertical)

		
		
counter = 0		
x = 0
y = 0
for comm in util.communityList3:
	counter += 1
	commOption = Button.create(page3)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()\nguiManager.updateComm()\njumpToCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25


page4C = sysMenu.addSubMenu("Community Page 4")
page4 = page4C.addContainer().getContainer()
page4.setLayout(ContainerLayout.LayoutVertical)


counter = 0		
x = 0
y = 0
for comm in util.communityList4:
	counter += 1
	commOption = Button.create(page4)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()\nguiManager.updateComm()\njumpToCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25

				
def hide():
	mm.getMainMenu().hide()

#-----------------------------------------------------------------------------------
