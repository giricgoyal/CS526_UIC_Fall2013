package main;

import processing.core.PApplet;
/**
 * 
 * @author giric
 *
 */
public abstract class BasicControl {

	public float myX, myY, myWidth, myHeight;
	protected PApplet parent;

	public abstract void draw();

	public BasicControl(PApplet parent, float x, float y, float width, float height) {
		this.parent = parent;
		this.myX = x;
		this.myY = y;
		this.myWidth = width;
		this.myHeight = height;
	}

}
