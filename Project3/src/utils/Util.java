/**
 * 
 */
package utils;

/**
 * @author giric
 *
 */


import main.Map;
import main.Project3;
import processing.core.*;

@SuppressWarnings("unused")
public class Util {
	PApplet parent;
	
	public static boolean isWall = true;
	
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
	
	public static String ALLIES = "Allies";
	public static String AXIS = "Axis";
	public static String NEUTRAL = "Neutral";
	public static String SOVIET = "Soviet Union";
	public static String BELLIGERENTS = "Co-Belligerents";
	
	public static String MILITARY = "Military";
	public static String CIVILIAN = "Civilian";
	
	public static int fontSmall = (int)scale(4);
	public static int fontRegular = (int)scale(5);
	public static int fontRegular2 = (int)scale(6);
	public static int fontMedium = (int)scale(7);
	public static int fontLarge = (int)scale(8);
	
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
	
	
	public static boolean isMapOnTop = true;
	public static boolean isMenuOn = false;
	public static boolean isConfirm = false;
	public static boolean isDataButtonsOn = false;
	public static boolean isMapButtonsOn = false;
	public static boolean isMapAnimationOn = false;
	public static boolean isCompareOptionsOn = false;
	public static int listNo = 0;
	public static float buttonW = scale(26);
	public static float buttonH = scale(26);
	public static float menuH = scale(35);
	public static float menuW = scale(50);
	
	
	public static boolean isDataOn = false;
	public static float dataWindowWidth = scale(180);
	public static float dataWindowHeight = scale(180);
	public static float dataWindowRadius = scale(1.5f);

	public static String buttonCountries[] = {"Australia","Austria","Belgium","Bulgaria","Canada","China","Czechoslovakia","Denmark","Finland","France","Germany","Great Britain","Greece","Hungary","India","Italy","Japan","Netherlands","New Zealand","Norway","Philippines","Poland","Romania","South Africa","Soviet Union","Spain","United States","Yugoslavia"};
	
	public static Map mapObj;
	
	public static int onScreenData = 0;
	
	public static int STOP = 0;
	public static int PLAY = 1;
	public static int PAUSE = 2;
	public static int isPlaying = STOP;
	public static int frameRate = 120;
	public static int timer = 0;
	public static int speed = 1;
	
	public static int factIndex = 0;
	public static int timer2 = 0;
	
	public static String keyList[] = {};
	
	
	public static String infoString1 = "World War 2, also known as the Second World War, was a war fought from 1939 to 1945 in Europe and, during much of the 1930s and 1940s, in Asia.\n\nThe war in Europe began in earnest on September 1, 1939 with the invasion of Poland by Nazi Germany, and concluded on September 2, 1945, with the official surrender of the last Axis nation, Japan.\n\nHowever, in Asia the war began earlier with Japanese interventions in China, and in Europe, the war ended earlier with the unconditional surrender of Germany on May 8, 1945.";
	public static String infoString2 = "The conflict spilled over into Africa, included a handful of incidents in the Americas, and a series of major naval battles.\n\nIt was the largest armed conflict in history, spanning the entire world and involving more countries than any other war, as well as introducing powerful new weapons, culminating in the first use of nuclear weapons.\n\nHowever, despite the name, not all countries of the world were involved; some through neutrality (such as the Eire - though Eire supplied some important secret information to the Allies;"; 
	public static String infoString3 = "D-Day's date was decided on the basis of incoming Atlantic weather information supplied from Ireland - Sweden, and Switzerland), others through strategic insignificance (Mexico).\n\nThe war ravaged civilians more severely than any previous conflict and served as a backdrop for genocidal killings by Nazi Germany as well as several other mass slaughters of civilians which, although not technically genocide, were significant.\n\nThese included the massacre of millions of Chinese and Korean nationals by Japan,";
	public static String infoString4 = "internal mass killings in the Soviet Union, and the bombing of civilian targets in German and Japanese cities by the Allies. In total, World War II produced about 50 million deaths, more than any other war to date.";
	public static String infoString[] = {infoString1, infoString2, infoString3, infoString4};
	public static int infoStringIndex = 0;
}
