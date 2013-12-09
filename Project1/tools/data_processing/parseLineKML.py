from pykml import parser
railLinesKMLFile = "../../data/chicago_data/cta_data/CTARailLines.kml"
railLinesKMLFileParsed = "../../data/chicago_data/cta_data/CTARailLinesParsed.txt"

railLinesDataFile = open(railLinesKMLFile)
railLinesData = ""
write = True
for line in railLinesDataFile:
	if line.find("<description>") != -1:
		write = False
	if line.find("</description>") != -1:
		write = True
	if write == True:
		if line.find("</description>") == -1:
			#print line
			railLinesData += line + "\n"
			
railLinesData.strip()
root = parser.fromstring(railLinesData)
linesName = ""
coordinates = ""
line = ""
writeToFile = open(railLinesKMLFileParsed, 'w')
for i in range(0,len(root.Document.Folder.Placemark)):
	linesName = root.Document.Folder.Placemark[i].name.text
	coordinates = root.Document.Folder.Placemark[i].MultiGeometry.LineString.coordinates.text
	lineTemp = linesName.strip().split(",")
	newLine = ""
	for temp in lineTemp:
		for temp2 in temp.strip().split(" "):
			if temp2 == "(Express)":
				pass
			elif temp2 == "(Forest Park)":
				pass
			elif temp2 == "Line":
				pass
			elif temp2 == "(O'Hare)":
				pass
			elif temp2 == "(Exp)":
				pass
			elif temp2 == "(Forest":
				pass
			elif temp2 == "Park)":
				pass
			else:
				newLine += temp2 + ","
	print newLine
	writeToFile.write(newLine + "\t" + coordinates + "\n")
