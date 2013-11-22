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
	private ArrayList<Button> compareButtonList;
	private ArrayList<Button> compareButtonList1;
	private ArrayList<Button> compareButtonList2;
	private ArrayList<Button> compareButtonList3;
	private ArrayList<Button> compareButtonList4;
	private	ArrayList<Button> listList;
	
	private Button cancelButton;
	private Button quitButton;
	private Button mapButton;
	private Button dataButton;
	private Button allDataButton;
	private Button removeAllData;
	private Button removeAllMap;
	private Button holocaustDataButton;
	private Button compareButton;
	private Button list1;
	private Button list2;
	private Button list3;
	private Button list4;
	private Button showMap;
	private Button timelineButton;
	private PlayButton playButton;
	private StopButton stopButton;
	
	private Data dataVar;
	
	private int buttonsLowerNum;
	private float buttonsLowerAngle;
	
	private int buttonsUpperDataNum;
	private float buttonsUpperDataAngle;
	private int buttonsUpperMapNum;
	private float buttonsUpperMapAngle;
	private int buttonsCompareNum;
	private float buttonsCompareAngle;
	
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
		compareButtonList = new ArrayList<Button>();
		compareButtonList1 = new ArrayList<Button>();
		compareButtonList2 = new ArrayList<Button>();
		compareButtonList3 = new ArrayList<Button>();
		compareButtonList4 = new ArrayList<Button>();
		listList = new ArrayList<Button>();
		
		cancelButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		cancelButton.setButton(Colors.button_red, true, true, Colors.button_background, "Close");
		buttonsLower.add(cancelButton);
		compareButtonList1.add(cancelButton);
		compareButtonList2.add(cancelButton);
		compareButtonList3.add(cancelButton);
		compareButtonList4.add(cancelButton);
		
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
		
		compareButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		compareButton.setButton(Colors.button_green, true, true, Colors.button_background, "Compare");
		buttonsUpperData.add(compareButton);
		
		removeAllData = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		removeAllData.setButton(Colors.button_red, true, true, Colors.button_background, "Del All");
		buttonsUpperData.add(removeAllData);
		
		removeAllMap = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		removeAllMap.setButton(Colors.button_red, true, true, Colors.button_background, "Del All");
		buttonsUpperMap.add(removeAllMap);
		
		showMap = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		showMap.setButton(Colors.button_green, true, true, Colors.button_background, "Show Map");
		buttonsUpperMap.add(showMap);
		
		timelineButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
		timelineButton.setButton(Colors.button_green, true, true, Colors.button_background, "Timeline");
		buttonsUpperMap.add(timelineButton);
		
		playButton = new PlayButton(parent, this.x, this.y, this.buttonW, this.buttonH);
		stopButton = new StopButton(parent, this.x, this.y, this.buttonW, this.buttonH);
		
		
		for (int i=0; i<Util.buttonCountries.length; i++) {
			Button tempButton = new Button(parent, this.x, this.y, this.buttonW, this.buttonH);
			tempButton.setButton(Colors.button_green, true, true, Colors.button_background, Util.buttonCountries[i]);
			compareButtonList.add(tempButton);
			if (i < Util.buttonCountries.length/4) {
				compareButtonList1.add(tempButton);
			}
			else if (i < Util.buttonCountries.length * 2 / 4) {
				compareButtonList2.add(tempButton);
			}
			else if (i < Util.buttonCountries.length * 3 / 4) {
				compareButtonList3.add(tempButton);
			}
			else if (i < Util.buttonCountries.length) {
				compareButtonList4.add(tempButton);
			}
		}
		
		list1 = new Button(parent, this.x, this.y, this.buttonW - Util.scale(15), this.buttonH - Util.scale(15));
		list1.setButton(Colors.DARK_GRAY, true, true, Colors.button_background, "1");
		listList.add(list1);
		
		list2 = new Button(parent, this.x, this.y, this.buttonW - Util.scale(15), this.buttonH - Util.scale(15));
		list2.setButton(Colors.DARK_GRAY, true, true, Colors.button_background, "2");
		listList.add(list2);

		list3 = new Button(parent, this.x, this.y, this.buttonW - Util.scale(15), this.buttonH - Util.scale(15));
		list3.setButton(Colors.DARK_GRAY, true, true, Colors.button_background, "3");
		listList.add(list3);
		
		list4 = new Button(parent, this.x, this.y, this.buttonW - Util.scale(15), this.buttonH - Util.scale(15));
		list4.setButton(Colors.DARK_GRAY, true, true, Colors.button_background, "4");
		listList.add(list4);
		
		buttonsLowerNum = buttonsLower.size();
		buttonsLowerAngle = 180f/(float)buttonsLowerNum; 
		
		buttonsUpperDataNum = buttonsUpperData.size() + 1;
		buttonsUpperDataAngle = 180f/(float)buttonsUpperDataNum;
		
		buttonsUpperMapNum = buttonsUpperMap.size() + 1;
		buttonsUpperMapAngle = 180f/(float)buttonsUpperMapNum;
		
		buttonsCompareNum = compareButtonList1.size() - 1;
		buttonsCompareAngle = 360f/(float)(buttonsCompareNum);
		
		
		connections.add(new ConnectObjects(this.parent, cancelButton, quitButton, Colors.button_background, Colors.button_background));
		connections.add(new ConnectObjects(this.parent, cancelButton, mapButton, Colors.button_background, Colors.button_background));
		connections.add(new ConnectObjects(this.parent, cancelButton, dataButton, Colors.button_background, Colors.button_background));
		
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, allDataButton, Colors.button_background, Colors.button_background));
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, holocaustDataButton, Colors.button_background, Colors.button_background));
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, removeAllData, Colors.button_background, Colors.button_background));
		connectionsUpperData.add(new ConnectObjects(this.parent, cancelButton, compareButton, Colors.button_background, Colors.button_background));
		
		connectionsUpperMap.add(new ConnectObjects(this.parent, cancelButton, removeAllMap, Colors.button_background, Colors.button_background));
		connectionsUpperMap.add(new ConnectObjects(this.parent, cancelButton, showMap, Colors.button_background, Colors.button_background));
		connectionsUpperMap.add(new ConnectObjects(this.parent, cancelButton, timelineButton, Colors.button_background, Colors.button_background));
		
		
		System.out.println("Menu setup Done");
	}
	
	public void setXY(float x, float y) {
		this.x = x;
		this.y = y;
		
		int lowerCount = 0;
		int upperDataCount = 0;
		int upperMapCount = 0;
		int compareButtonCount = 0;
		
		cancelButton.setXY(this.x, this.y);
		quitButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		mapButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		dataButton.setXY(this.x + (Util.menuW * PApplet.cos(PApplet.radians((++lowerCount) * buttonsLowerAngle))),  this.y + (Util.menuH * PApplet.sin(PApplet.radians(lowerCount * buttonsLowerAngle))));
		
		removeAllData.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		compareButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		holocaustDataButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		allDataButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperDataCount) * buttonsUpperDataAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperDataCount * buttonsUpperDataAngle))));
		
		removeAllMap.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperMapCount) * buttonsUpperMapAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperMapCount * buttonsUpperMapAngle))));
		showMap.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperMapCount) * buttonsUpperMapAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperMapCount * buttonsUpperMapAngle))));
		timelineButton.setXY(this.x +(Util.menuW * PApplet.cos(PApplet.radians((++upperMapCount) * buttonsUpperMapAngle))), this.y - (Util.menuH * PApplet.sin(PApplet.radians(upperMapCount * buttonsUpperMapAngle))));
		
		
		for (int i=0; i<compareButtonList.size(); i++) {
			compareButtonList.get(i).setXY(this.x +((Util.menuW - Util.scale(10)) * PApplet.cos(PApplet.radians((++compareButtonCount) * buttonsCompareAngle))), this.y - ((Util.menuW - Util.scale(10)) * PApplet.sin(PApplet.radians(compareButtonCount * buttonsCompareAngle))));
		}
		
		list1.setXY(this.x +(Util.scale(20) * PApplet.cos(PApplet.radians(0))), this.y - (Util.scale(20) * PApplet.sin(PApplet.radians(0))));
		list2.setXY(this.x +(Util.scale(20) * PApplet.cos(PApplet.radians(90))), this.y - (Util.scale(20) * PApplet.sin(PApplet.radians(90))));
		list3.setXY(this.x +(Util.scale(20) * PApplet.cos(PApplet.radians(180))), this.y - (Util.scale(20) * PApplet.sin(PApplet.radians(180))));
		list4.setXY(this.x +(Util.scale(20) * PApplet.cos(PApplet.radians(270))), this.y - (Util.scale(20) * PApplet.sin(PApplet.radians(270))));
	}
	
	public void setVisible(boolean val){
		this.isVisible = val;
	}
	
	public void draw() {
		if (Util.isMapAnimationOn && !Util.isDataOn) {
			this.parent.pushStyle();
			this.parent.fill(Colors.transparentBlack);
			this.parent.rect(Util.screenW / 6, 0, Util.screenW * 4 /6, Util.screenH);
			this.parent.popStyle();
			playButton.draw();
		}
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
		if (Util.isCompareOptionsOn) {
			parent.pushStyle();
			parent.fill(Colors.transparentGray);
			parent.rect(0,0,Util.screenW, Util.screenH);
			if (Util.listNo == 1) {
				for (Button b : compareButtonList1) {
					b.draw();
				}
			}
			else if (Util.listNo == 2) {
				for (Button b : compareButtonList2) {
					b.draw();
				}
			}
			else if (Util.listNo == 3) {
				for (Button b : compareButtonList3) {
					b.draw();
				}
			}
			else if (Util.listNo == 4) {
				for (Button b : compareButtonList4) {
					b.draw();
				}
			}
			for (Button b : listList) {
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
	
	void resetEverySwitch(boolean val) {
		clear();
		Util.isMapOnTop = val;
		Util.isMenuOn = val;
		dataVar.setVisible(val, "");
		Util.isCompareOptionsOn = val;
		Util.isConfirm = val;
		Util.isMapButtonsOn = val;
		Util.isConfirm = val;
		Util.isDataButtonsOn = val;
		Util.listNo = 0;
		Util.isMapAnimationOn = val;
		quitButton.setName("Quit");
		cancelButton.setName("Close");
	}
	
	public void isInMenu(float posX, float posY) {
		if (Util.isMenuOn && Util.listNo == 0) {
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
						Util.isCompareOptionsOn = false;
						System.out.println("Menu Off");
						parent.pushStyle();
						parent.fill(Colors.BACKGROUND_COLOR);
						parent.rect(0, 0, Util.screenW, Util.screenH);
						parent.popStyle();
						quitButton.setName("Quit");
						cancelButton.setName("Close");
						if (Util.isMapOnTop) {
							clear();
							//Util.mapObj.draw();
							//this.parent.redraw();
						}
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
				Util.isCompareOptionsOn = false;
				quitButton.setName("Quit");
				cancelButton.setName("Close");
				System.out.println("Map Selected");
			}
			if (dataButton.checkIn(posX, posY)) {
				Util.isDataButtonsOn = Util.isDataButtonsOn? false:true;
				Util.isMapButtonsOn = false;
				Util.isConfirm = false;
				Util.isCompareOptionsOn = false;
				quitButton.setName("Quit");
				cancelButton.setName("Close");
				System.out.println("Data Selected");
			}
			if (Util.isDataButtonsOn) {
				if (allDataButton.checkIn(posX, posY)) {
					dataVar.setVisible(true, "allData");
					clear();
					Util.isDataOn = true;
					Util.isCompareOptionsOn = false;
					Util.isMapOnTop = false;
				}
				if (removeAllData.checkIn(posX, posY)) {
					Util.isDataOn = false;
					Util.isCompareOptionsOn = false;
					dataVar.setVisible(false, "");
					clear();
					Util.isMapOnTop = true;
					//Util.mapObj.draw();
					//this.parent.redraw();
				}
				if (holocaustDataButton.checkIn(posX, posY)) {
					dataVar.setVisible(true, "holocaust");
					Util.isDataOn = true;
					Util.isCompareOptionsOn = false;
					clear();
					Util.isMapOnTop = false;
				}
				if (compareButton.checkIn(posX, posY)) {
					Util.isMenuOn = false;
					Util.isCompareOptionsOn = true;
					cancelButton.setName("Cancel");
					Util.listNo = 1;
				}
			}
			if (Util.isMapButtonsOn) {
				if (showMap.checkIn(posX, posY)) {
					resetEverySwitch(false);
					Util.isMapOnTop = true;
					//this.parent.redraw();
				}
				if (timelineButton.checkIn(posX, posY)) {
					resetEverySwitch(false);
					Util.isMapAnimationOn = true;
					Util.isMapOnTop = true;
					playButton.setXY(Util.screenW/2-this.buttonW/2, Util.screenH/2-this.buttonH/2);
					//this.parent.redraw();
				}
			}
		}
		else if (Util.listNo >= 1 && Util.listNo <= 4) {
			if (cancelButton.checkIn(posX, posY)) {
				Util.isMenuOn = true;
				Util.listNo = 0;
				Util.isCompareOptionsOn = false;
				cancelButton.setName("Close");
			}
			if (list1.checkIn(posX, posY)) {
				Util.listNo = 1;
			}
			if (list2.checkIn(posX, posY)) {
				Util.listNo = 2;
			}
			if (list3.checkIn(posX, posY)) {
				Util.listNo = 3;
			}
			if (list4.checkIn(posX, posY)) {
				Util.listNo = 4;
			}
			if (Util.listNo == 1) {
				for (Button b : compareButtonList1) {
					if (b.checkIn(posX, posY)) {
						System.out.println(b.getName());
						dataVar.setVisible(true, b.getName());
						Util.isDataOn = true;
						Util.isMapOnTop = false;
						clear();
					}
				}
			}
			if (Util.listNo == 2) {
				for (Button b : compareButtonList2) {
					if (b.checkIn(posX, posY)) {
						System.out.println(b.getName());
						dataVar.setVisible(true, b.getName());
						Util.isDataOn = true;
						Util.isMapOnTop = false;
						clear();
					}
				}
			}
			if (Util.listNo == 3) {
				for (Button b : compareButtonList3) {
					if (b.checkIn(posX, posY)) {
						System.out.println(b.getName());
						dataVar.setVisible(true, b.getName());
						Util.isDataOn = true;
						Util.isMapOnTop = false;
						clear();
					}
				}
			}
			if (Util.listNo == 4) {
				for (Button b : compareButtonList4) {
					if (b.checkIn(posX, posY)) {
						System.out.println(b.getName());
						dataVar.setVisible(true, b.getName());
						Util.isDataOn = true;
						Util.isMapOnTop = false;
						clear();
					}
				}
			}
		}
		else if (Util.isMapAnimationOn) {
			// if in Play button are (whole map screen)
			if (posX >= Util.screenW/6 && posX <= Util.screenW * 5/6) {
				if (posY >= 0 && posY <= Util.screenH){
					Util.isPlaying = Util.PLAY;
					playButton.setXY(Util.screenW * 5 /6 - (2 * this.buttonW) - Util.scale(5), Util.screenH - this.buttonH - Util.scale(2.5f));
					this.parent.loop();
				}
			}
		}
	}
	
	public void setDataVars(Data dataVar) {
		this.dataVar = dataVar;
	}
}
