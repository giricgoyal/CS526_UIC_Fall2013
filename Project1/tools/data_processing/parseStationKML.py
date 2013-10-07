from pykml import parser
railStationKMLFile = "../../data/chicago_data/cta_data/CTARailStations.kml"
railStationKMLFileParsed = "../../data/chicago_data/cta_data/CTARailStationsParsed.txt"
railStationDataFile = open(railStationKMLFile)
railStationData = ""
write = True
for line in railStationDataFile:
	if line.find("<description>") != -1:
		write = False
	if line.find("</description>") != -1:
		write = True
	if write == True:
		if line.find("</description>") == -1:
			#print line
			railStationData += line + "\n"
			
railStationData.strip()
root = parser.fromstring(railStationData)
stationName = ""
coordinates = ""
line = ""
writeToFile = open(railStationKMLFileParsed, 'w')
for i in range(0,len(root.Document.Folder.Placemark)):
	stationName = root.Document.Folder.Placemark[i].name.text
	coordinates = root.Document.Folder.Placemark[i].Point.coordinates.text
	print stationName + " : " + coordinates + " : " + str(line)
	writeToFile.write(stationName + "\t" + coordinates + "\t" + line + "\n")
