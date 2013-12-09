# ------------------------------------------------------------------------------------------
# imports
from math import *
from euclid import *
from omega import *
from cyclops import *
from util import *
from wandaid import *
from system import *
from cameraManager import *


# -----------------------------------------------------------------------------------------
# variables

env = None


# ---------------------------------------------------------------------------------------
# methods
def initSound():
	global env
	env = getSoundEnvironment()
	env.setAssetDirectory('gg_p2')
	
	bkSound = SoundInstance(env.loadSoundFromFile('bkSound','backGround.wav'))
	bkSound.play()
	bkSound.setVolume(25)
	bkSound.setLoop(True)
