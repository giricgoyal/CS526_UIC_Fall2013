/**
 * 
 */
package db;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Map;

import types.TypeCasualtyData;
import types.TypeEventsData;
import types.TypeNameIdPair;
import types.TypeShapeColorPair;
import utils.Util;

/**
 * @author giric
 *
 */
public class DataManager {
	private Hashtable<String, TypeNameIdPair> nameIdPair = new Hashtable<String, TypeNameIdPair>();
	private Hashtable<Integer, TypeEventsData> eventsDataPair = new Hashtable<Integer, TypeEventsData>();
	private Hashtable<String, TypeCasualtyData> casualtyData = new Hashtable<String, TypeCasualtyData>();
	private ArrayList<String> factsData = new ArrayList<String>();
	
	public ArrayList<String> readFacts(String file) {
		try {
			BufferedReader fileIn = new BufferedReader(new FileReader(file));
			String aLine;
			while((aLine = fileIn.readLine()) != null) {
				if (aLine != "" || aLine != null) {
					factsData.add(aLine);
				}
			}
			return factsData;
		}	catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	public Hashtable<String, TypeCasualtyData> readDataFile(String file) {
		try {
			BufferedReader fileIn = new BufferedReader(new FileReader(file));
			String aLine;
			String aLineArray[];
			while((aLine = fileIn.readLine()) != null) {
				if (aLine.startsWith("//")) { 
					continue;
				}
				else {
					aLineArray = aLine.split("\t");
					String name = aLineArray[0].trim();
					float totalCasualities = Float.valueOf(aLineArray[1].trim()).floatValue();
					float civilianCasualityies = Float.valueOf(aLineArray[3].trim()).floatValue();
					float militaryCasualities = Float.valueOf(aLineArray[2].trim()).floatValue();
					float holocaustCasualities = Float.valueOf(aLineArray[4].trim()).floatValue();
					this.casualtyData.put(name, new TypeCasualtyData(name, totalCasualities, civilianCasualityies, militaryCasualities, holocaustCasualities));
				}
			}
			return this.casualtyData;
		}	catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	@SuppressWarnings("resource")
	public Hashtable<String,TypeNameIdPair> readPairFile(String file) {
		try {
			BufferedReader fileIn = new BufferedReader(new FileReader(file));
			String aLine;
			String aLineArray[];
			String side = "";
			while ((aLine = fileIn.readLine()) != null) {
				if (aLine.compareTo("") == 0) 
					continue;
				if (aLine.compareTo("\n") == 0) 
					continue;
				if (aLine.contains("//")) {
					if (aLine.contains("Allies"))
						side = Util.ALLIES;
					else if (aLine.contains("Co"))
						side = Util.BELLIGERENTS;
					else if (aLine.contains("Axis"))
						side = Util.AXIS;
					else if (aLine.contains("Neutral"))
						side = Util.NEUTRAL;
				}
				else {
					aLineArray = aLine.split("\t");
					String name = aLineArray[0].trim();
					String id = aLineArray[1].trim();
					this.nameIdPair.put(name, new TypeNameIdPair(name, id, side));
				}
			}
			return this.nameIdPair;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public Hashtable<Integer, TypeEventsData> readEvents(String file){
		try{
			BufferedReader fileIn = new BufferedReader(new FileReader(file));
			String aLine;
			int id;
			int dd;
			int mm;
			int yyyy;
			String date;
			String name;
			String description;
			String fileN;
			String locs;
			float lat;
			float lon;
			Hashtable<String, TypeShapeColorPair> ht;
			Hashtable<String, TypeNameIdPair> nameIdHt;
			String aLineArray[];
			while((aLine = fileIn.readLine()) != null){
				ht = new Hashtable<String, TypeShapeColorPair>();
				nameIdHt = new Hashtable<String, TypeNameIdPair>();
				aLineArray = aLine.split("\t");
				id = Integer.valueOf(aLineArray[0].trim()).intValue();
				date = aLineArray[1].trim();
				dd = Integer.valueOf(date.split(" ")[0].trim()).intValue();
				mm = Util.monthIndex(date.split(" ")[1].trim());
				yyyy = Integer.valueOf(date.split(" ")[2].trim()).intValue();
				name = aLineArray[3].trim();
				description = aLineArray[4].trim();
				locs = aLineArray[2].trim();
				lat = Util.INVALID_LATLON;
				lon = Util.INVALID_LATLON;
				if (locs.contains(";")) {
					String l1 = locs.split(";")[0].trim();
					String l2 = locs.split(";")[1].trim();
					String side1 = l1.split(":")[0].trim();
					String arr1 = l1.split(":")[1].trim();
					String side2 = l2.split(":")[0].trim();
					String arr2 = l2.split(":")[1].trim();
					String array1[] = arr1.split(",");
					String array2[] = arr2.split(",");
					for (String a : array1) {
						if (a.contains("loc")) {
							lat = Float.valueOf(a.split(" ")[1].trim()).floatValue();
							lon = Float.valueOf(a.split(" ")[2].trim()).floatValue();
						}
						else {
							nameIdHt.put(a, new TypeNameIdPair("",a,side1));
						}
					}
					for (String a: array2) {
						if (a.contains("loc")) {
							lat = Float.valueOf(a.split(" ")[1].trim()).floatValue();
							lon = Float.valueOf(a.split(" ")[2].trim()).floatValue();
						}
						else {
							nameIdHt.put(a, new TypeNameIdPair("",a,side2));
						}
					}
				}
				else {
					if (locs.contains("Victory")) {
					
					}
					else {
						String side = locs.split(":")[0].trim();
						String arr = locs.split(":")[1].trim();
						String array[] = arr.split(",");
						for (String a : array) {
							if (a.contains("loc")) {
								lat = Float.valueOf(a.split(" ")[1].trim()).floatValue();
								lon = Float.valueOf(a.split(" ")[2].trim()).floatValue();
							}
							else {
								nameIdHt.put(a, new TypeNameIdPair("",a,side));
							}
						}
					}
				}
				eventsDataPair.put(id, new TypeEventsData(id, dd, mm, yyyy, date, name, description, "", lat, lon, ht, nameIdHt));
			}
			return this.eventsDataPair;
		}	catch(Exception e){
			e.printStackTrace();
		}
		return null;
	}
}
