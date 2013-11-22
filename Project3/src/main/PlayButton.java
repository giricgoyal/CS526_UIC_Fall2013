/**
 * 
 */
package main;


import processing.core.PApplet;
import processing.core.PConstants;
import utils.Colors;
import utils.Util;

/**
 * @author joysword
 *
 */
public class PlayButton extends Button {

	/**
	 * @param parent
	 * @param x
	 * @param y
	 * @param width
	 * @param height
	 */
	public PlayButton(PApplet parent, float x, float y, float width,
			float height) {
		super(parent, x, y, width, height);
	}
	
	public void setXY(float x, float y) {
		this.myX = x;
		this.myY = y;
	}
	
	public void scaleButton(int scaleFactor) {
		this.myWidth = this.myWidth * scaleFactor;
		this.myHeight = this.myHeight * scaleFactor;
	}
	
	@Override
	public void draw() {
		parent.pushStyle();
		parent.fill(Colors.WHITE);
		parent.noStroke();
		
		if (Util.isPlaying == Util.PLAY) {
			parent.beginShape(PConstants.QUADS);
			parent.vertex(myX+myWidth*1/12, myY);
			parent.vertex(myX+myWidth*5/12, myY);
			parent.vertex(myX+myWidth*5/12, myY+myHeight);
			parent.vertex(myX+myWidth*1/12, myY+myHeight);
		
			parent.vertex(myX+myWidth*7/12, myY);
			parent.vertex(myX+myWidth*11/12, myY);
			parent.vertex(myX+myWidth*11/12, myY+myHeight);
			parent.vertex(myX+myWidth*7/12, myY+myHeight);
			parent.endShape();
		}
		else {
			parent.beginShape(PConstants.TRIANGLES);
			parent.vertex(myX, myY);
			parent.vertex(myX+myWidth, myY+myHeight/2);
			parent.vertex(myX, myY+myHeight);
			parent.endShape();
		}
		
		parent.popStyle();
	}
}
