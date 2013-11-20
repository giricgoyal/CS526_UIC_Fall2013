package main;

import java.awt.Color;

import utils.Colors;
import utils.Util;
import processing.core.PApplet;
import processing.core.PConstants;

/**
 * Button class. Create a button and assign a name to it.
 * If you want the button change color while selected call setShowClicked()
 * @author Giric
 *
 */
public class Button extends BasicControl {
	private boolean selected;
	private boolean showClicked;
	private boolean addStroke;
	private String name;
	private boolean elps;
	private int color;
	private int borderColor;

	public Button(PApplet parent, float x, float y, float width, float height) {
		super(parent, x, y, width, height);
		elps=false;
		selected = false;
		addStroke = false;
		showClicked = false;
		name = "";
		color = 0;
		borderColor = Colors.DARK_GRAY;
	}
	
	@Override
	public void draw() {
		parent.pushStyle();
		if(showClicked) parent.fill(selected?Colors.buttonSelectedColor:Colors.buttonColor);
		else parent.fill(color);
		if(addStroke) {
			parent.stroke(borderColor);
			parent.strokeWeight(Util.scale(1));
		}
		else {
			parent.noStroke();
		}
		parent.rectMode(PConstants.CORNER);
		parent.ellipseMode(PConstants.CENTER);
		if(elps) parent.ellipse(myX, myY, myWidth, myHeight);
		else 
			parent.rect(myX, myY, myWidth, myHeight);
		parent.textAlign(PConstants.CENTER,PConstants.CENTER);
		parent.fill(borderColor);
		parent.textFont(Util.font);
		if(elps) {
			parent.textSize(Util.scale(5));
			parent.text(name, myX, myY);
		}
		else { 
		parent.textSize(Util.scale(5));
		parent.text(name, (myWidth)/2+myX, (myHeight)/2+myY);
		}
		parent.popStyle();
	}
	
	public void setXY(float x, float y) {
		myX = x;
		myY = y;
	}
	
	public void setHW(float h, float w) {
		myHeight = h;
		myWidth = w;
	}
	
	public boolean isSelected(){
		return selected;
	}
	
	public void setElps(boolean val){
		this.elps = val;
	}

	public boolean checkIn(float posX,float posY){
		if (elps){
			float radius = myWidth/2;
			//System.out.println(posX + "," + posY + " : " + myX + "," + myY);
			float tempDist = PApplet.dist(posX, posY, myX, myY);
			//System.out.println(radius);
			//System.out.println(tempDist);
			return tempDist<=radius ? true : false;
		}
		return (myX<posX && posX<myX+myWidth && myY<posY && posY<myY+myHeight) ? true: false;
	}
	
	public void setSelected(boolean selected){
		this.selected = selected;
	}
	
	public void setName(String name){
		this.name=name;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void setShowClick(){
		this.showClicked=true;
	}
	
	public void setColor(int color) {
		this.color = color;
	}
	
	
	public void setButton(int color, boolean elps, boolean stroke, int bkColor, String name) {
		setColor(color);
		setElps(elps);
		setStroke(stroke, bkColor);
		setName(name);
	}
	
	public void setStroke(boolean val, int color){
		this.addStroke = val;
		this.borderColor = color;
	}
}
