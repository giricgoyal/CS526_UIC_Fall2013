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
	else:
		print "Disabled"
		cameraManager.set2DCamera()
	#uiRoot.removeChild(windowMain)
	#uiRoot.addChild(uiOptionsButton)
	
def yearMenu():
	print "year Menu"
	if util.isYearMenuOn == False:
		windowMain.removeChild(windowType)
		windowMain.addChild(windowYear)
		windowMain.removeChild(windowComm)
		windowMain.removeChild(windowTime)
		util.isTypeMenuOn = False
		util.isCommunityMenuOn = False
		util.isTimeMenuOn = False
		windowMain.setSize(Vector2(uiSizeMaxX, uiSizeMaxY))
	else:
		windowMain.removeChild(windowYear)
		windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	util.isYearMenuOn = not(util.isYearMenuOn)
	for button in yearButtonList:
		if button.getText() == util.selectedYear:
			button.setChecked(True)
			windowYear.removeChild(uiUpdateButton1)
		else:
			button.setChecked(False)
	
def manageYear(button):
	print "Managing year : " + button.getText() + " : " + util.selectedYear
	if util.selectedYear == button.getText():
		windowYear.removeChild(uiUpdateButton1)
	else:
		if windowYear.getChildByName('uiUpdateButton1') == None:
			windowYear.addChild(uiUpdateButton1)
		
	
def update():
	print "updating"
	if util.isYearMenuOn == True:
		for button in yearButtonList:
			if button.isChecked():
				if button.getText() != util.selectedYear:
					util.selectedYear = button.getText()
					#windowMain.removeChild(windowComm)
					break
		print "New selected Year : " + util.selectedYear + ", Updating"
	elif util.isTypeMenuOn == True:
		for button in crimeTypeButtonList:
			if button.isChecked():
				if button.getText() != util.selectedCrime:
					util.selectedCrime = button.getText()
					#windowMain.removeChild(windowComm)
					break
	elif util.isCommunityMenuOn == True:
		for button in commButtonList:
			if button.isChecked():
				if button.getText() != util.selectedComm:
					util.selectedComm = button.getText()
					#windowMain.removeChild(windowComm)
					break
	elif util.isTimeMenuOn == True:
		for button in precisionList:
			if button.isChecked():
				if button.getText() != util.precisionLevel:
					util.precisionLevel = button.getText()
					break
					
	windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	windowMain.removeChild(windowComm)
	windowMain.removeChild(windowType)
	windowMain.removeChild(windowYear)
	windowMain.removeChild(windowTime)
	util.isTypeMenuOn = False
	util.isYearMenuOn = False
	util.isCommunityMenuOn = False
	util.isTimeMenuOn = False
	
def typeMenu():
	print "Type Menu"
	if util.isTypeMenuOn == False:
		windowMain.removeChild(windowYear)
		windowMain.addChild(windowType)
		windowMain.removeChild(windowComm)
		windowMain.removeChild(windowTime)
		windowMain.setSize(Vector2(uiSizeMaxX, uiSizeMaxY))
		util.isYearMenuOn = False
		util.isCommunityMenuOn = False
		util.isTimeMenuOn = False
	else:
		windowMain.removeChild(windowType)
		windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	util.isTypeMenuOn = not(util.isTypeMenuOn)
	for button in crimeTypeButtonList:
		if button.getText() == util.selectedCrime:
			button.setChecked(True)
			windowType.removeChild(uiUpdateButton2)
		else:
			button.setChecked(False)

	
def manageType():
	print "managing Type : " + util.selectedCrime
	for crime in crimeTypeButtonList:
		if crime.isChecked() == True:
			if util.selectedCrime == crime.getText():
				windowType.removeChild(uiUpdateButton2)
			else:
				if windowType.getChildByName('uiUpdateButton2') == None:
					windowType.addChild(uiUpdateButton2)
		
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
	
