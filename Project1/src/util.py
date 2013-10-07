#-------------------------------------------------------
#	util.py file for utility stuff
#-------------------------------------------------------
from math import *
from euclid import *
from omega import *
from cyclops import *

class MyVertexSet:
	x = 0.0
	y = 0.0
	color = ""
	vector = Vector3(0,0,0)
	def __init__(self, x,y,color):
		self.x = x
		self.y = y
		self.color = color
		vector = Vector3(x,y,0)
		
class MyCrime:
	type = ""
	x = 0.0
	y = 0.0
	color = ""
	year = 0
	def __init__(self, type, x, y, color, year):
		self.type = type
		self.x = x
		self.y = y
		self.color = color
		self.year = year
	
class MyTrain:
	x = 0.0
	y = 0.0
	color = ""
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		
class SysDateTime:
		mm = ""
		dd = ""
		yyyy = ""
		hr = ""
		min = ""
		p = "AM"
		def __init__(self, date, time):
			self.mm = str(date.month)
			self.dd = str(date.day)
			self.yyyy = str(date.year)
			self.hr = str(time.hour)
			self.min = str(time.minute)
			if date.month < 10:
				self.mm = "0"+self.mm
			if date.day < 10:
				self.dd = "0"+self.dd
			if time.hour < 10:
				self.hr = "0"+self.hr
			if time.hour > 12:
				self.p = "PM"
				if time.hour-12 < 10:
					self.hr = "0"+str(time.hour-12)
				else:
					self.hr = str(time.hour-12)
			if time.minute < 10:
				self.min = "0"+self.min
			
			
		
city1 = None
city2 = None
city3 = None
cityMapList = [False, False, True]
light1 = None

_2001 = "2001"
_2002 = "2002"
_2003 = "2003"
_2004 = "2004"
_2005 = "2005"
_2006 = "2006"
_2007 = "2007"
_2008 = "2008"
_2009 = "2009"
_2010 = "2010"
_2011 = "2011"
_2012 = "2012"
_2013 = "2013"
_all = "s01to13"

crimeData = []
crimeList = ["Arson","Assault", "Battery", "Burglary", "Homicide", "Kidnapping", "Motor Vehicle Theft", "Narcotics", "Offence Involving Children","Prostitution" "Robbery", "Sexual Assault", "Sex Offense", "Theft", "Weapons Violation"]
communityList1 = ["ALBANY PARK", "ARCHER HEIGHTS","ARMOUR SQUARE","ASHBURN","AUBURN GRESHAM","AUSTIN","AVALON PARK","AVONDALE","BELMONT CRAGIN","BEVERLY","BRIDGEPORT","BRIGHTON PARK","BURNSIDE","CALUMET HEIGHTS","CHATHAM","CHICAGO LAWN","CLEARING","DOUGLAS","DUNNING"]
communityList2 = ["EAST GARFIELD PARK","EAST SIDE","EDGEWATER","EDISON PARK","ENGLEWOOD","FOREST GLEN","FULLER PARK","GAGE PARK","GARFIELD RIDGE","GRAND BOULEVARD","GREATER GRAND CROSSING","HEGEWISCH","HERMOSA","HUMBOLDT PARK","HYDE PARK","IRVING PARK","JEFFERSON PARK"]
communityList3 = ["KENWOOD","LAKE VIEW","LINCOLN PARK","LINCOLN SQUARE","LOGAN SQUARE","LOOP","LOWER WEST SIDE","MCKINLEY PARK","MONTCLARE","MORGAN PARK","MOUNT GREENWOOD","NEAR NORTH SIDE","NEAR SOUTH SIDE","NEAR WEST SIDE","NEW CITY","NORTH CENTER","NORTH LAWNDALE","NORTH PARK","NORWOOD PARK","OAKLAND","OHARE","PORTAGE PARK","PULLMAN"]
communityList4 = ["RIVERDALE","ROGERS PARK","ROSELAND","SOUTH CHICAGO","SOUTH DEERING","SOUTH LAWNDALE","SOUTH SHORE","UPTOWN","WASHINGTON HEIGHTS","WASHINGTON PARK","WEST ELSDON","WEST ENGLEWOOD","WEST GARFIELD PARK","WEST LAWN","WEST PULLMAN","WEST RIDGE","WEST TOWN","WOODLAWN"]


selectedYear = _2013
selectedView = "3D"
selectedCrime = "Assault"
selectedArea = 0
selectedDate = ""
selectedTime = ""
selectedComm = ""

selectedDate = 0
selectedMonth = 0
selectedHour = 0
selectedMin = 0
selectedP = "AM"
precisionLevel = "Year"

lat = 0.0
lon = 0.0
month = 0
date = 0
year = 0
time = ""
type = ""
block = 0

cave = 1

is3DEnabled = True
isCTAEnabled = False
isCrimeEnabled = True
isTypeMenuOn = False
isYearMenuOn = False
isBoundaryOn = False
isCommunityMenuOn = False
isTimeMenuOn = False
isCrimeCountOn = False
isTypeUpdateButton = False
isYearUpdateButton = False
isCommunityJumpButton = False
isRealTimeEnabled = False


def getColor(max, value, min):
	x = float(((float(value)-float(min))/(float(max)-float(min))) * 100)
	print x
	g = "00"
	r = str(hex(int((255 * x)/100)))
	b = str(hex(int((255 * (100-x))/100)))
	if len(str(r)) < 2:
		r = "0" + r
	if len(str(b)) < 2:
		b = "0" + b
	color = "#"+r.strip().split("x")[1]+g+b.strip().split("x")[1]+"88"
	#color = "#"+hex(int(r)) + hex(int(g)) + hex(int(b))
	print str(color) + " " + str(max) + " " + str(min) + " " + str(value)
	return color
	
def getColorByType(type):
	type = type.lower()
	if type == "assault":
		return "#EE121299"
	if type == "battery":
		return "#1aEF1299"
	if type == "burglary":
		return "#1111FE99"
	return "#000000FF"