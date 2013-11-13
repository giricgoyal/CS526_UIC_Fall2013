/**
 * 
 */
package types;

import processing.core.PShape;

/**
 * @author giric
 *
 */
public class TypeShapeColorPair {
	PShape shape;
	int color;
	String name;
	
	TypeShapeColorPair() {
		shape = new PShape();
		color = 0x00000000f;
		name = "";
	}
	
	public TypeShapeColorPair(PShape shape, int color, String name) {
		this.shape = shape;
		this.color = color;
		this.name = name;
	}

	/**
	 * @return the shape
	 */
	public PShape getShape() {
		return shape;
	}

	/**
	 * @param shape the shape to set
	 */
	public void setShape(PShape shape) {
		this.shape = shape;
	}

	/**
	 * @return the color
	 */
	public int getColor() {
		return color;
	}

	/**
	 * @param color the color to set
	 */
	public void setColor(int color) {
		this.color = color;
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	
}
