/**
 * 
 */
package main;

import java.util.ArrayList;
import java.util.Hashtable;

import processing.core.PApplet;
import types.TypeCasualtyData;
import utils.Util;

/**
 * @author giric
 *
 */
public class Data {
	private PApplet parent;
	private float x, y;
	private float w, h;
	
	private DataPlot allData;
	private DataPlot holocaustData;
	
	private ArrayList<DataPlot> allPlots;
	
	/**
	 * @param parent
	 * @param x
	 * @param y
	 * @param w
	 * @param h
	 */
	public Data(PApplet parent, float x, float y, float w, float h) {
		this.parent = parent;
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		
		allPlots = new ArrayList<DataPlot>();
		
		allData = new DataPlot(this.parent, this.x, this.y, this.w, this.h);
		allPlots.add(allData);
		
		holocaustData = new DataPlot(parent, this.x, this.y, this.w, this.h);
		allPlots.add(holocaustData);
		
		System.out.println("Data Setup Done");
	}
	
	public void setCasualtyData(Hashtable<String, TypeCasualtyData> casualtyData) {
		allData.setData(casualtyData);
		allData.setDataName("all Data");
		holocaustData.setData(casualtyData);
		holocaustData.setDataName("holocaust");
	}
	
	public void draw() {
		if (Util.isDataOn) {
			for (DataPlot d : allPlots) {
				if (d.isVisible) {
					d.draw();
				}
			}
		}
	}
	
	public void setVisible(boolean val, String str) {
		if (str.compareToIgnoreCase("allData") == 0) {
			allData.isVisible = true;
			allData.myX = Util.scale(10);
			allData.myY = Util.scale(10);
		}
		if (str.compareToIgnoreCase("holocaust") == 0) {
			holocaustData.isVisible = true;
			holocaustData.myX = Util.scale(10);
			holocaustData.myY = Util.scale(10);
		}
	}
	
	public void isInWindow(float posX, float posY, float currentX, float currentY) {
		if (allData.isInRectangle(posX, posY)) {
			allData.moveWindow(posX, posY, currentX, currentY);
		}
		if (holocaustData.isInRectangle(posX, posY)) {
			holocaustData.moveWindow(posX, posY, currentX, currentY);
		}
	}
}
