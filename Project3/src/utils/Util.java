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
	
	public static String WHITE = "#FFFFFFFF";
	public static String BLACK = "#000000FF";
	
	public static PFont font;
	

}
