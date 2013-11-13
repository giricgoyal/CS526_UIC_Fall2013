/**
 * 
 */
package main;

import java.util.Enumeration;
import java.util.Hashtable;

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
	PShape map;
	PApplet parent;
	PShape x;
	PShape child;
	Hashtable<String,TypeShapeColorPair> ht;
	Hashtable<String,TypeShapeColorPair> allChildren;
	
	public Map(PApplet p, String file) {
		this.parent = p;
		map = this.parent.loadShape(file);
		x = this.parent.loadShape(file);
		map.scale(Util.scale(0.55f/2f), Util.scale(0.35f/2f));
		//x = map.getChild("path4123");
		//x.scale(0.55f, 0.35f);
		ht = new Hashtable<String, TypeShapeColorPair>();
		
	}
	
	@SuppressWarnings("static-access")
	public void draw() {
		
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
		
		if (!this.ht.isEmpty()) {
			Enumeration keys;
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
			parent.textAlign(parent.LEFT, parent.TOP);
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
			parent.textAlign(parent.LEFT, parent.TOP);
			parent.textFont(Util.font);
			parent.textSize(Util.fontRegular);
			parent.fill(Colors.TEXT_GRAY);
			parent.text(Util.ALLIES, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + Util.scale(4));
			
			parent.strokeWeight(Util.scale(0.5f));
			parent.stroke(Colors.AXIS_BORDER);
			parent.fill(Colors.AXIS);
			parent.rect(Util.legendX + Util.scale(2), Util.legendY + Util.scale(2) + Util.legendH/5, Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
			parent.noStroke();
			parent.textAlign(parent.LEFT, parent.TOP);
			parent.textFont(Util.font);
			parent.textSize(Util.fontRegular);
			parent.fill(Colors.TEXT_GRAY);
			parent.text(Util.AXIS, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + Util.scale(3) + Util.legendH/5);
			
			parent.strokeWeight(Util.scale(0.5f));
			parent.stroke(Colors.SOVIET_BORDER);
			parent.fill(Colors.SOVIET);
			parent.rect(Util.legendX + Util.scale(2), Util.legendY + (2*Util.legendH/5) + Util.scale(1), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
			parent.noStroke();
			parent.textAlign(parent.LEFT, parent.TOP);
			parent.textFont(Util.font);
			parent.textSize(Util.fontRegular);
			parent.fill(Colors.TEXT_GRAY);
			parent.text(Util.SOVIET, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (2*Util.legendH/5) + Util.scale(2));
			
			parent.strokeWeight(Util.scale(0.5f));
			parent.stroke(Colors.BELLIGERENTS_BORDER);
			parent.fill(Colors.BELLIGERENTS);
			parent.rect(Util.legendX + Util.scale(2), Util.legendY + (3 * Util.legendH/5), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
			parent.noStroke();
			parent.textAlign(parent.LEFT, parent.TOP);
			parent.textFont(Util.font);
			parent.textSize(Util.fontRegular);
			parent.fill(Colors.TEXT_GRAY);
			parent.text(Util.BELLIGERENTS, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (3 * Util.legendH/5) + Util.scale(1));
			
			parent.strokeWeight(Util.scale(0.5f));
			parent.stroke(Colors.NEUTRAL_BORDER);
			parent.fill(Colors.NEUTRAL);
			parent.rect(Util.legendX + Util.scale(2), Util.legendY + (4 * Util.legendH/5) - Util.scale(1), Util.legendH/5-Util.scale(3), Util.legendH/5-Util.scale(3), Util.scale(0.5f));
			parent.noStroke();
			parent.textAlign(parent.LEFT, parent.TOP);
			parent.textFont(Util.font);
			parent.textSize(Util.fontRegular);
			parent.fill(Colors.TEXT_GRAY);
			parent.text(Util.NEUTRAL, Util.legendX + Util.legendH/5 + Util.scale(1), Util.legendY + (4 * Util.legendH/5));
			
			
			parent.stroke(Colors.DARK_GRAY);
		}
		/*
		x.disableStyle();
		parent.fill(Colors.RED);
		parent.shape(x, Util.screenW/6, 0);
		*/
		parent.popStyle();	
	}
	
	public void plotMapColor(Hashtable<String,TypeNameIdPair> ht) {
		this.ht = new Hashtable<String, TypeShapeColorPair>();
		if (!ht.isEmpty()) {
			Enumeration keys;
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
}