def commMenu():
	print "Community menu"
	if util.isCommunityMenuOn == False:
		windowMain.removeChild(windowYear)
		windowMain.addChild(windowComm)
		windowMain.removeChild(windowType)
		windowMain.removeChild(windowTime)
		windowMain.setSize(Vector2(uiSizeMaxX, uiSizeMaxY))
		util.isYearMenuOn = False
		util.isTypeMenuOn = False
		util.isTimeMenuOn = False
		addList()
	else:
		windowMain.removeChild(windowComm)
		windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	util.isCommunityMenuOn = not(util.isCommunityMenuOn)
	for button in commButtonList:
		if button.getText() == util.selectedComm:
			button.setChecked(True)
			windowComm.removeChild(uiUpdateButton2)
		else:
			button.setChecked(False)

def manageCommunity():
	print "managing Community : " + util.selectedComm
	print len(commButtonList)
	for comm in commButtonList:
		if comm.isChecked() == True:
			if util.selectedComm == comm.getText():
				windowComm.removeChild(jumpButton)
				util.isCommunityJumpButton = False
			else:
				if util.isCommunityJumpButton == False:
					windowComm.addChild(jumpButton)
					util.isCommunityJumpButton = True
					
					
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
	windowMain.removeChild(windowComm)
	windowMain.removeChild(windowYear)
	windowMain.removeChild(windowType)
	windowMain.removeChild(windowTime)
	windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	for button in commButtonList:
		button.setChecked(False)
		
		
def timeMenu():
	print "time menu on"
	if util.isTimeMenuOn == False:
		windowMain.removeChild(windowYear)
		windowMain.removeChild(windowComm)
		windowMain.removeChild(windowType)
		windowMain.addChild(windowTime)
		windowMain.setSize(Vector2(uiSizeMaxX/2, uiSizeMaxY))
		util.isYearMenuOn = False
		util.isTypeMenuOn = False
		util.isCommunityMenuOn = False
	else:
		windowMain.removeChild(windowTime)
		windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
	util.isTimeMenuOn = not(util.isTimeMenuOn)
	for button in precisionList:
		if button.getText() == util.precisionLevel:
			button.setChecked(True)
		else:
			button.setChecked(False)
			
def manageTime(button):
	print "Managing time : " + button.getText() + " : " + util.selectedTime
	if util.selectedTime == button.getText():
		windowTime.removeChild(uiUpdateButton3)
	else:
		if windowTime.getChildByName('uiUpdateButton3') == None:
			windowTime.addChild(uiUpdateButton3)
		

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
		if util.selectedYear > 2013:
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

# Create options Menu button
#uiOptionsButton = Button.create('uiOptionsButton', uiRoot)
#uiOptionsButton.setText('Options')
#uiOptionsButton.setPosition(Vector2(0,15))
#uiOptionsButton.setUIEventCommand('guiManager.toggleOptionsMenu()')


# Create container for first window
#windowMain = wf.createContainer('mainWindow', uiRoot, ContainerLayout.LayoutFree)
#windowMain.setPosition(Vector2(10,10))
#windowMain.setMargin(0)
#windowMain.setPadding(1)
#uiRoot.removeChild(windowMain)

windowMainn = sysMenu.addContainer()
windowMain = windowMainn.getContainer()
windowMain.setAutosize(False)
windowMain.setSize(Vector2(uiSizeMinX, uiSizeMaxY))
windowMain.setLayout(ContainerLayout.LayoutFree)
#windowMain.addChild(windowMain)

# Close button- ---------------------------------------------------------------------------------
# create close button
#uiCloseButton = Button.create('uiCloseButton', windowMain)
#uiCloseButton.setText('<<<')
#uiCloseButton.setPosition(Vector2(0,0))
#uiCloseButton.setUIEventCommand('guiManager.closeOptionsMenu()')

uiOptionsLabel = Label.create(windowMain)
uiOptionsLabel.setText('Options Menu')
uiOptionsLabel.setPosition(Vector2(0*util.cave,0*util.cave))
uiOptionsLabel.setColor(Color('Yellow'))
uiOptionsLabel.setFont('fonts/arial.ttf 14')

# View Menu ------------------------------------------------------------------	
# Create button for view Menu
ui3DButton = Button.create(windowMain)
ui3DButton.setText(('Disable' if util.is3DEnabled else 'Enable') + ' 3D')
ui3DButton.setPosition(Vector2(0*util.cave,15*util.cave))
ui3DButton.setUIEventCommand('guiManager.view(guiManager.ui3DButton)')


