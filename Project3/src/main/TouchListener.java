package main;
import processing.core.PApplet;
import omicronAPI.*;
/**
 * 
 * @author giric
 *
 */
public class TouchListener implements OmicronTouchListener {

	private PApplet parent;

	public void setThings(PApplet parent) {this.parent=parent;}
	
	// Called on a touch down event
	// mousePressed events also call this with an ID of -1 and an xWidth and
	// yWidth of 10.
	@Override
	public void touchDown(int ID, float xPos, float yPos, float xWidth, float yWidth) {
		/*cp5.getPointer().setX(parent.ceil(xPos));
		cp5.getPointer().setY(parent.ceil(yPos));
		cp5.getPointer().pressed();*/

		// This is an optional call if you want the function call in the main
		// applet class.
		// 'OmicronExample' should be replaced with the sketch name i.e.
		// ((SketchName)applet).touchDown( ID, xPos, yPos, xWidth, yWidth );
		// Make sure applet is defined as PApplet and that 'applet = this;' is
		// in setup().
		((Project3) parent).touchDown(ID, xPos, yPos, xWidth, yWidth);
		parent.ellipse(xPos, yPos, xWidth, yWidth);
	}// touchDown

	// Called on a touch move event
	// mouseDragged events also call this with an ID of -1 and an xWidth and
	// yWidth of 10.
	public void touchMove(int ID, float xPos, float yPos, float xWidth,	float yWidth) {
		
		((Project3) parent).touchMove(ID, xPos, yPos, xWidth, yWidth);
		parent.ellipse(xPos, yPos, xWidth, yWidth);
	}// touchMove

	// Called on a touch up event
	// mouseReleased events also call this with an ID of -1 and an xWidth and
	// yWidth of 10.
	public void touchUp(int ID, float xPos, float yPos, float xWidth, float yWidth) {
		//cp5.getPointer().released();

		((Project3) parent).touchUp(ID, xPos, yPos, xWidth, yWidth);
	}// touchUp

	

}// TouchListener
