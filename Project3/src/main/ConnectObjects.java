/**
 * 
 */
package main;

import processing.core.PApplet;
import utils.Util;

/**
 * @author giric
 *
 */
public class ConnectObjects {
	private PApplet parent;
	private Button firstObj;
	private Button secondObj;
	private int color;
	private int backgroundColor;
	
	public ConnectObjects(PApplet parent, Button firstObj, Button secondObj, int color, int backgroundColor) {
		this.parent = parent;
		this.firstObj = firstObj;
		this.secondObj = secondObj;
		this.color = color;
		this.backgroundColor = backgroundColor;
	}
	
	public void setColors(int color, int backgroundColor) {
		this.color = color;
		this.backgroundColor = backgroundColor;
	}
	
	public void draw() {
		parent.pushStyle();
		parent.fill(color);
		parent.stroke(backgroundColor);
		parent.strokeWeight(Util.scale(1.5f));
		parent.line(firstObj.myX, firstObj.myY, secondObj.myX, secondObj.myY);
		parent.popStyle();
	}
}