# Year Selection-----------------------------------------------------------------------------
# create select year option menu
uiYearMenuButton = Button.create(windowMain)
uiYearMenuButton.setText('Select Year')
uiYearMenuButton.setPosition(Vector2(0*util.cave, 30*util.cave))
uiYearMenuButton.setUIEventCommand('guiManager.yearMenu()')


# create container for year options
windowYear = Container.create(ContainerLayout.LayoutFree, windowMain)
windowYear.setPosition(Vector2(140*util.cave,20*util.cave))
windowYear.setMargin(1*util.cave)
windowYear.setPadding(1*util.cave)
windowYear.setSize(Vector2(400*util.cave,100*util.cave))
windowMain.removeChild(windowYear)


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
ui2012Button.setUIEventCommand('guiManager.manageYear(guiManager.ui2012Button)\nremoveCrimeData()')
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
uiUpdateButton1.setUIEventCommand('guiManager.update()\naddAndRemoveData()')
uiUpdateButton1.setPosition(Vector2(0*util.cave, 80*util.cave))



# type of crime------------------------------------------------------------------------------
# select type option menu
uiTypeMenuButton = Button.create(windowMain)
uiTypeMenuButton.setText('Select Type')
uiTypeMenuButton.setPosition(Vector2(0*util.cave, 45*util.cave))
uiTypeMenuButton.setUIEventCommand('guiManager.typeMenu()')


# container for type options
windowType = Container.create(ContainerLayout.LayoutFree, windowMain)
windowType.setPosition(Vector2(140*util.cave,20*util.cave))
windowType.setMargin(1*util.cave)
windowType.setPadding(1*util.cave)
windowType.setSize(Vector2(400*util.cave,100*util.cave))
windowMain.removeChild(windowType)


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
uiUpdateButton2.setUIEventCommand('guiManager.update()\naddAndRemoveData()')
uiUpdateButton2.setPosition(Vector2(0*util.cave, 80*util.cave))



# Community buttons ----------------------------------------------------------
# select type option menu
uiCommButton = Button.create(windowMain)
uiCommButton.setText('Select Community')
uiCommButton.setPosition(Vector2(0*util.cave, 60*util.cave))
uiCommButton.setUIEventCommand('guiManager.commMenu()')


# container for type options
windowComm = Container.create(ContainerLayout.LayoutFree, windowMain)
windowComm.setPosition(Vector2(140*util.cave,20*util.cave))
windowComm.setMargin(1*util.cave)
windowComm.setPadding(1*util.cave)
windowComm.setSize(Vector2(400*util.cave,130*util.cave))
windowMain.removeChild(windowComm)


# jump button
jumpButton = Button.create(windowComm)
jumpButton.setText("Take the Jump")
jumpButton.setPosition(Vector2(10*util.cave, 120*util.cave))
jumpButton.setUIEventCommand('guiManager.update()\njumpToCommunity()')
windowComm.removeChild(jumpButton)


# 1 to 7 buttons
numButton1 = Button.create(windowComm)
numButton1.setText("1")
numButton1.setPosition(Vector2(200*util.cave, 150*util.cave))
numButton1.setUIEventCommand('guiManager.displayListNo = 1 \nguiManager.addList()')

numButton2 = Button.create(windowComm)
numButton2.setText("2")
numButton2.setPosition(Vector2(220*util.cave, 150*util.cave))
numButton2.setUIEventCommand('guiManager.displayListNo = 2 \nguiManager.addList()')

numButton3 = Button.create(windowComm)
numButton3.setText("3")
numButton3.setPosition(Vector2(240*util.cave, 150*util.cave))
numButton3.setUIEventCommand('guiManager.displayListNo = 3 \nguiManager.addList()')

numButton4 = Button.create(windowComm)
numButton4.setText("4")
numButton4.setPosition(Vector2(260*util.cave, 150*util.cave))
numButton4.setUIEventCommand('guiManager.displayListNo = 4 \nguiManager.addList()')

numButton5 = Button.create(windowComm)
numButton5.setText("5")
numButton5.setPosition(Vector2(280*util.cave, 150*util.cave))
numButton5.setUIEventCommand('guiManager.displayListNo = 5 \nguiManager.addList()')

