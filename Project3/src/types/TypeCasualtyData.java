/**
 * 
 */
package types;

/**
 * @author giric
 *
 */
public class TypeCasualtyData {
	private String countryName;
	private float totalCasualties;
	private float civilianCasualties;
	private float militaryCasualties;
	private float holocaustCasualties;
	
	
	/**
	 * @param countryName
	 * @param totalCasualties
	 * @param civilianCasualties
	 * @param militaryCasualties
	 * @param holocaustCasualties
	 */
	public TypeCasualtyData(String countryName, float totalCasualties,
			float civilianCasualties, float militaryCasualties,
			float holocaustCasualties) {
		this.countryName = countryName;
		this.totalCasualties = totalCasualties;
		this.civilianCasualties = civilianCasualties;
		this.militaryCasualties = militaryCasualties;
		this.holocaustCasualties = holocaustCasualties;
	}
	/**
	 * @return the countryName
	 */
	public String getCountryName() {
		return countryName;
	}
	/**
	 * @param countryName the countryName to set
	 */
	public void setCountryName(String countryName) {
		this.countryName = countryName;
	}
	/**
	 * @return the totalCasualties
	 */
	public float getTotalCasualties() {
		return totalCasualties;
	}
	/**
	 * @param totalCasualties the totalCasualties to set
	 */
	public void setTotalCasualties(float totalCasualties) {
		this.totalCasualties = totalCasualties;
	}
	/**
	 * @return the civilianCasualties
	 */
	public float getCivilianCasualties() {
		return civilianCasualties;
	}
	/**
	 * @param civilianCasualties the civilianCasualties to set
	 */
	public void setCivilianCasualties(float civilianCasualties) {
		this.civilianCasualties = civilianCasualties;
	}
	/**
	 * @return the militaryCasualties
	 */
	public float getMilitaryCasualties() {
		return militaryCasualties;
	}
	/**
	 * @param militaryCasualties the militaryCasualties to set
	 */
	public void setMilitaryCasualties(float militaryCasualties) {
		this.militaryCasualties = militaryCasualties;
	}
	/**
	 * @return the holocaustCasualties
	 */
	public float getHolocaustCasualties() {
		return holocaustCasualties;
	}
	/**
	 * @param holocaustCasualties the holocaustCasualties to set
	 */
	public void setHolocaustCasualties(float holocaustCasualties) {
		this.holocaustCasualties = holocaustCasualties;
	}
	
	
}
