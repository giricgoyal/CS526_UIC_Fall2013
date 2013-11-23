/**
 * 
 */
package main;

import java.util.ArrayList;
import java.util.Hashtable;

import processing.core.PApplet;
import types.TypeCasualtyData;
import utils.Colors;
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
	private ArrayList<DataPlot> allPiCharts;
	
	public boolean isMoving;
	
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
		allPiCharts = new ArrayList<DataPlot>();
		
		allData = new DataPlot(this.parent, this.x, this.y, this.w, this.h);
		allPlots.add(allData);
		
		holocaustData = new DataPlot(parent, this.x, this.y, this.w, this.h);
		allPlots.add(holocaustData);
		
		for (String s : Util.buttonCountries) {
			DataPlot tempData = new DataPlot(parent, this.x, this.y, this.w/4.5f, this.h/3);
			tempData.setPiChart(true);
			tempData.setDataName(s);
			allPiCharts.add(tempData);
		}
		
		System.out.println("Data Setup Done");
	}
	
	public void setCasualtyData(Hashtable<String, TypeCasualtyData> casualtyData) {
		allData.setData(casualtyData);
		allData.setDataName("all Data");
		holocaustData.setData(casualtyData);
		holocaustData.setDataName("holocaust");
		for (DataPlot dp : allPiCharts) {
			dp.setData(casualtyData);
		}
	}
	
	public void draw() {
		if (Util.isDataOn) {
			for (DataPlot d : allPlots) {
				if (d.isVisible) {
					d.draw();
				}
			}
			for (DataPlot dp : allPiCharts) {
				if (dp.isVisible) {
					dp.draw();
				}
			}
		}
	}
	
	public void drawRemoveBox() {
		if (this.isMoving) {
			this.parent.pushStyle();
			this.parent.noFill();
			this.parent.stroke(Colors.RED);
			this.parent.strokeWeight(Util.scale(3));
			this.parent.rect(0,0,Util.screenW, Util.screenH);
			this.parent.popStyle();
		}
	}
	
	public void setVisible(boolean val, String str) {
		if (str.compareToIgnoreCase("allData") == 0) {
			if (!allData.isVisible) {
				allData.isVisible = val;
				allData.myX = Util.scale(10);
				allData.myY = Util.scale(10);
				Util.onScreenData++;
				System.out.println("On screen objects : " + Util.onScreenData);
			}
		}
		if (str.compareToIgnoreCase("holocaust") == 0) {
			if (!holocaustData.isVisible) {
				holocaustData.isVisible = val;
				holocaustData.myX = Util.scale(450);
				holocaustData.myY = Util.scale(10);
				Util.onScreenData++;
				System.out.println("On screen objects : " + Util.onScreenData);
			}
		}
		if (str.compareToIgnoreCase("") == 0) {
			allData.isVisible = val;
			holocaustData.isVisible = val;
			for (DataPlot d: allPiCharts) {
				d.isVisible = val;
			}
			if (!val){
				Util.onScreenData = 0;
				System.out.println("On screen objects : " + Util.onScreenData);
			}
		}
		for (DataPlot s : allPiCharts) {
			if (str.compareToIgnoreCase(s.getDataName()) == 0) {
				if (!s.isVisible) {
					s.isVisible = val;
					s.myX = parent.random(Util.screenW * 2 / 6, Util.screenW * 4 / 6);
					s.myY = parent.random(0, Util.screenH * 2 / 3);
					Util.onScreenData++;
					System.out.println("On screen objects : " + Util.onScreenData);
					break;
				}
			}
		}
	}
	
	public boolean isInWindow(float posX, float posY, float currentX, float currentY) {
		if (allData.isInRectangle(posX, posY)) {
			//boolean val = allData.moveOutline(posX, posY, currentX, currentY);
			boolean val = allData.moveWindow(posX, posY, currentX, currentY);
			drawRemoveBox();
			allData.drawOutline();
			this.isMoving = val;
			return true;
		}
		if (holocaustData.isInRectangle(posX, posY)) {
			//boolean val = holocaustData.moveOutline(posX, posY, currentX, currentY);
			boolean val = holocaustData.moveWindow(posX, posY, currentX, currentY);
			drawRemoveBox();
			holocaustData.drawOutline();
			this.isMoving = val;
			return true;
		}
		for (DataPlot dp : allPiCharts) {
			if (dp.isInRectangle(posX, posY)) {
				//boolean val = holocaustData.moveOutline(posX, posY, currentX, currentY);
				boolean val = dp.moveWindow(posX, posY, currentX, currentY);
				drawRemoveBox();
				dp.drawOutline();
				this.isMoving = val;
				return true;
			}
		}
		return false;
	}
	
	public boolean moveData() {
		if (allData.isOutlineMoved()) {
			allData.setWindowatOutline();
			this.isMoving = false;
			return true;
		}
		
		if (holocaustData.isOutlineMoved()) {
			holocaustData.setWindowatOutline();
			this.isMoving = false;
			return true;
		}
		for (DataPlot dp: allPiCharts) {
			if (dp.isOutlineMoved()) {
				dp.setWindowatOutline();
				this.isMoving = false;
				return true;
			}
		}
		return false;
	}
}