numButton6 = Button.create(windowComm)
numButton6.setText("6")
numButton6.setPosition(Vector2(300*util.cave, 150*util.cave))
numButton6.setUIEventCommand('guiManager.displayListNo = 6 \nguiManager.addList()')

numButton7 = Button.create(windowComm)
numButton7.setText("7")
numButton7.setPosition(Vector2(320*util.cave, 150*util.cave))
numButton7.setUIEventCommand('guiManager.displayListNo = 7 \nguiManager.addList()')

#Container for lists
# 1
listComm1 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm1.setPosition(Vector2(5*util.cave,5*util.cave))
listComm1.setMargin(1*util.cave)
listComm1.setPadding(1*util.cave)
listComm1.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm1)

# 2
listComm2 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm2.setPosition(Vector2(5*util.cave,5*util.cave))
listComm2.setMargin(1*util.cave)
listComm2.setPadding(1*util.cave)
listComm2.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm2)

# 3
listComm3 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm3.setPosition(Vector2(5*util.cave,5*util.cave))
listComm3.setMargin(1*util.cave)
listComm3.setPadding(1*util.cave)
listComm3.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm3)

# 4
listComm4 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm4.setPosition(Vector2(5*util.cave,5*util.cave))
listComm4.setMargin(1*util.cave)
listComm4.setPadding(1*util.cave)
listComm4.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm4)

# 5
listComm5 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm5.setPosition(Vector2(5*util.cave,5*util.cave))
listComm5.setMargin(1*util.cave)
listComm5.setPadding(1*util.cave)
listComm5.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm5)

# 6
listComm6 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm6.setPosition(Vector2(5*util.cave,5*util.cave))
listComm6.setMargin(1*util.cave)
listComm6.setPadding(1*util.cave)
listComm6.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm6)

# 7
listComm7 = Container.create(ContainerLayout.LayoutFree, windowComm)
listComm7.setPosition(Vector2(5*util.cave,5*util.cave))
listComm7.setMargin(1*util.cave)
listComm7.setPadding(1*util.cave)
listComm7.setSize(Vector2(400*util.cave,100*util.cave))
windowComm.removeChild(listComm7)



displayListNo = 1
commButtonList = []

counter = 0
x = 0
y = 0
for comm in util.communityList1:
	counter += 1
	commOption = Button.create(listComm1)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25

counter = 0		
x = 0
y = 0
for comm in util.communityList2:
	counter += 1
	commOption = Button.create(listComm2)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25
		
		
counter = 0		
x = 0
y = 0
for comm in util.communityList3:
	counter += 1
	commOption = Button.create(listComm3)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25
		
		
counter = 0		
x = 0
y = 0
for comm in util.communityList4:
	counter += 1
	commOption = Button.create(listComm4)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25
	
	
counter = 0		
x = 0
y = 0
for comm in util.communityList5:
	counter += 1
	commOption = Button.create(listComm5)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25
		
		
counter = 0		
x = 0
y = 0
for comm in util.communityList6:
	counter += 1
	commOption = Button.create(listComm6)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25
		
		
counter = 0		
x = 0
y = 0
for comm in util.communityList7:
	counter += 1
	commOption = Button.create(listComm7)
	commOption.setText(comm)
	commOption.setCheckable(True)
	commOption.setRadio(True)
	commButtonList.append(commOption)
	commOption.setUIEventCommand('guiManager.manageCommunity()')
	commOption.setPosition(Vector2(x*util.cave,y*util.cave))
	x += 200 
	if counter % 3 == 0:
		x = 0
		y += 25

# Time, day, date, month, year selector
timeButtonList = []

uiSelectTimeButton = Button.create(windowMain)
uiSelectTimeButton.setText("Select Time")
uiSelectTimeButton.setPosition(Vector2(0*util.cave, 75*util.cave))
uiSelectTimeButton.setUIEventCommand('guiManager.timeMenu()')

