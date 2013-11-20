/**
 * Main entry point for the application
 */

/**
 * @author giric
 *
 */

package main;

import java.awt.ScrollPaneAdjustable;
import java.io.FileNotFoundException;
import java.util.Hashtable;

import db.DataManager;
import types.TypeCasualtyData;
import types.TypeEventsData;
import types.TypeNameIdPair;
import types.TypeTouch;
import utils.Colors;
import utils.Files;
import utils.Util;
import processing.core.*;
import processing.net.*;
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
	private OmicronAPI omicronManager;
	private TouchListener touchListener;
	
	private Map mapObj;
	private DataManager dm;
	private MenuManager menu;
	private Data data;
	
	
	private Hashtable<String, TypeNameIdPair> generalPowersPair;
	private Hashtable<String, TypeEventsData> eventsDataPair;
	private Hashtable<String, TypeCasualtyData> casualtyData;
	
	float currentX, currentY;
	
	
	/**
	 * initialize the application
	 * @throws FileNotFoundException 
	 */
	void initApp() {
		Util.font = this.loadFont(sketchPath + "/data/Helvetica-Bold-100.vlw");
		System.out.println(sketchPath + "/data/Helvetica-Bold-100.vlw");
		System.out.println("Font set");
		
		dm = new DataManager();
		
		generalPowersPair = new Hashtable<String, TypeNameIdPair>();
		generalPowersPair = dm.readPairFile(sketchPath + Files.POWERS_GENERAL);
		System.out.println("Reading File " + Files.POWERS_GENERAL + " Done");
		
		eventsDataPair = new Hashtable<String, TypeEventsData>();
		eventsDataPair = dm.readEvents(sketchPath + Files.EVENTS);
		System.out.println("Reading File " + Files.EVENTS + " Done");
		
		casualtyData = new Hashtable<String, TypeCasualtyData>();
		casualtyData = dm.readDataFile(sketchPath + Files.CASUALTY_DATA);
		System.out.println("Reading File" + Files.CASUALTY_DATA + " Done");
		
		
		data = new Data(this, 10f, 10f, Util.dataWindowWidth, Util.dataWindowHeight);
		data.setCasualtyData(casualtyData);
		
		menu = new MenuManager(this, 0f, 0f, Util.buttonW, Util.buttonH);
		menu.setDataVars(data);
		
		mapObj = new Map(this, "WorldMap.svg");
		System.out.println("map set");
		mapObj.plotMapColor(generalPowersPair);
		mapObj.setEventsMap(eventsDataPair);
		Util.mapObj = mapObj;
	}
	
	public void initOmicron() {
		// Creates the OmicronAPI object. This is placed in init() since we want
		// to use fullscreen
		omicronManager = new OmicronAPI(this);

		// Removes the title bar for full screen mode (present mode will not
		// work on Cyber-commons wall)
		omicronManager.setFullscreen(true);

		// Make the connection to the tracker machine
		omicronManager.connectToTracker(7001, 7340, "131.193.77.159");
		// Create a listener to get events
		touchListener = new TouchListener();
		touchListener.setThings(this);
		// Register listener with OmicronAPI
		omicronManager.setTouchListener(touchListener);
		System.out.println("Omicron Initiated");
	}
	
	void clearScreen() {
		pushStyle();
		fill(Colors.BACKGROUND_COLOR);
		rect(0,0,Util.screenW, Util.screenH);
		popStyle();
	}
	
	void drawGridLines() {
		if (!Util.isWall) {
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
		mapObj.draw();
	}
	
	
	/**
	 * (non-Javadoc)
	 * @see processing.core.PApplet#draw()
	 */
	public void draw(){
		if (!Util.isMapOnTop) {
			clearScreen();
		}
	
		data.draw();
		
		menu.draw();
		drawGridLines();
		
		// PROCESS OMICRON
		if (Util.isWall) {
			omicronManager.process();
		}
	}
	
	
	
	/**	
	 * 	Interaction methods
	 */
	
	int touchID1;
	int touchID2;
	PVector initTouchPos = new PVector();
	PVector initTouchPos2 = new PVector();
	PVector lastTouchPos = new PVector();
	PVector lastTouchPos2 = new PVector();
	int mapDragHack=1;
	
	@SuppressWarnings("rawtypes")
	Hashtable touchList;
	
	public void keyPressed() {
		if (key == 'a'){
			System.out.println("Menu On");
			Util.isMenuOn = true;
			menu.setXY(random(Util.scale(20), Util.scale(600)), random(Util.scale(20), Util.scale(150)));
		}
	}
	
	public void myPressed(int id, float mx, float my) {
		System.out.println("mouse Pressed : " + id + " at : " + mx + "," + my);
		currentX = mx;
		currentY = my;
		if (Util.isWall) {
			System.out.println("Touches : " + touchList.size());
			if (touchList.size() == 5) {
				/*
				if (Util.isMenuOn) {
					System.out.println("Menu Off");
					Util.isMenuOn = false;
				}
				*/
				//if (!Util.isMenuOn) {
					System.out.println("Menu On");
					Util.isMenuOn = true;
					menu.setXY(mx, my);
				//}
			}
			if (touchList.size() == 1) {
				menu.isInMenu(mx, my);
			}
		}
		else {
			if (id == -1) {
				menu.isInMenu(mx, my);
			}
		}
		redraw();
	}
	
	public void myDragged(int id, float mx, float my) {
		data.isInWindow(mx, my, currentX, currentY);
		currentX = mx;
		currentY = my;
	}
	
	public void myClicked(int id, float mx, float my){
		
	}
	
	public void myReleased(int id, float mx, float my) {
		if (Util.isWall)
			touchList.remove(id);
		
		if (data.isMoving) {
			data.isMoving = false;
		}
	}
	
	public void mouseDragged() {
		if (!Util.isWall) {
			myDragged(-1, mouseX, mouseY);
		}
	}

	public void mousePressed() {
		if (!Util.isWall) {
			myPressed(-1, mouseX, mouseY);
		}
	}

	public void mouseClicked() {
		if (!Util.isWall) {
			myClicked(-1, mouseX, mouseY);
		}
	}

	public void mouseReleased() {
		if (!Util.isWall) {
			myReleased(-1, mouseX, mouseY);
		}
	}
	
	@SuppressWarnings("unchecked")
	public void touchDown(int ID, float xPos, float yPos, float xWidth,
			float yWidth) {
		TypeTouch t = new TypeTouch(ID, xPos, yPos, xWidth, yWidth);
		touchList.put(ID,t);
		System.out.println("Added Touch "+ID);
		
		pushStyle();
		noFill();
		stroke(255,0,0);
		ellipse(xPos, yPos, xWidth *2, yWidth * 2);
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
