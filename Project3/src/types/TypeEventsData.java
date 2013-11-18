/**
 * 
 */
package types;

import java.util.Hashtable;

import utils.Util;

/**
 * @author giric
 *
 */
public class TypeEventsData {
	private int id;
	private int dd;
	private int mm;
	private int yyyy;
	private String date;
	private String name;
	private String description;
	private String file;
	private float lat;
	private float lon;
	private Hashtable<String, TypeNameIdPair> nameIdHt;
	private Hashtable<String, TypeShapeColorPair> ht;
	
	public TypeEventsData() {
		this.id = 0;
		this.dd = 0;
		this.mm = 0;
		this.yyyy = 0;
		this.date = "";
		this.name = "";
		this.description = "";
		this.file = "";
		this.lat = Util.INVALID_LATLON;
		this.lon = Util.INVALID_LATLON;
		this.ht = null;
		this.nameIdHt = null;
		
	}
	/**
	 * @param id
	 * @param dd
	 * @param mm
	 * @param yyyy
	 * @param date
	 * @param name
	 * @param description
	 * @param file
	 * @param lat
	 * @param lon
	 * @param ht
	 * @param nameIdHt
	 */
	public TypeEventsData(int id, int dd, int mm, int yyyy, String date,
			String name, String description, String file, float lat, float lon,
			Hashtable<String, TypeShapeColorPair> ht, Hashtable<String, TypeNameIdPair> nameIdHt) {
		this.id = id;
		this.dd = dd;
		this.mm = mm;
		this.yyyy = yyyy;
		this.date = date;
		this.name = name;
		this.description = description;
		this.file = file;
		this.lat = lat;
		this.lon = lon;
		this.ht = ht;
		this.nameIdHt = nameIdHt;
	}
	/**
	 * @return the id
	 */
	public int getId() {
		return id;
	}
	/**
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}
	/**
	 * @return the dd
	 */
	public int getDd() {
		return dd;
	}
	/**
	 * @param dd the dd to set
	 */
	public void setDd(int dd) {
		this.dd = dd;
	}
	/**
	 * @return the mm
	 */
	public int getMm() {
		return mm;
	}
	/**
	 * @param mm the mm to set
	 */
	public void setMm(int mm) {
		this.mm = mm;
	}
	/**
	 * @return the yyyy
	 */
	public int getYyyy() {
		return yyyy;
	}
	/**
	 * @param yyyy the yyyy to set
	 */
	public void setYyyy(int yyyy) {
		this.yyyy = yyyy;
	}
	/**
	 * @return the date
	 */
	public String getDate() {
		return date;
	}
	/**
	 * @param date the date to set
	 */
	public void setDate(String date) {
		this.date = date;
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
	 * @return the description
	 */
	public String getDescription() {
		return description;
	}
	/**
	 * @param description the description to set
	 */
	public void setDescription(String description) {
		this.description = description;
	}
	/**
	 * @return the file
	 */
	public String getFile() {
		return file;
	}
	/**
	 * @param file the file to set
	 */
	public void setFile(String file) {
		this.file = file;
	}
	/**
	 * @return the lat
	 */
	public float getLat() {
		return lat;
	}
	/**
	 * @param lat the lat to set
	 */
	public void setLat(float lat) {
		this.lat = lat;
	}
	/**
	 * @return the lon
	 */
	public float getLon() {
		return lon;
	}
	/**
	 * @param lon the lon to set
	 */
	public void setLon(float lon) {
		this.lon = lon;
	}
	/**
	 * @return the ht
	 */
	public Hashtable<String, TypeShapeColorPair> getHt() {
		return ht;
	}
	/**
	 * @param ht the ht to set
	 */
	public void setHt(Hashtable<String, TypeShapeColorPair> ht) {
		this.ht = ht;
	}
	/**
	 * @return the nameIdHt
	 */
	public Hashtable<String, TypeNameIdPair> getNameIdHt() {
		return nameIdHt;
	}
	/**
	 * @param nameIdHt the nameIdHt to set
	 */
	public void setNameIdHt(Hashtable<String, TypeNameIdPair> nameIdHt) {
		this.nameIdHt = nameIdHt;
	}
}
