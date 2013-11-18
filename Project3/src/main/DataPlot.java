/**
 * 
 */
package main;

import java.util.Enumeration;
import java.util.Hashtable;

import processing.core.PApplet;
import processing.core.PConstants;
import processing.core.PVector;
import types.TypeCasualtyData;
import utils.Colors;
import utils.Util;

/**
 * @author giric
 *
 */
public class DataPlot extends BasicControl {
	
	public  boolean isVisible;
	private Hashtable<String, TypeCasualtyData> casualtyData;
	private PVector dis;
	private String dataName;
	
	private float dataWinX, dataWinY;
	private float dataWinW, dataWinH;
	
	public DataPlot(PApplet parent, float x, float y, float width, float height) {
		super(parent, x, y, width, height);
		// TODO Auto-generated constructor stub
		isVisible = false;
		casualtyData = new Hashtable<String, TypeCasualtyData>();
		dis = new PVector(0,0);
		dataName = "";
		dataWinX = x;
		dataWinY = y;
		dataWinW = width;
		dataWinH = height;
	}

	public void drawAllCasualties() {
		dataWinW = myWidth - Util.scale(47);
		dataWinH = myHeight - Util.scale(15);
		dataWinX = myX + Util.scale(44);
		dataWinY = myY + Util.scale(12);
		
		this.parent.stroke(Colors.dark);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.fill(Colors.dark);
		this.parent.rect(dataWinX, dataWinY, dataWinW, dataWinH, Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontMedium);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Casualties (x1000)", myX + Util.scale(3), myY + Util.scale(5));
		
		this.parent.fill(Colors.TOTAL);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.stroke(Colors.TOTAL_DARK);
		this.parent.rect(myX + myWidth/2 - Util.scale(12), myY + Util.scale(3), Util.scale(5), Util.scale(5), Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontRegular);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Total", myX + myWidth/2 - Util.scale(5), myY + Util.scale(6));
		
		this.parent.fill(Colors.CIVILIAN);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.stroke(Colors.CIVILIAN_DARK);
		this.parent.rect(myX + myWidth/2 + Util.scale(12), myY + Util.scale(3), Util.scale(5), Util.scale(5), Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontRegular);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Civilian", myX + myWidth/2 + Util.scale(20), myY + Util.scale(6));
		
		this.parent.fill(Colors.MILITARY);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.stroke(Colors.MILITARY_DARK);
		this.parent.rect(myX + myWidth/2 + Util.scale(42), myY + Util.scale(3), Util.scale(5), Util.scale(5), Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontRegular);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Military", myX + myWidth/2 + Util.scale(50), myY + Util.scale(6));
		
		
		Enumeration<String> keys = casualtyData.keys();
		String key;
		float delta_y = (float)dataWinH / (float)(casualtyData.size());
		float y = dataWinY;
		while(keys.hasMoreElements()) {
			key = (String)keys.nextElement();
			String name = casualtyData.get(key).getCountryName();
			float total = casualtyData.get(key).getTotalCasualties();
			float military = casualtyData.get(key).getMilitaryCasualties();
			float civilian = casualtyData.get(key).getCivilianCasualties();
			
			float x_total = PApplet.map(total, 0f, 25000f, 0, dataWinW);
			float x_civilian = PApplet.map(civilian, 0f, 25000f, 0, dataWinW);
			float x_military = PApplet.map(military, 0f, 25000f, 0f, dataWinW);
			
			this.parent.fill(Colors.white);
			this.parent.textAlign(PConstants.RIGHT, PConstants.CENTER);
			this.parent.textSize(Util.fontRegular);
			this.parent.text(name, dataWinX - Util.scale(2), y + Util.scale(3f));
			

			this.parent.fill(Colors.BACKGROUND_COLOR);
			this.parent.stroke(Colors.BACKGROUND_COLOR);
			this.parent.strokeWeight(Util.scale(0.5f));
			this.parent.rect(dataWinX, y + Util.scale(1.5f), dataWinW, Util.scale(3));
			
			
			this.parent.fill(Colors.TOTAL);
			this.parent.stroke(Colors.TOTAL);
			this.parent.strokeWeight(Util.scale(0.5f));
			this.parent.rect(dataWinX, y + Util.scale(1.5f), x_total, Util.scale(3));
			
			if (x_civilian < x_military) {
				this.parent.fill(Colors.MILITARY);
				this.parent.stroke(Colors.MILITARY);
				this.parent.strokeWeight(Util.scale(0.5f));
				this.parent.rect(dataWinX, y + Util.scale(1.5f), x_military, Util.scale(3));
				
				this.parent.fill(Colors.CIVILIAN);
				this.parent.stroke(Colors.CIVILIAN);
				this.parent.strokeWeight(Util.scale(0.5f));
				this.parent.rect(dataWinX, y + Util.scale(1.5f), x_civilian, Util.scale(3));
			}
			else {
				this.parent.fill(Colors.CIVILIAN);
				this.parent.stroke(Colors.CIVILIAN);
				this.parent.strokeWeight(Util.scale(0.5f));
				this.parent.rect(dataWinX, y + Util.scale(1.5f), x_civilian, Util.scale(3));
				
				this.parent.fill(Colors.MILITARY);
				this.parent.stroke(Colors.MILITARY);
				this.parent.strokeWeight(Util.scale(0.5f));
				this.parent.rect(dataWinX, y + Util.scale(1.5f), x_military, Util.scale(3));
			}
			y = y + delta_y;
		}
	}
	
