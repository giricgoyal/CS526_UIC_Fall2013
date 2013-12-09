from pykml import parser
communityFile = "../../data/chicago_data/community_data/communityData.kml"
communityFileProcessed = "../../data/chicago_data/community_data/communityData.txt"
commFile2 = "../../data/chicago_data/community_data/communityLocation.txt"
communityDataFile = open(communityFile)
communityData = ""
communityName = []
areaNum = []
write = True
for line in communityDataFile:
	if line.find("<description>") != -1:
		write = False
	if line.find("</description>") != -1:
		write = True
	if write == True:
		if line.find("</description>") == -1:
			print line
			communityData += line + "\n"
	if write == False:
		if line.find("COMMUNITY") != -1:
			tempName = line[line.rfind("\">")+2:line.rfind("</span>")]
			print tempName
			communityName.append(tempName)
		if line.find("AREA_NUMBE") != -1:
			tempName = line[line.rfind("\">")+2:line.rfind("</span>")]
			print tempName
			areaNum.append(tempName)
			
communityData.strip()
root = parser.fromstring(communityData)
stationName = ""
coordinates = ""
point = ""
writeToFile = open(communityFileProcessed, 'w')
writeToFile2 = open(commFile2, 'w')
for i in range(0,len(root.Document.Placemark)):
	commName = communityName[i]
	coordinates = root.Document.Placemark[i].MultiGeometry.Polygon.outerBoundaryIs.LinearRing.coordinates.text
	point = root.Document.Placemark[i].MultiGeometry.Point.coordinates.text
	#print commName + " : " + coordinates
	c1 = coordinates.strip().split(" ")
	newList = ""
	for t in (temp.strip().split(",") for temp in c1):
		for t2 in t:
			print t2
			newList += t2 + ","
	newList.rstrip(",")
	writeToFile.write(commName + "\t" + newList + "\t" + areaNum[i] + "\t" + point + "\n")
	writeToFile2.write(commName + "\t" + areaNum[i] + "\t" + point + "\n")
	

