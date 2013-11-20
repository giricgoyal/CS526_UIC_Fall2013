package utils;

/**
 * 
 * @author giric
 *
 */
public class Colors {
	public static int black = 0xFF101010;
	public static int dark;
	public static int medium = 0xFF2E2E2E;
	public static int light = 0xFFDDDDDD;	
	public static int white = 0xFFEEEEEE;
	public static int gray = 0xFFE5D8BD;
	
	public static int transparentWhite = 0x99bbbbbb;
	public static int transparentGray = 0x99777777;
	public static int transparentBlack = 0x99101010;
	public static int transparentBlue = 0x99e3f2ff;
	public static int transparent = 0x10111111;
	
	public static int helpColor = 0xa01e1e1d;
	
	public static int gridColor = 0x88FB8072;
	
	public static int filterColor = 0xFF987E18;
	
	public static int windowBackground = 0xff1f1f1f;//0xFF202020; 
	
	public static int grey = 0xFF999999;
	
	public static int tweetColor = 0xFFE3F8FF;
	public static int tweetColor2 = 0xFFD2E7EE;
	public static int buttonColor = 0xff9d9d9c; //0xff65B6F3;
	public static int buttonSelectedColor = 0xffededec; //0xffbd9d6c; //0xffEBBD61;
	public static int button_red = 0xfebb3232;
	public static int button_blue = 0xfe222299;
	public static int button_green = 0xfe225522;
	public static int button_quit = 0xfe424242;
	public static int button_background = 0xffd2d2d2;
	
	public static int buttonBorder = 0xff1d1d1c;
	public static int buttonSelectedBorder = 0xff1d1d1c;
	
	public static int weatherPanel = 0x80111111;
	
	public static int map1;
	public static int map2;
	public static int map3;
	public static int map4;	
	public static int map5;
	public static int map6;
	public static int map7;
	
	// joysword
	public static int NETHERLAND = 0xffff6600;
	public static int BLIZZARD = 0xff01b2f1;
	public static int PEACH = 0xffdf59ae;
	
	
	// colors from p3g2, thanks
	public static int DARK_GRAY = 0xff3f3f3f;
	public static int MEDIUM_GRAY = 0xff767676;
	public static int LIGHT_GRAY = 0xffa8a8a6;
	public static int TEXT_GRAY = 0xff757575;
	public static int BLACK = 0xdd000000;
	public static int DARK_ORANGE = 0xffCD6519;
	public static int DARKER_ORANGE = 0xff854210;
	public static int DARKERER_ORANGE = 0xff62300C;
	public static int DARK_BROWN = 0xff453108;
	public static int DARK_BLUE = 0xdd3B6DC2;
	public static int DARKER_BLUE = 0xdd2a4e8b;
	public static int DARKERER_BLUE = 0xdd1D3660;
	public static int LIGHT_BLUE = 0xdd65B6F3;
	public static int LIGHT_GREEN = 0xdd52923C;
	public static int DARK_GREEN = 0xdd52bb3c;
	public static int LIGHT_ORANGE = 0xffEBBD61;
	public static int WHITE = 0xddf7f7f7;
	public static int DARK_WHITE = 0xff999999;
	public static int RED = 0xddd14C41;
	public static int DARK_RED = 0xdd9b4c41;
	public static int DARKER_RED = 0xddaa4c41;
	public static int BACKGROUND_COLOR = 0xff1f1f1f;
	public static int GRAPH_COLOR_1 = 0xff8da940;
	public static int GRAPH_COLOR_2 = 0x8fadb0b0;
	public static int GRAPH_COLOR_3 = 0xfff16451;
	public static int GRAPH_COLOR_4 = 0xff4fc1bb;
	public static int[] GRAPH_COLORS = {0x88ED1F1F, 0x881F97ED, 0x882BD937, 0x88FCFC14, 0x88FFFFFF, 0x88D500ED, 0x88FFA024};
	
	public static int ALLIES = LIGHT_BLUE;
	public static int ALLIES_BORDER = DARK_BLUE;
	public static int AXIS = RED;
	public static int AXIS_BORDER = DARK_RED;
	public static int SOVIET = LIGHT_GREEN;
	public static int SOVIET_BORDER = DARK_GREEN;
	public static int BELLIGERENTS = LIGHT_ORANGE;
	public static int BELLIGERENTS_BORDER = DARK_ORANGE;
	public static int NEUTRAL = LIGHT_GRAY;
	public static int NEUTRAL_BORDER = 0xff999999;
	
	public static int getColor(String side) {
		if (side.compareTo(Util.ALLIES) == 0) 
			return ALLIES;
		else if (side.compareTo(Util.AXIS) == 0)
			return AXIS;
		else if (side.compareTo(Util.SOVIET) == 0)
			return SOVIET;
		else if (side.compareTo(Util.NEUTRAL) == 0)
			return NEUTRAL;
		else if (side.compareTo(Util.BELLIGERENTS) == 0)
			return BELLIGERENTS;
		return 0;
	}
	
	public static int TOTAL = WHITE;
	public static int TOTAL_DARK = LIGHT_GRAY;
	public static int CIVILIAN = 0xff3B6DC2;
	public static int CIVILIAN_DARK = 0xff2a4e8b;
	public static int MILITARY = 0xff9b4c41;
	public static int MILITARY_DARK = 0xffaa4c41;
	public static int HOLOCAUST = RED;
	public static int HOLOCAUST_DARK = DARK_RED;
	
}
