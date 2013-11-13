/**
 * 
 */
package db;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;

import types.TypeNameIdPair;
import utils.Util;

/**
 * @author giric
 *
 */
public class DataManager {
	Hashtable<String,TypeNameIdPair> nameIdPair = new Hashtable<String,TypeNameIdPair>();
	
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
					nameIdPair.put(name, new TypeNameIdPair(name, id, side));
				}
			}
			return this.nameIdPair;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
}
