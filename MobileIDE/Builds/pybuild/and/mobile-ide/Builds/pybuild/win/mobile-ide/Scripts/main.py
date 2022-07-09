from godot import exposed, export
from godot import *

Globals = ResourceLoader.load("res://Autoload/Globals.gd")

@exposed
class main(Node):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		print("Python is ready!")
		Globals.call("hello")
		#print(Globals.get("execute"))
		#if Globals.execute:
		#	print(Globals.execute)
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
