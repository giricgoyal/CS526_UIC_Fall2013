/**
 * 
 */
package main;

import utils.Colors;
import processing.core.PApplet;
import processing.core.PConstants;

/**
 * @author joysword
 *
 */
public class StopButton extends Button {

	/**
	 * @param parent
	 * @param x
	 * @param y
	 * @param width
	 * @param height
	 */
	public StopButton(PApplet parent, float x, float y, float width,
			float height) {
		super(parent, x, y, width, height);
	}

	@Override
	public void draw() {
		parent.pushStyle();
		parent.fill(Colors.WHITE);
		parent.noStroke();
		
		parent.rectMode(PConstants.CORNER);
		parent.rect(myX, myY, myWidth, myHeight);
		
		parent.popStyle();
	}
}

