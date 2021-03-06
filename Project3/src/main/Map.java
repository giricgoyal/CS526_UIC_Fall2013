/**
 * 
 */
package main;

import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Enumeration;
import java.util.Hashtable;

import types.TypeEventsData;
import types.TypeNameIdPair;
import types.TypeShapeColorPair;
import utils.Colors;
import utils.Util;
import processing.core.PApplet;
import processing.core.PConstants;
import processing.core.PImage;
import processing.core.PShape;

/**
 * @author giric
 *
 */
public class Map {
	private PShape map;
	private PApplet parent;
	private PShape x, y;
	private PShape child;
	PShape china;
	private Hashtable<String,TypeShapeColorPair> ht;
	//private Hashtable<String,TypeShapeColorPair> allChildren;
	private Hashtable<Integer, TypeEventsData> eventsDataHt;
	private ArrayList<String> factsList;
	private int keyCounter;
	
	private PImage bulletHole;
	
	
	private float tl_x;
	private float tl_y;
	private float tl_w;
	private float tl_h;
	private ArrayList<Integer> tl_idList;
	
	
	public Map(PApplet p, String file) {
		this.parent = p;
		map = this.parent.loadShape(file);
		x = this.parent.loadShape(file);
		y = this.parent.loadShape(file);
		map.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
		//x = map.getChild("path4123");
		//x.scale(0.55f, 0.35f);
		ht = new Hashtable<String, TypeShapeColorPair>();
		eventsDataHt = new Hashtable<Integer, TypeEventsData>();
		factsList = new ArrayList<String>();
		tl_idList = new ArrayList<Integer>();
		
		bulletHole = new PImage();
		keyCounter = 1;
		
		china = map.getChild("path3691");
		china.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
	}
	
