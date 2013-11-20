package types;

/**
 * 
 * @author giric
 *
 */

public class TypeTouch {
	float xPos;
	float yPos;
	float xWidth;
	float yWidth;
	int ID;
	 
	public TypeTouch( int id, float x, float y, float w, float h ){
		ID = id;
		xPos = x;
		yPos = y;
		xWidth = w;
		yWidth = h;
	}
}
