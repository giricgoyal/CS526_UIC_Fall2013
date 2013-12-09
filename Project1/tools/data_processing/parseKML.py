from pykml import parser
communityFile = "../../data/chicago_data/community_data/communityData.kml"
communityFileProcessed = "../../data/chicago_data/community_data/communityData.txt"
communityDataFile = open(communityFile)
communityData = ""
write = True
for line in communityDataFile:
	if line.find("<description>") != -1:
		write = False
	if line.find("</description>") != -1:
		write = True
	if write == True:
		if line.find("</description>") == -1:
			#print line
			railStationData += line + "\n"
	if write == False:
		if line.find("COMMUNITY") == -1:
			tempname = line[line.rfind("\">")+2:line.rfind("</span>")]
			print tempName
			
communityData.strip()
root = parser.fromstring(communityData)
stationName = ""
coordinates = ""
line = ""
writeToFile = open(communityFileProcessed, 'w')
#for i in range(0,len(root.Document.Folder.Placemark)):
#	stationName = root.Document.Folder.Placemark[i].name.text
#	coordinates = root.Document.Folder.Placemark[i].Point.coordinates.text
	
#	print stationName + " : " + coordinates + " : " + str(line)
#	writeToFile.write(stationName + "\t" + coordinates + "\t" + line + "\n")