	void drawOverViewMap() {
		Enumeration<String> keys;
		String key;
		PShape tempShape;
		int color;
		keys = this.ht.keys();
		TypeShapeColorPair tp;
		while(keys.hasMoreElements()) {
			key = (String)keys.nextElement();
			tp = this.ht.get(key);
			tempShape = tp.getShape();
			color = tp.getColor();
			//System.out.println(tp.getName() + tp.getColor());
			tempShape.disableStyle();
			parent.fill(color);
			parent.noStroke();
			parent.shape(tempShape, Util.screenW/6, 0);
		}
		
		
		china.disableStyle();
		parent.fill(Colors.ALLIES);
		//parent.shape(china, -894,-7);
		parent.shape(china, -Util.scale(447),-Util.scale(3.5f));
		china.enableStyle();
		
		parent.noStroke();
		parent.smooth();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontMedium);
		parent.fill(Colors.TEXT_GRAY);
		parent.text("Who Fought Whom? (1939-1945)", Util.legendX, Util.legendY - Util.scale(10));
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.MEDIUM_GRAY);
		parent.fill(Colors.DARK_GRAY);
		parent.rect(Util.legendX, Util.legendY, Util.legendW, Util.legendH, Util.legendR);
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.ALLIES_BORDER);
		parent.fill(Colors.ALLIES);
		parent.rect(Util.legendX + Util.scale(2), Util.legendY + Util.scale(3), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
		parent.noStroke();
		parent.smooth();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontRegular);
		parent.fill(Colors.TEXT_GRAY);
		parent.text(Util.ALLIES, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + Util.scale(4));
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.AXIS_BORDER);
		parent.fill(Colors.AXIS);
		parent.rect(Util.legendX + Util.scale(2), Util.legendY + Util.scale(2) + Util.legendH/5, Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
		parent.noStroke();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontRegular);
		parent.fill(Colors.TEXT_GRAY);
		parent.text(Util.AXIS, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + Util.scale(3) + Util.legendH/5);
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.SOVIET_BORDER);
		parent.fill(Colors.SOVIET);
		parent.rect(Util.legendX + Util.scale(2), Util.legendY + (2*Util.legendH/5) + Util.scale(1), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
		parent.noStroke();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontRegular);
		parent.fill(Colors.TEXT_GRAY);
		parent.text(Util.SOVIET, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (2*Util.legendH/5) + Util.scale(2));
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.BELLIGERENTS_BORDER);
		parent.fill(Colors.BELLIGERENTS);
		parent.rect(Util.legendX + Util.scale(2), Util.legendY + (3 * Util.legendH/5), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
		parent.noStroke();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontRegular);
		parent.fill(Colors.TEXT_GRAY);
		parent.text(Util.BELLIGERENTS, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (3 * Util.legendH/5) + Util.scale(1));
		
		parent.strokeWeight(Util.scale(0.5f));
		parent.stroke(Colors.NEUTRAL_BORDER);
		parent.fill(Colors.NEUTRAL);
		parent.rect(Util.legendX + Util.scale(2), Util.legendY + (4 * Util.legendH/5) - Util.scale(1), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
		parent.noStroke();
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.textFont(Util.font);
		parent.textSize(Util.fontRegular);
		parent.fill(Colors.TEXT_GRAY);
		parent.text(Util.NEUTRAL, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (4 * Util.legendH/5));
		
		
		parent.stroke(Colors.DARK_GRAY);
	}
	
	public void drawTimeline() {
		try {
			drawOverViewMap();
			Util.menuObj.emptyTimeLineList();
			
			parent.pushStyle();
			parent.fill(Colors.transparentBlack);
			parent.rect(Util.screenW / 6, 0, Util.screenW * 4 /6, Util.screenH);
			parent.fill(Colors.DARK_WHITE);
			parent.stroke(Colors.DARK_WHITE);
			parent.stroke(Util.scale(0.5f));
			parent.rect(Util.screenW/6 + Util.scale(30), Util.screenH - Util.scale(30), Util.screenW * 4/6 - Util.scale(60), Util.scale(10));
			parent.popStyle();
			
			int start = 1937;
			int end = 1945;
			int counter = 0;
			float x = Util.screenW / 6 + Util.scale(30);
			while(start+counter < end) {
				parent.pushStyle();
				float xPrime = x;
				counter++;
				x = PApplet.map(start + counter, start, end, Util.screenW / 6 + Util.scale(30), Util.screenW * 5/6 - Util.scale(30));
				parent.stroke(Colors.BLACK);
				parent.line(x, Util.screenH - Util.scale(30), x, Util.screenH - Util.scale(20));
				parent.fill(Colors.WHITE);
				parent.textSize(Util.fontMedium);
				parent.textAlign(PConstants.CENTER, PConstants.CENTER);
				parent.text(start + counter, x-(x-xPrime)/2, Util.screenH - Util.scale(10));
				
				int monS = 0;
				int monE = 12;
				int monCounter = 0;
				float monX;
				while(monS + monCounter < monE) {
					monCounter++;
					monX = PApplet.map(monS+monCounter, monS, monE, xPrime, x);
					parent.stroke(Colors.white);
					parent.line(monX, Util.screenH - Util.scale(27), monX, Util.screenH - Util.scale(23));
				}
				
				parent.popStyle();
			}
			
			Enumeration keys = eventsDataHt.keys();
			int key;
			while(keys.hasMoreElements()) {
				key = (Integer)keys.nextElement();
				int dd = this.eventsDataHt.get(key).getDd();
				int mm = this.eventsDataHt.get(key).getMm();
				int yyyy = this.eventsDataHt.get(key).getYyyy();
				int id = this.eventsDataHt.get(key).getId();
				float mapYear = PApplet.map(yyyy, start, end, Util.screenW / 6 + Util.scale(30), Util.screenW * 5/6 - Util.scale(30));
				float mapYearPrev = PApplet.map(yyyy-1, start, end, Util.screenW / 6 + Util.scale(30), Util.screenW * 5/6 - Util.scale(30));
				float mapMonth = PApplet.map(mm-1, 0, 12, mapYearPrev, mapYear);
				float mapMonthPrev = PApplet.map(mm-2, 0, 12, mapYearPrev, mapYear);
				
				parent.fill(Colors.RED);
				parent.rect(mapMonth, Util.screenH - Util.scale(27), mapMonth - mapMonthPrev, Util.scale(4));
				
				Util.menuObj.addButtonToTimeLineList(mapMonth, Util.screenH - Util.scale(30), mapMonth - mapMonthPrev, Util.scale(10), String.valueOf(id));
			
			}
		
			if (Util.isInfoOn) {
				drawTimeLineInfo();
			}
			else {
				parent.pushStyle();
				parent.fill(Colors.DARKER_BLUE);
				parent.stroke(Colors.DARKER_BLUE);
				parent.strokeWeight(Util.scale(0.5f));
				parent.rect(Util.screenW/6 + Util.scale(30), Util.screenH/3 + Util.scale(10), Util.screenW *4/6 - Util.scale(60), Util.screenH/3 - Util.scale(20), Util.dataWindowRadius);
				parent.fill(Colors.WHITE);
				parent.textAlign(PConstants.CENTER, PConstants.BOTTOM);
				parent.textSize(Util.fontLarge);
				parent.text(Util.timelingTag, Util.screenW/2, Util.screenH/2);
				parent.textAlign(PConstants.CENTER, PConstants.TOP);
				parent.textSize(Util.fontRegular2);
				parent.text(Util.timelingTag2, Util.screenW/2, Util.screenH/2);
				parent.popStyle();
			}
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	
	public void setTimeLineInfo(float x, float y, float w, float h, ArrayList<Integer> id_list) {
		
		this.tl_x = x;
		this.tl_y = y;
		this.tl_w = w;
		this.tl_h = h;
		this.tl_idList = id_list;
		
	}
	
	public void drawTimeLineInfo() {
		
		parent.pushStyle();
		parent.fill(Colors.DARKERER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(tl_x, Util.screenH - Util.scale(27), tl_w, Util.scale(4));
		
		parent.beginShape();
			parent.vertex(tl_x, tl_y);
			parent.vertex(tl_x + tl_w, tl_y);
			parent.vertex(tl_x + tl_w, tl_y - Util.scale(20));
			parent.vertex(Util.screenW * 5/6 - Util.scale(30), tl_y - Util.scale(20));
			parent.vertex(Util.screenW * 5/6 - Util.scale(30), Util.scale(30));
			parent.vertex(Util.screenW /6 + Util.scale(30), Util.scale(30));
			parent.vertex(Util.screenW /6 + Util.scale(30), tl_y - Util.scale(20));
			parent.vertex(tl_x, tl_y - Util.scale(20));
			parent.vertex(tl_x, tl_y);
		parent.endShape();
		
		parent.popStyle();
		
		parent.pushStyle();
		parent.fill(Colors.DARKER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(Util.screenW / 6 + Util.scale(32), Util.scale(42), Util.screenW * 4 / 6 - Util.scale(64), Util.screenH - Util.scale(94), Util.dataWindowRadius);
		parent.popStyle();
		
		float tabX = Util.screenW / 6 + Util.scale(32);
		float tabY = Util.scale(32);
		float tabW = (Util.screenW * 4/6 - Util.scale(60))/3 - Util.scale(1.5f);
		float tabH = Util.scale(10);
		
		for (int i=0; i < tl_idList.size(); i++) {
			parent.pushStyle();
			if (Util.selectedInfoPane == i) {
				parent.fill(Colors.DARKER_BLUE);
				parent.stroke(Colors.DARKER_BLUE);
			}
			else {
				parent.fill(Colors.DARKERER_BLUE);
				parent.stroke(Colors.DARKER_BLUE);
			}
			parent.strokeWeight(Util.scale(0.5f));
			parent.rect(tabX + tabW*i, tabY, tabW, tabH, Util.dataWindowRadius);
			if (Util.selectedInfoPane == i) {
				parent.fill(Colors.transparentBlue);
			}
			else {
				parent.fill(Colors.DARKER_BLUE);
			}
			
			parent.textSize(Util.fontRegular2);
			parent.textAlign(PConstants.LEFT, PConstants.CENTER);
			parent.text(eventsDataHt.get(tl_idList.get(tl_idList.size() - i -1)).getDate(), tabX + tabW*i + Util.scale(2), tabY + tabH/2);
			parent.popStyle();
		}
		System.out.println("Selected : " + Util.selectedInfoPane + " : " + eventsDataHt.get(tl_idList.get(tl_idList.size() - Util.selectedInfoPane -1)).getName());
		
		int id;
		int dd;
		int mm;
		int yyyy;
		String date;
		String name;
		String description;
		String file;
		float lat;
		float lon;
		Hashtable<String, TypeNameIdPair> tempNameIdHt;
		Hashtable<String, TypeShapeColorPair> tempShapeColorHt;
		
		int index = tl_idList.get(tl_idList.size() - Util.selectedInfoPane - 1);
		
		id = this.eventsDataHt.get(index).getId();
		dd = this.eventsDataHt.get(index).getDd();
		mm = this.eventsDataHt.get(index).getMm();
		yyyy = this.eventsDataHt.get(index).getYyyy();
		date = this.eventsDataHt.get(index).getDate();
		name = this.eventsDataHt.get(index).getName();
		description = this.eventsDataHt.get(index).getDescription();
		file = this.eventsDataHt.get(index).getFile();
		lat = this.eventsDataHt.get(index).getLat();
		lon = this.eventsDataHt.get(index).getLon();
		tempNameIdHt = this.eventsDataHt.get(index).getNameIdHt();
		tempShapeColorHt = this.eventsDataHt.get(index).getHt();
		
		parent.pushStyle();
		parent.fill(Colors.gray);
		parent.textSize(Util.fontLarge);
		parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		parent.text(name, tabX + Util.scale(2), tabY + tabH + Util.scale(5));
		parent.stroke(Colors.gray);
		parent.line(tabX + Util.scale(2), tabY + tabH + Util.scale(10), tabX + Util.scale(387), tabY + tabH + Util.scale(10));
		parent.fill(Colors.transparentBlue);
		parent.textSize(Util.fontRegular2);
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.noStroke();
		parent.text(description, tabX + Util.scale(2), tabY + tabH + Util.scale(16), Util.scale(200), Util.screenH/2);
		PImage image = parent.loadImage(parent.sketchPath + "/data/images/" + id + ".jpg");
		parent.imageMode(PConstants.CENTER);
		image.resize((int)(Util.scale(80)), (int)Util.scale(80));
		parent.image(image,Util.screenW /2 + Util.screenW / 6, Util.screenH/2);
		parent.popStyle();
		
	}
	
	
	public void drawEventsMap() {
		try {
			int id;
			int dd;
			int mm;
			int yyyy;
			String date;
			String name;
			String description;
			String file;
			float lat;
			float lon;
			Hashtable<String, TypeNameIdPair> tempNameIdHt;
			Hashtable<String, TypeShapeColorPair> tempShapeColorHt;
			keyCounter = 1;
			id = this.eventsDataHt.get(keyCounter).getId();
			dd = this.eventsDataHt.get(keyCounter).getDd();
			mm = this.eventsDataHt.get(keyCounter).getMm();
			yyyy = this.eventsDataHt.get(keyCounter).getYyyy();
			date = this.eventsDataHt.get(keyCounter).getDate();
			name = this.eventsDataHt.get(keyCounter).getName();
			description = this.eventsDataHt.get(keyCounter).getDescription();
			file = this.eventsDataHt.get(keyCounter).getFile();
			lat = this.eventsDataHt.get(keyCounter).getLat();
			lon = this.eventsDataHt.get(keyCounter).getLon();
			tempNameIdHt = this.eventsDataHt.get(keyCounter).getNameIdHt();
			tempShapeColorHt = this.eventsDataHt.get(keyCounter).getHt();
	//		if (tempShapeColorHt.isEmpty())
	//			System.out.println("Empty");
			Enumeration<String> keys2 = tempShapeColorHt.keys();
			String key2;
			PShape tempShape;
			while(keys2.hasMoreElements()){
				key2 = (String)keys2.nextElement();
				tempShape = tempShapeColorHt.get(key2).getShape();
				int tempColor = tempShapeColorHt.get(key2).getColor();
				//tempShape = y.getChild(key2);
				tempShape.disableStyle();
				//
				parent.fill(tempColor);
				parent.shape(tempShape, Util.screenW/6, 0);
				System.out.println(key2);
			}
			
			if (keyCounter >= eventsDataHt.size()) {
				Util.isPlaying = Util.STOP;
				System.out.println("Stop");
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void drawFacts() {
		parent.fill(Colors.DARK_GRAY);
		parent.noStroke();
		parent.rect(Util.screenW * 5 / 6 + Util.scale(1), 0 + Util.scale(1), Util.screenW / 6 - Util.scale(2), Util.screenH - Util.scale(2), Util.scale(5));
		
		parent.fill(Colors.DARKERER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(Util.screenW * 5 / 6 + Util.scale(2), 0 + Util.scale(2), Util.screenW / 6 - Util.scale(4), Util.scale(12), Util.scale(5));
		
		parent.fill(Colors.LIGHT_GRAY);
		parent.textSize(Util.fontMedium);
		parent.textAlign(PConstants.CENTER, PConstants.CENTER);
		parent.text("Did You Know?", Util.screenW *5/6 + Util.screenW / 12, Util.scale(3) + Util.scale(6f));
		
		parent.fill(Colors.DARKERER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(Util.screenW * 5 / 6 + Util.scale(2), 0 + Util.scale(16), Util.screenW / 6 - Util.scale(4), Util.screenH - Util.scale(18.5f), Util.scale(5));
		
		parent.fill(Colors.WHITE);
		parent.textSize(Util.fontRegular2);
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.text(factsList.get(Util.factIndex), Util.screenW * 5 / 6 + Util.scale(7), Util.scale(20), Util.screenW / 6 - Util.scale(18), Util.screenH - Util.scale(17));
		
		bulletHole.resize((int)Util.scale(10), (int)Util.scale(10));
		parent.tint(Colors.transparentBlue);
		parent.image(bulletHole, Util.screenW * 5/6 + Util.screenW /12 + Util.scale(20), Util.screenH - Util.scale(22));
		parent.image(bulletHole, Util.screenW * 5/6 + Util.screenW /12 + Util.scale(45), Util.screenH - Util.scale(23));
		parent.image(bulletHole, Util.screenW * 5/6 + Util.screenW /12 + Util.scale(30), Util.screenH - Util.scale(20));
		parent.image(bulletHole, Util.screenW * 5/6 + Util.screenW /12 + Util.scale(40), Util.screenH - Util.scale(15));
	}
	
	
	public void drawAbout() {
		parent.fill(Colors.DARK_GRAY);
		parent.noStroke();
		parent.rect(0 + Util.scale(1), 0 + Util.scale(1), Util.screenW / 6 - Util.scale(2), Util.screenH - Util.scale(2), Util.scale(5));
		
		parent.fill(Colors.DARKERER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(0 + Util.scale(2), 0 + Util.scale(2), Util.screenW / 6 - Util.scale(4), Util.scale(18), Util.scale(5));
		
		parent.fill(Colors.LIGHT_GRAY);
		parent.textSize(Util.fontMedium);
		parent.textAlign(PConstants.CENTER, PConstants.CENTER);
		parent.text("I Can See Clearly Now:\nWorld War II",Util.screenW / 12, Util.scale(3) + Util.scale(9f));
		
		parent.fill(Colors.DARKERER_BLUE);
		parent.stroke(Colors.DARKER_BLUE);
		parent.strokeWeight(Util.scale(0.5f));
		parent.rect(0 + Util.scale(2), 0 + Util.scale(22), Util.screenW / 6 - Util.scale(4), Util.screenH - Util.scale(24.5f), Util.scale(5));
		
		parent.fill(Colors.WHITE);
		parent.textSize(Util.fontRegular2);
		parent.textAlign(PConstants.LEFT, PConstants.TOP);
		parent.text(Util.infoString[Util.infoStringIndex], Util.scale(9), Util.scale(28), Util.screenW / 6 - Util.scale(18), Util.screenH - Util.scale(20));
	
		bulletHole.resize((int)Util.scale(10), (int)Util.scale(10));
		parent.tint(Colors.transparentBlue);
		parent.image(bulletHole, Util.scale(5),  Util.scale(5));
	}
	
	@SuppressWarnings("static-access")
	public void draw() {
		if (Util.isMapOnTop) {
			parent.pushStyle();
			parent.noStroke();
			parent.fill(Colors.transparentBlue);
			parent.rect(Util.screenW/6 + Util.scale(1), 0 + Util.scale(1), Util.screenW*4/6 - Util.scale(2), Util.screenH - Util.scale(2), Util.scale(5));
			parent.stroke(Colors.DARK_GRAY);
			map.disableStyle();
			parent.shapeMode(parent.CORNER);
			parent.fill(Colors.WHITE);
			parent.shape(map, Util.screenW/6, 0);
			map.enableStyle();
			
			if (!Util.isMapAnimationOn) {
				drawOverViewMap();
			}
			else {
				//drawEventsMap();
				drawTimeline();
			}
			//drawFacts();
			/*
			x.disableStyle();
			parent.fill(Colors.RED);
			parent.shape(x, Util.screenW/6, 0);
			*/
			parent.popStyle();
		}
	}
	
	public void plotMapColor(Hashtable<String,TypeNameIdPair> ht) {
		this.ht = new Hashtable<String, TypeShapeColorPair>();
		if (!ht.isEmpty()) {
			Enumeration<String> keys;
			String key;
			String name;
			String side;
			String id;
			int color = 0;
			TypeNameIdPair tp;
			keys = ht.keys();
			while(keys.hasMoreElements()) {
				key = (String)keys.nextElement();
				tp = ht.get(key);
				name = tp.getName();
				side = tp.getSide();
				id = tp.getId();
				if (id.contains(",")) {
					String ids[] = id.split(",");
					for (int i=0; i<ids.length; i++) {
						id = ids[i];
						child = x.getChild(id);
						child.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
						child.enableStyle();
						if (side.compareTo(Util.ALLIES) == 0 && name.compareTo("Soviet Union") == 0)
							color = Colors.SOVIET;
						else if (side.compareTo(Util.ALLIES) == 0) 
							color = Colors.ALLIES;
						else if (side.compareTo(Util.AXIS) == 0)
							color = Colors.AXIS;
						else if (side.compareTo(Util.BELLIGERENTS) == 0)
							color = Colors.BELLIGERENTS;
						else if (side.compareTo(Util.NEUTRAL) == 0)
							color = Colors.NEUTRAL;
						this.ht.put(id, new TypeShapeColorPair(child, color, name));
					}
				}
				else {
					child = x.getChild(id);
					child.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
					child.enableStyle();
					if (side.compareTo(Util.ALLIES) == 0 && name.compareTo("Soviet Union") == 0)
						color = Colors.SOVIET;
					else if (side.compareTo(Util.ALLIES) == 0) 
						color = Colors.ALLIES;
					else if (side.compareTo(Util.AXIS) == 0)
						color = Colors.AXIS;
					else if (side.compareTo(Util.BELLIGERENTS) == 0)
						color = Colors.BELLIGERENTS;
					else if (side.compareTo(Util.NEUTRAL) == 0)
						color = Colors.NEUTRAL;
					this.ht.put(id, new TypeShapeColorPair(child, color, name));
				}
			}
		}
	}
	
	public void setEventsMap(Hashtable<Integer, TypeEventsData> ht) {
		if (!ht.isEmpty()) {
			Enumeration<Integer> keys;
			int key;
			
			keys = ht.keys();
			while(keys.hasMoreElements()) {
				key = (int)keys.nextElement();
				int id = ht.get(key).getId();
				int dd = ht.get(key).getDd();
				int mm = ht.get(key).getMm();
				int yyyy = ht.get(key).getYyyy();
				String date = ht.get(key).getDate();
				String name = ht.get(key).getName();
				String description = ht.get(key).getDescription();
				String file = ht.get(key).getFile();
				float lat = ht.get(key).getLat();
				float lon = ht.get(key).getLon();
				Hashtable<String, TypeShapeColorPair> tempShapeColorPairHt = new Hashtable<String, TypeShapeColorPair>();
				Hashtable<String, TypeNameIdPair> tempNameIdHt = ht.get(key).getNameIdHt();
				
				Enumeration<String> keys2 = tempNameIdHt.keys();
				String key2;
				while(keys2.hasMoreElements()) {
					key2 = (String)keys2.nextElement();
					String pathId = tempNameIdHt.get(key2).getId();
					String name2 = tempNameIdHt.get(key2).getName();
					String side = tempNameIdHt.get(key2).getSide();
					int color = 0;
					child = y.getChild(pathId);
					child.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
					child.enableStyle();
					if (side.compareTo(Util.ALLIES) == 0 && name.compareTo("Soviet Union") == 0)
						color = Colors.SOVIET;
					else if (side.compareTo(Util.ALLIES) == 0) 
						color = Colors.ALLIES;
					else if (side.compareTo(Util.AXIS) == 0)
						color = Colors.AXIS;
					else if (side.compareTo(Util.BELLIGERENTS) == 0)
						color = Colors.BELLIGERENTS;
					else if (side.compareTo(Util.NEUTRAL) == 0)
						color = Colors.NEUTRAL;
					tempShapeColorPairHt.put(key2, new TypeShapeColorPair(child, color, name2));
				}
				this.eventsDataHt.put(key, new TypeEventsData(id, dd, mm, yyyy, date, name, description, file, lat, lon, tempShapeColorPairHt, tempNameIdHt));
			}
		}
	}
	
	public void loadBulletImage(String file) {
		this.bulletHole = parent.loadImage(file);
	}
	
	public void setFactsList(ArrayList<String> factsList) {
		this.factsList = factsList;
	}
	
	public void resetKeyCounter() {
		this.keyCounter = 0;
	}
	
	public int getKeyCounter() {
		return this.keyCounter;
	}
	
	public void incrementKeyCounter() {
		this.keyCounter++;
	}
	
	public boolean isInInfoPane(float mx, float my) {
		return ((mx >= Util.scale(2) && mx <= Util.screenW / 6 - Util.scale(2) && my >= Util.scale(22) && my <= Util.screenH - Util.scale(2f))) ? true : false;
	}
	
	public boolean changeInfo(float mx, float my, float currentX, float currentY) {
		
		return false;
	}
	
	public boolean isInInfoPaneOnMap(float mx, float my) {
		return (mx >= Util.screenW/6 + Util.scale(30) && mx <= Util.screenW *5/6 - Util.scale(30) && my >= Util.scale(30) && my <= Util.screenH - Util.scale(50)) ? true : false;
	}
	
	public void initializeTimeLine() {
		tl_x = Util.screenW/6 + Util.scale(30);
		tl_y = Util.scale(30);
		tl_w = Util.screenW *4/6 - Util.scale(60);
		tl_h = Util.screenH - Util.scale(80);
	}
}