	public void drawHolocaustData() {
		dataWinW = myWidth - Util.scale(47);
		dataWinH = myHeight - Util.scale(15);
		dataWinX = myX + Util.scale(44);
		dataWinY = myY + Util.scale(12);
		
		this.parent.stroke(Colors.dark);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.fill(Colors.dark);
		this.parent.rect(dataWinX, dataWinY, dataWinW, dataWinH, Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontMedium);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Victims of Holocaust (x1000)", myX + Util.scale(3), myY + Util.scale(5));
		
		this.parent.fill(Colors.HOLOCAUST);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.stroke(Colors.HOLOCAUST_DARK);
		this.parent.rect(myX + myWidth/2 + Util.scale(25), myY + Util.scale(3), Util.scale(5), Util.scale(5), Util.dataWindowRadius);
		
		this.parent.fill(Colors.gray);
		this.parent.textSize(Util.fontRegular);
		this.parent.textAlign(PConstants.LEFT, PConstants.CENTER);
		this.parent.text("Jews", myX + myWidth/2 + Util.scale(35), myY + Util.scale(6));
		
		Enumeration<String> keys = casualtyData.keys();
		String key;
		float delta_y = (float)dataWinH / (float)(casualtyData.size());
		float y = dataWinY;
		while(keys.hasMoreElements()) {
			key = (String)keys.nextElement();
			String name = casualtyData.get(key).getCountryName();
			float holocaust = casualtyData.get(key).getHolocaustCasualties();
			
			float x_total = PApplet.map(holocaust, 0f, 3500f, 0, dataWinW);
			
			this.parent.fill(Colors.white);
			this.parent.textAlign(PConstants.RIGHT, PConstants.CENTER);
			this.parent.textSize(Util.fontRegular);
			this.parent.text(name, dataWinX - Util.scale(2), y + Util.scale(3f));
			

			this.parent.fill(Colors.BACKGROUND_COLOR);
			this.parent.stroke(Colors.BACKGROUND_COLOR);
			this.parent.strokeWeight(Util.scale(0.5f));
			this.parent.rect(dataWinX, y + Util.scale(1.5f), dataWinW, Util.scale(3));
			
			
			this.parent.fill(Colors.HOLOCAUST);
			this.parent.stroke(Colors.HOLOCAUST);
			this.parent.strokeWeight(Util.scale(0.5f));
			this.parent.rect(dataWinX, y + Util.scale(1.5f), x_total, Util.scale(3));
			
			y = y + delta_y;
		}
	}
	
	
	@Override
	public void draw() {
		// TODO Auto-generated method stub
		this.parent.pushStyle();
		this.parent.stroke(Colors.light);
		this.parent.strokeWeight(Util.scale(0.5f));
		this.parent.fill(Colors.medium);
		this.parent.rect(myX, myY, myWidth, myHeight, Util.dataWindowRadius);
		
		
		if (dataName.compareToIgnoreCase("all data") == 0) {
			drawAllCasualties();
		}
		
		if (dataName.compareToIgnoreCase("holocaust") == 0) {
			drawHolocaustData();
		}
		
		this.parent.popStyle();
	}
	
	public void setData(Hashtable<String, TypeCasualtyData> casualtyData) {
		this.casualtyData = casualtyData;
	}
	

	public boolean isInRectangle(float posX,float posY){
		return (myX<posX && posX<myX+myWidth && myY<posY && posY<myY+myHeight) ? true: false;
	}
	
	public boolean moveWindow(float posX, float posY, float currentX, float currentY) {
		if (this.isVisible) {
			dis.x = posX - currentX;
			dis.y = posY - currentY;
			myX += dis.x;
			myY += dis.y;
			float centerX = myX + myWidth/2;
			float centerY = myY + myHeight/2;
			if (centerX < 0 || centerX > Util.screenW || centerY < 0 || centerY > Util.screenH) {
				this.isVisible = false;
				return false;
			}
			return true;
		}
		return false;
	}
	
	public void setDataName(String dataName) {
		this.dataName = dataName;
	}
}
