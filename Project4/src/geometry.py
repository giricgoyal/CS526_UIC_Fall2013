# Use lines and spheres to create a disc.
from math import *
from euclid import *
from omega import *
from cyclops import *

class geometry:
	_radius = 0.0
	_centerX = 0.0
	_centerY = 0.0
	_color = '#000000CC'
	_shape = 'circle'
	_scale = 1
	_ObjShape = None

	def __init__(self, _radius, _centerX, _centerY, _color, _shape):
		self._radius = _radius
		self._centerX = _centerX
		self._centerY = _centerY
		self._color = _color
		self._shape = _shape
		self._scale = 1
		self._ObjShape = CylinderShape.create(1, self._radius, self._radius, 10, 128)

	def draw(self):
		if self._shape == 'circle':
			self._drawCircle();
	
	def _setColor(self):
		if self._ObjShape != None:
			self._ObjShape.setEffect('colored -e ' + self._color)

	def _setTransparent(self, val):
		if self._ObjShape != None:
			self._ObjShape.getMaterial().setTransparent(val)

	def _setScale(self, val):
		if self._ObjShape != None:
			self._ObjShape.setScale(Vector3(val, val, 0.1))
		 
	def _setPosition(self, vector3):
		print "Setting pos"
		if self._ObjShape != None:
			self._ObjShape.setPosition(vector3)
		else:
			print "Null object"

	def _drawCircle(self):
		self._setColor()
		self._setTransparent(True)
		self._setScale(1)
		self._setPosition(Vector3(0,0,0))



