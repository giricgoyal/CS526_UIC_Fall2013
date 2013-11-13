/**
 * Main entry point for the application
 */

/**
 * @author giric
 *
 */

package main;

import java.io.FileNotFoundException;
import java.util.Hashtable;

import db.DataManager;
import types.TypeNameIdPair;
import utils.Colors;
import utils.Files;
import utils.Util;
import processing.core.*;
import omicronAPI.OmicronAPI;

@SuppressWarnings("serial")
public class Project3 extends PApplet {
	
	/**
	 * @param args
	 */
	public static void main(String args[]) {
		System.out.println("premain");
		PApplet.main(new String[] { "main.Project3" });
		System.out.println("postmain");
	}
	
	
	/**
	 * Variable and object declarations
	 */	
	OmicronAPI omicronManager;
	TouchListener touchListener;
	
	Map map;
	DataManager dm;
	
	
	Hashtable<String, TypeNameIdPair> generalPowersPair;
	
	/**
	 * initialize the application
	 * @throws FileNotFoundException 
	 */
	void initApp() {
		Util.font = this.loadFont("Helvetica-Bold-100.vlw");
		System.out.println("Font set");
		
		dm = new DataManager();
		
		generalPowersPair = new Hashtable<String, TypeNameIdPair>();
		generalPowersPair = dm.readPairFile(sketchPath + Files.POWERS_GENERAL);
		System.out.println("Reading Database 1 Done");
		
		map = new Map(this, "WorldMap.svg");
		System.out.println("map set");
		map.plotMapColor(generalPowersPair);
	}
	
	public void initOmicron() {
		// Creates the OmicronAPI object. This is placed in init() since we want
		// to use fullscreen
		omicronManager = new OmicronAPI(this);

		// Removes the title bar for full screen mode (present mode will not
		// work on Cyber-commons wall)
		omicronManager.setFullscreen(true);

		// Make the connection to the tracker machine
		omicronManager.ConnectToTracker(7001, 7340, "131.193.77.159");
		// Create a listener to get events
		touchListener = new TouchListener();
		touchListener.setThings(this);
		// Register listener with OmicronAPI
		omicronManager.setTouchListener(touchListener);
		System.out.println("Omicron Initiated");
	}
	
	
	void drawGridLines() {
		pushStyle();
		stroke(255, 0, 0);
		strokeWeight(1);
		line(Util.screenW/6, 0, Util.screenW/6, Util.screenH);
		line(Util.screenW * 2/6, 0, Util.screenW * 2/6, Util.screenH);
		line(Util.screenW * 3/6, 0, Util.screenW * 3/6, Util.screenH);
		line(Util.screenW * 4/6, 0, Util.screenW * 4/6, Util.screenH);
		line(Util.screenW * 5/6, 0, Util.screenW * 5/6, Util.screenH);
		line(0, Util.screenH/3, Util.screenW, Util.screenH/3);
		line(0, Util.screenH * 2/3, Util.screenW, Util.screenH * 2/3);
		popStyle();
	}
	
	/**
	 * (non-Javadoc)
	 * @see processing.core.PApplet#setup()
	 */
	public void setup(){
		
		size((int)Util.screenW, (int)Util.screenH, JAVA2D);
		background(Colors.BACKGROUND_COLOR);
		
		if (Util.isWall) {
			initOmicron();
		}
		
		initApp();
		System.out.println("App setup DONE");
		
	}
	
	
	/**
	 * (non-Javadoc)
	 * @see processing.core.PApplet#draw()
	 */
	public void draw(){
		
		if (Util.isMapOnTop) {
			map.draw();
		}
		
		if (Util.isWall) {
			omicronManager.process();
		}
		
		if (!Util.isWall) {
			drawGridLines();
		}
	}
	
	
	
	/**	
	 * 	Interaction methods
	 */
	public void myPressed(int id, float mx, float my) {
		System.out.println("mouse Pressed : " + id);
		//map.plotMapColor(generalPowersPair);
	}
	
	public void myDragged(int id, float mx, float my) {
		
	}
	
	public void myClicked(int id, float mx, float my){
		
	}
	
	public void myReleased(int id, float mx, float my) {
		
	}
	
	public void mouseDragged() {
		if (!Util.isWall)
		myDragged(-1, mouseX, mouseY);
	}

	public void mousePressed() {
		if (!Util.isWall)
		myPressed(-1, mouseX, mouseY);
	}

	public void mouseClicked() {
		if (!Util.isWall) 
		myClicked(-1, mouseX, mouseY);
	}

	public void mouseReleased() {
		if (!Util.isWall)
		myReleased(-1, mouseX, mouseY);
	}
	
	public void touchDown(int ID, float xPos, float yPos, float xWidth,
			float yWidth) {
		myPressed(ID, xPos, yPos);
	}
	
	public void touchMove(int ID, float xPos, float yPos, float xWidth,
			float yWidth) {
		myDragged(ID, xPos, yPos);
	}

	public void touchUp(int ID, float xPos, float yPos, float xWidth,
			float yWidth) {
		myReleased(ID, xPos, yPos);
	}
}
