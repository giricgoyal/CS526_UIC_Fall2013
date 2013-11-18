/**
 * 
 */
package main;

import java.util.ArrayList;

import processing.core.PApplet;
import utils.Colors;
import utils.Util;

/**
 * @author giric
 *
 */
public class MenuManager {
	private PApplet parent;
	private float x;
	private float y;
	private float buttonW;
	private float buttonH;
	private boolean isVisible;
	
	private ArrayList<Button> buttonsLower;
	private ArrayList<Button> buttonsUpperData;
	private ArrayList<Button> buttonsUpperMap;
	private ArrayList<ConnectObjects> connections;
	private ArrayList<ConnectObjects> connectionsUpperData;
	private ArrayList<ConnectObjects> connectionsUpperMap;
	private ArrayList<String> displayDataList;
	
	
	private Button cancelButton;
	private Button quitButton;
	private Button mapButton;
	private Button dataButton;
	private Button allDataButton;
	private Button removeAllData;
	private Button removeAllMap;
	private Button holocaustDataButton;
	
	private Data dataVar;
	
	private int buttonsLowerNum;
	private float buttonsLowerAngle;
	
	private int buttonsUpperDataNum;
	private float buttonsUpperDataAngle;
	private int buttonsUpperMapNum;
	private float buttonsUpperMapAngle;
	
