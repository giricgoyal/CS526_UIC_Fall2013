/**
 * 
 */
package types;

/**
 * @author giric
 *
 */
public class TypeNameIdPair {
	String name;
	String id;
	String side;
	
	TypeNameIdPair(){
		name = null;
		id = null;
		side = null;
	}
	
	/**
	 * @param name
	 * @param id
	 * @param side
	 */
	public TypeNameIdPair(String name, String id, String side) {
		this.name = name;
		this.id = id;
		this.side = side;
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

	/**
	 * @return the id
	 */
	public String getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(String id) {
		this.id = id;
	}

	/**
	 * @return the side
	 */
	public String getSide() {
		return side;
	}

	/**
	 * @param side the side to set
	 */
	public void setSide(String side) {
		this.side = side;
	}
}