windowTime = Container.create(ContainerLayout.LayoutFree, windowMain)
windowTime.setPosition(Vector2(140*util.cave,20*util.cave))
windowTime.setMargin(1*util.cave)
windowTime.setPadding(1*util.cave)
windowTime.setSize(Vector2(200*util.cave,100*util.cave))
windowMain.removeChild(windowTime)


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
monthWindow.setPosition(Vector2(60 *util.cave, 150*util.cave))
precisionList.append(monthWindow)
dayWindow = Button.create(windowTime)
dayWindow.setText("Day")
dayWindow.setCheckable(True)
dayWindow.setRadio(True)
dayWindow.setPosition(Vector2(60*util.cave, 170*util.cave))
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
minWindow.setPosition(Vector2(140 *util.cave, 150*util.cave))
precisionList.append(minWindow)
defaultWindow = Button.create(windowTime)
defaultWindow.setText("Default")
defaultWindow.setCheckable(True)
defaultWindow.setRadio(True)
defaultWindow.setPosition(Vector2(140 *util.cave, 170*util.cave))
precisionList.append(defaultWindow)

# update button
uiUpdateButton3 = Button.create(windowTime)
uiUpdateButton3.setText('Update')
uiUpdateButton3.setUIEventCommand('guiManager.update()\nupdateTime()')
uiUpdateButton3.setPosition(Vector2(110*util.cave, 200*util.cave))


# Check Buttons---------------------------------------------------
# Toggle Satellite
uiMapButton = Button.create(windowMain)
uiMapButton.setText('Satellite')
uiMapButton.setPosition(Vector2(0*util.cave,100*util.cave))
uiMapButton.setCheckable(True)
uiMapButton.setUIEventCommand('guiManager.satellite(guiManager.uiMapButton)')


# Toggle Crime Data ----------------------------------------------------
uiCrimeToggleButton = Button.create(windowMain)
uiCrimeToggleButton.setText('Crime Data')
uiCrimeToggleButton.setPosition(Vector2(0*util.cave,125*util.cave))
uiCrimeToggleButton.setCheckable(True)
uiCrimeToggleButton.setChecked(True)
uiCrimeToggleButton.setUIEventCommand('guiManager.crime(guiManager.uiCrimeToggleButton)\nmanageCrimeData()')

# Toggle CTA data ------------------------------------------------------
uiCTAButton = Button.create(windowMain)
uiCTAButton.setText('CTA Data')
uiCTAButton.setPosition(Vector2(0*util.cave,150*util.cave))
uiCTAButton.setCheckable(True)
uiCTAButton.setUIEventCommand('guiManager.cta(guiManager.uiCTAButton)\nmanageCTAData()')


# Boundaries ----------------------------------------------------------
uiBoundaryButton = Button.create(windowMain)
uiBoundaryButton.setText('Regionalize')
uiBoundaryButton.setPosition(Vector2(0*util.cave,175*util.cave))
uiBoundaryButton.setCheckable(True)
uiBoundaryButton.setUIEventCommand('guiManager.boundary(guiManager.uiBoundaryButton)\nmanageCommunities()')
		
# Show Crime Count --------------------------------------------------------------------------
uiCrimeCountButton = Button.create(windowMain)
uiCrimeCountButton.setText('Crime Count')
uiCrimeCountButton.setPosition(Vector2(0*util.cave,200*util.cave))
uiCrimeCountButton.setCheckable(True)
uiCrimeCountButton.setUIEventCommand('guiManager.crimeCount(guiManager.uiCrimeCountButton)\nmanageCrimeCount()')

# Go real time -------------------------------------------------------------------------
uiRealTimeButton = Button.create(windowMain)
uiRealTimeButton.setText('Real Time Tracking')
uiRealTimeButton.setPosition(Vector2(0*util.cave, 225*util.cave))
uiRealTimeButton.setCheckable(True)
uiRealTimeButton.setUIEventCommand('guiManager.realTime(guiManager.uiRealTimeButton)\nmanageRealTime()')
		
# overview button/ Reset -------------------------------------------------------------------
overViewButton = Button.create(windowMain)
overViewButton.setText("Reset Cam")
overViewButton.setPosition(Vector2(0*util.cave, 255*util.cave))
#overViewButton.setCheckable(True)
#overViewButton.setChecked(True)
overViewButton.setUIEventCommand('guiManager.overView()\noverView()')