	MenuManager(PApplet parent, float x, float y, float w, float h){
		this.parent = parent;
		isVisible = false;
		this.x = x;
		this.y = y;
		this.buttonH = h;
		this.buttonW = w;
		
		buttonsLower = new ArrayList<Button>();
		buttonsUpperData = new ArrayList<Button>();
		buttonsUpperMap = new ArrayList<Button>();
		connections = new ArrayList<ConnectObjects>();
		connectionsUpperData = new ArrayList<ConnectObjects>();
		connectionsUpperMap = new ArrayList<ConnectObjects>();
		displayDataList = new ArrayList<String>();
		
		cancelButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		cancelButton.setButton(Colors.button_red, true, true, Colors.button_background, "Close");
		buttonsLower.add(cancelButton);
		
		quitButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		quitButton.setButton(Colors.button_quit, true, true, Colors.button_background, "Quit");
		buttonsLower.add(quitButton);
		
		mapButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		mapButton.setButton(Colors.button_blue, true, true, Colors.button_background, "Map");
		buttonsLower.add(mapButton);
		
		dataButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		dataButton.setButton(Colors.button_blue, true, true, Colors.button_background, "Data");
		buttonsLower.add(dataButton);
		
		allDataButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		allDataButton.setButton(Colors.button_green, true, true, Colors.button_background, "Casualties");
		buttonsUpperData.add(allDataButton);
		
		holocaustDataButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		holocaustDataButton.setButton(Colors.button_green, true, true, Colors.button_background, "Holocaust");
		buttonsUpperData.add(holocaustDataButton);
		
		removeAllData = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		removeAllData.setButton(Colors.button_red, true, true, Colors.button_background, "Del All");
		buttonsUpperData.add(removeAllData);
		
		removeAllMap = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		removeAllMap.setButton(Colors.button_red, true, true, Colors.button_background, "Del All");
		buttonsUpperMap.add(removeAllMap);
		
		buttonsLowerNum = buttonsLower.size();
		buttonsLowerAngle = 180f/(float)buttonsLowerNum; 
		
		buttonsUpperDataNum = buttonsUpperData.size() + 1;
		buttonsUpperDataAngle = 180f/(float)buttonsUpperDataNum;
		
		buttonsUpperMapNum = buttonsUpperMap.size() + 1;
		buttonsUpperMapAngle = 180f/(float)buttonsUpperMapNum;
		
		connections.add(new ConnectObjects(this.parent, cancelButton, quitButton, Colors.button_background, Colors.button_background));
		connections.add(new ConnectObjects(this.parent, cancelButton, mapButton, Colors.button_background, Colors.button_background));
		connections.add(new ConnectObjects(this.parent, cancelButton, dataButton, Colors.button_background, Colors.button_background));
		
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, allDataButton, Colors.button_background, Colors.button_background));
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, holocaustDataButton, Colors.button_background, Colors.button_background));
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, removeAllData, Colors.button_background, Colors.button_background));
		
		connectionsUpperMap.add(new ConnectObjects(this.parent, cancelButton, removeAllMap, Colors.button_background, Colors.button_background));
		
		System.out.println("Menu setup Done");
	}
	
	public void setXY(float x, float y) {
		this.x = x;
		this.y = y;
		
		int lowerCount = 0;
		int upperDataCount = 0;
		int upperMapCount = 0;
		
		cancelButton.setXY(this.x, this.y);
		quitButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		mapButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		dataButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		
		removeAllData.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		holocaustDataButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		allDataButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		
		removeAllMap.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperMapCount) * buttonsUpperMapAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperMapCount * buttonsUpperMapAngle))));
		
	}
	
	public void setVisible(boolean val){
		this.isVisible = val;
	}
	
	public void draw() {
		if (Util.isMenuOn) {
			parent.pushStyle();
			parent.fill(Colors.transparentGray);
			parent.rect(0,0,Util.screenW, Util.screenH);
			for (ConnectObjects cb : connections) {
				cb.draw();
			}
			if (Util.isDataButtonsOn && !Util.isConfirm) {
				for (ConnectObjects cb : connectionsUpperData) {
					cb.draw();
				}
				for (Button b : buttonsUpperData) {
					b.draw();
				}
			}
			if (Util.isMapButtonsOn && !Util.isConfirm) {
				for (ConnectObjects cb : connectionsUpperMap) {
					cb.draw();
				}
				for (Button b : buttonsUpperMap) {
					b.draw();
				}
			}
			for (Button b : buttonsLower) {
				b.draw();
			}
			parent.popStyle();
		}
	}
	
	void confirmQuit() {
		System.out.println("Confirm Quiting Application");
		quitButton.setName("Confirm");
		cancelButton.setName("Cancel");
		//Util.isDataButtonsOn = false;
		Util.isConfirm = true;
		//Util.isMapButtonsOn = false;
	}
	
	void clear() {
		this.parent.pushStyle();
		this.parent.fill(Colors.BACKGROUND_COLOR);
		this.parent.rect(0, 0, Util.screenW, Util.screenH);
		this.parent.popStyle();
	}
	
	public void isInMenu(float posX, float posY) {
		if (Util.isMenuOn) {
			if (cancelButton.checkIn(posX, posY)) {
				if (Util.isConfirm) {
					quitButton.setName("Quit");
					cancelButton.setName("Close");
					Util.isConfirm = false;
				}
				else {
					Util.isMenuOn = false;
					Util.isDataButtonsOn = false;
					Util.isMapButtonsOn = false;
					Util.isConfirm = false;
					System.out.println("Menu Off");
					parent.pushStyle();
					parent.fill(Colors.BACKGROUND_COLOR);
					parent.rect(0, 0, Util.screenW, Util.screenH);
					parent.popStyle();
					quitButton.setName("Quit");
					cancelButton.setName("Close");
				}
			}
			if (quitButton.checkIn(posX, posY)) {
				if (Util.isConfirm){
					System.out.println("Quiting Application");
					parent.exit();
				}
				else {
					confirmQuit();
				}
			}
			if (mapButton.checkIn(posX, posY)) {
				Util.isDataButtonsOn = false;
				Util.isConfirm = false;
				Util.isMapButtonsOn = Util.isMapButtonsOn? false:true;
				quitButton.setName("Quit");
				cancelButton.setName("Close");
				System.out.println("Map Selected");
			}
			if (dataButton.checkIn(posX, posY)) {
				Util.isDataButtonsOn = Util.isDataButtonsOn? false:true;
				Util.isMapButtonsOn = false;
				Util.isConfirm = false;
				quitButton.setName("Quit");
				cancelButton.setName("Close");
				System.out.println("Data Selected");
			}
			if (allDataButton.checkIn(posX, posY)) {
				dataVar.setVisible(true, "allData");
				//clear();
				Util.isDataOn = true;
			}
			if (removeAllData.checkIn(posX, posY)) {
				Util.isDataOn = false;
			}
			if (holocaustDataButton.checkIn(posX, posY)) {
				dataVar.setVisible(true, "holocaust");
				Util.isDataOn = true;
			}
		}
	}
	
	public void setDataVars(Data dataVar) {
		this.dataVar = dataVar;
	}
}
