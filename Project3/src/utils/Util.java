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
	
	public static int fontRegular = (int)scale(5);
	public static int fontMedium = (int)scale(7f);
	
}
