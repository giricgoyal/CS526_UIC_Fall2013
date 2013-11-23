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
import java.util.ArrayList;
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
	private Hashtable<Integer, TypeEventsData> eventsDataPair;
	private Hashtable<String, TypeCasualtyData> casualtyData;
	private ArrayList<String> factsData;
	
	float currentX, currentY;
	
	
	int touchID1;
	int touchID2;
	PVector initTouchPos = new PVector();
	PVector initTouchPos2 = new PVector();
	PVector lastTouchPos = new PVector();
	PVector lastTouchPos2 = new PVector();
	int mapDragHack=1;
	
	Hashtable<Integer, TypeTouch> touchList;
	
	int test = 0;
	
	int directionRight = 1;
	int directionLeft = 0;
	int moveDirection = -1;
	
	
	/**
	 * initialize the application
	 * @throws FileNotFoundException 
	 */
	void initApp() {
		Util.font = this.loadFont(sketchPath + "/data/Helvetica-Bold-100.vlw");
		System.out.println(sketchPath + "/data/Helvetica-Bold-100.vlw");
		System.out.println("Font set");
		
		dm = new DataManager();
		
		touchList = new Hashtable<Integer, TypeTouch>();
		
		generalPowersPair = new Hashtable<String, TypeNameIdPair>();
		generalPowersPair = dm.readPairFile(sketchPath + Files.POWERS_GENERAL);
		System.out.println("Reading File " + Files.POWERS_GENERAL + " Done");
		
		eventsDataPair = new Hashtable<Integer, TypeEventsData>();
		eventsDataPair = dm.readEvents(sketchPath + Files.EVENTS);
		System.out.println("Reading File " + Files.EVENTS + " Done");
		
		casualtyData = new Hashtable<String, TypeCasualtyData>();
		casualtyData = dm.readDataFile(sketchPath + Files.CASUALTY_DATA);
		System.out.println("Reading File " + Files.CASUALTY_DATA + " Done");
		
		factsData = new ArrayList<String>();
		factsData = dm.readFacts(sketchPath + Files.FACTS_DATA);
		System.out.println("Reading File " + Files.FACTS_DATA + " Done");
		
		data = new Data(this, 10f, 10f, Util.dataWindowWidth, Util.dataWindowHeight);
		data.setCasualtyData(casualtyData);
		
		menu = new MenuManager(this, 0f, 0f, Util.buttonW, Util.buttonH);
		menu.setDataVars(data);
		
		mapObj = new Map(this, "WorldMap.svg");
		System.out.println("map set");
		mapObj.plotMapColor(generalPowersPair);
		mapObj.setEventsMap(eventsDataPair);
		mapObj.setFactsList(factsData);
		mapObj.loadBulletImage(sketchPath + Files.BULLET_HOLE); 
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
		frameRate(Util.frameRate);
		
		size((int)Util.screenW, (int)Util.screenH, JAVA2D);
		background(Colors.BACKGROUND_COLOR);
		
		if (Util.isWall) {
			initOmicron();
		}
		
		initApp();
		System.out.println("App setup DONE");
		drawOnce();
		//noLoop();
		//redraw();
		//mapObj.draw();
	}
	
	
	/**
	 * (non-Javadoc)
	 * @see processing.core.PApplet#draw()
	 */
	public void draw(){
		//drawOnce();
		
		Util.timer++;
		Util.timer2++;
		if (!Util.isMenuOn && !Util.isDataOn) {
			if (Util.timer2 % (Util.frameRate * 5) == 0) {
				if (!Util.isDataOn && !Util.isMenuOn) {
					Util.factIndex++;
				}
				if (Util.factIndex >= factsData.size()) {
					Util.factIndex = 0;
				}
				mapObj.drawFacts();
				//mapObj.drawAbout();
			}
		}

		/*
		if (Util.isMapAnimationOn) {
			if (Util.isPlaying == Util.PLAY) {
				if (Util.timer % (Util.frameRate * Util.speed) == 0) {
					mapObj.incrementKeyCounter();
					System.out.println(mapObj.getKeyCounter());
					clearScreen();
					drawOnce();
				}
			}
		}
		*/
		// PROCESS OMICRON
		if (Util.isWall) {
			omicronManager.process();
		}
	}
	
	
	
	/**	
	 * 	Interaction methods
	 */
	
	public void drawOnce() {
		//if (!Util.isMapOnTop) {
			clearScreen();
		//}
		mapObj.draw();
		data.draw();
		
		if (!Util.isDataOn) {
			mapObj.drawFacts();
			mapObj.drawAbout();
		}
		
		menu.draw();
		drawGridLines();
	}
	
	
	
	public void keyPressed() {
		if (key == 'a'){
			System.out.println("Menu On");
			Util.isMenuOn = true;
			Util.isPlaying = Util.STOP;
			menu.setXY(random(Util.scale(20), Util.scale(600)), random(Util.scale(20), Util.scale(150)));
			drawOnce();
		}
		if (key == 'p') {
			System.out.println("TEsting play");
			Util.isPlaying = Util.PLAY;
		}
		if (key == 's') {
			System.out.println("Testing stop");
			Util.isPlaying = Util.STOP;
			test = 0;
		}
	}
	
	public void myPressed(int id, float mx, float my) {
		System.out.println("mouse Pressed : " + id + " at : " + mx + "," + my);
		currentX = mx;
		currentY = my;
		if (Util.isWall) {
			System.out.println("Touches : " + touchList.size());
			if (touchList.size() == 5) {
				System.out.println("Menu On");
				Util.isMenuOn = true;
				Util.isPlaying = Util.STOP;
				menu.setXY(mx, my);
				//drawOnce();
			}
			if (touchList.size() == 1) {
				menu.isInMenu(mx, my);
				//drawOnce();
			}
		}
		else {
			if (id == -1) {
				menu.isInMenu(mx, my);
				//drawOnce();
			}
		}
	}
	
	public void myDragged(int id, float mx, float my) {
		if (!Util.isMenuOn) {
			if (Util.isDataOn) {
				boolean val= data.isInWindow(mx, my, currentX, currentY);
				currentX = mx;
				currentY = my;
				if (Util.onScreenData == 0) {
					Util.isMapAnimationOn = false;
					Util.isMapOnTop = true;
					Util.isDataOn = false;
					//clearScreen();
					//mapObj.draw();
				}
				//drawOnce();
			}
			else {
				if (mapObj.isInInfoPane(mx, my)) {
					if (currentX - mx < 0) {
						
						moveDirection = directionRight;
					}
					else {
						
						moveDirection = directionLeft;
					}
					currentX = mx;
					currentY = my;
				}
			}
		}
	}
	
	public void myClicked(int id, float mx, float my){
		
	}
	
	public void myReleased(int id, float mx, float my) {
		if (Util.isWall)
			touchList.remove(id);
		
		if (data.isMoving) {
			//data.moveData();
			data.isMoving = false;
		}
		
		if (!Util.isDataOn && !Util.isMenuOn) {
			if (moveDirection != -1) {
				if (moveDirection == directionLeft) {
					System.out.println("Right " + Util.infoStringIndex);
					if (Util.infoStringIndex < Util.infoString.length-1) {
						Util.infoStringIndex++;
					}
				}
				else {
					System.out.println("Left " + Util.infoStringIndex);
					if (Util.infoStringIndex > 0) {
						Util.infoStringIndex--;
					}
				}
			}
		}
		
		drawOnce();
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
	
	public void touchDown(int ID, float xPos, float yPos, float xWidth,
			float yWidth) {
		try {
			TypeTouch t = new TypeTouch(ID, xPos, yPos, xWidth, yWidth);
			System.out.println("Added Touch "+ID + " : " + t.toString());
			touchList.put(ID,t);
		} catch(Exception e) {
			e.printStackTrace();
		}
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
		touchList.remove(ID);
		System.out.println("Released Touch "+ID);
		myReleased(ID, xPos, yPos);
	}
}
