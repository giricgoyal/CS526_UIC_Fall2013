/**
 * 
 */
package main;

import java.util.Enumeration;
import java.util.Hashtable;

import types.TypeEventsData;
import types.TypeNameIdPair;
import types.TypeShapeColorPair;
import utils.Colors;
import utils.Util;
import processing.core.PApplet;
import processing.core.PConstants;
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
	private Hashtable<String,TypeShapeColorPair> ht;
	//private Hashtable<String,TypeShapeColorPair> allChildren;
	private Hashtable<String, TypeEventsData> eventsDataHt;
	
	public Map(PApplet p, String file) {
		this.parent = p;
		map = this.parent.loadShape(file);
		x = this.parent.loadShape(file);
		y = this.parent.loadShape(file);
		map.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
		//x = map.getChild("path4123");
		//x.scale(0.55f, 0.35f);
		ht = new Hashtable<String, TypeShapeColorPair>();
		eventsDataHt = new Hashtable<String, TypeEventsData>();
		
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
			parent.shape(tempShape, Util.screenW/6, 0);
		}
		
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
	
	
	public void drawEventsMap() {
		Enumeration<String> keys = this.eventsDataHt.keys();
		String key;
		
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
		
		while(keys.hasMoreElements()) {
			key = (String)keys.nextElement();
			
			id = this.eventsDataHt.get("15 March 1938").getId();
			dd = this.eventsDataHt.get("15 March 1938").getDd();
			mm = this.eventsDataHt.get("15 March 1938").getMm();
			yyyy = this.eventsDataHt.get("15 March 1938").getYyyy();
			date = this.eventsDataHt.get("15 March 1938").getDate();
			name = this.eventsDataHt.get("15 March 1938").getName();
			description = this.eventsDataHt.get("15 March 1938").getDescription();
			file = this.eventsDataHt.get("15 March 1938").getFile();
			lat = this.eventsDataHt.get("15 March 1938").getLat();
			lon = this.eventsDataHt.get("15 March 1938").getLon();
			tempNameIdHt = this.eventsDataHt.get("15 March 1938").getNameIdHt();
			tempShapeColorHt = this.eventsDataHt.get("15 March 1938").getHt();
			//if (tempShapeColorHt.isEmpty())
			//	System.out.println("Empty");
			Enumeration<String> keys2 = tempShapeColorHt.keys();
			String key2;
			while(keys2.hasMoreElements()){
				key2 = (String)keys2.nextElement();
				PShape tempShape = tempShapeColorHt.get(key2).getShape();
				//System.out.println(tempShape);
				int tempColor = tempShapeColorHt.get(key2).getColor();
				tempShape.disableStyle();
				parent.fill(tempColor);
				parent.shape(tempShape, Util.screenW/6, 0);
				//System.out.println(tempColor);
			}
			break;
		}
	}
	
	@SuppressWarnings("static-access")
	public void draw() {
		if (Util.isMapOnTop) {
			parent.pushStyle();
			parent.noStroke();
			parent.fill(Colors.transparentBlue);
			parent.rect(Util.screenW/6 + Util.scale(2), 0 + Util.scale(2), Util.screenW*4/6 - Util.scale(4), Util.screenH - Util.scale(4), Util.scale(5));
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
				drawEventsMap();
			}
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
	
	public void setEventsMap(Hashtable<String, TypeEventsData> ht) {
		if (!ht.isEmpty()) {
			Enumeration<String> keys;
			String key;
			
			keys = ht.keys();
			while(keys.hasMoreElements()) {
				key = (String)keys.nextElement();
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
					PShape child = y.getChild(pathId);
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
}
