/**
 * 
 */
package utils;

/**
 * @author giric
 *
 */


import main.Project3;
import processing.core.*;

@SuppressWarnings("unused")
public class Util {
	PApplet parent;
	
	public static boolean isWall = false;
	
	Util(PApplet p){
		this.parent = p;
	}
	
	public static float scale(float pixel) {
		if (isWall) {
			return pixel*12;
		}
		else {
			return pixel*2;
		}
	}
	
	public static float screenW = scale(680);
	public static float screenH = scale(192);
	

	public static float legendX = Util.screenW/6 + Util.scale(5);
	public static float legendY = Util.screenH *2/3 + Util.scale(15);
	public static float legendH = Util.scale(40);
	public static float legendW = Util.scale(50);
	public static float legendR = Util.scale(0.5f);
	
	
	public static PFont font;
	
	public static boolean isMapOnTop = true;
	
	public static String ALLIES = "Allies";
	public static String AXIS = "Axis";
	public static String NEUTRAL = "Neutral";
	public static String SOVIET = "Soviet Union";
	public static String BELLIGERENTS = "Co-Belligerents";
	
	public static int fontSmall = (int)scale(4);
	public static int fontRegular = (int)scale(5);
	public static int fontMedium = (int)scale(7f);
	
	public static float INVALID_LATLON = -999f;
	
	public static int monthIndex(String month) {
		if (month.compareTo("Jan") == 0)
			return 1;
		else if (month.compareTo("Feb") == 0) 
			return 2;
		else if (month.compareTo("March") == 0)
			return 3;
		else if (month.compareTo("April") == 0)
			return 4;
		else if (month.compareTo("May") == 0)
			return 5;
		else if (month.compareTo("June") == 0)
			return 6;
		else if (month.compareTo("July") == 0) 
			return 7;
		else if (month.compareTo("Aug") == 0)
			return 8;
		else if (month.compareTo("Sept") == 0) 
			return 9;
		else if (month.compareTo("Oct") == 0)
			return 10;
		else if (month.compareTo("Nov") == 0)
			return 11;
		else if (month.compareTo("Dec") == 0)
			return 12;
		return 0;
	}
	
	
	public static boolean isMenuOn = false;
	public static boolean isConfirm = false;
	public static boolean isDataButtonsOn = false;
	public static boolean isMapButtonsOn = false;
	public static float buttonW = scale(26);
	public static float buttonH = scale(26);
	public static float menuH = scale(40);
	public static float menuW = scale(40);
	
	
	public static boolean isDataOn = false;
	public static float dataWindowWidth = scale(180);
	public static float dataWindowHeight = scale(180);
	public static float dataWindowRadius = scale(1.5f);
}
