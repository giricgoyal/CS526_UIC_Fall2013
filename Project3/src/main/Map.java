/**
 * 
 */
package main;

import utils.Util;
import processing.core.PApplet;
import processing.core.PConstants;
import processing.core.PShape;

/**
 * @author giric
 *
 */
public class Map {
	PShape map;
	PApplet parent;
	
	public Map(PApplet p, String file) {
		this.parent = p;
		map = this.parent.loadShape(file);
		//map.scale((float)(map.width/Util.screenW), (float)(map.height/Util.screenH));
		map.scale(0.55f, 0.35f);
	}
	
	@SuppressWarnings("static-access")
	public void draw() {
		parent.shapeMode(parent.CORNER);
		parent.shape(map, Util.screenW/6, 0);
	}
}
