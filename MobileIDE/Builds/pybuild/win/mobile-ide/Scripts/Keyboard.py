from godot import exposed, export
from godot import *

from io import StringIO
from contextlib import redirect_stdout


Globals = ResourceLoader.load("res://Autoload/Globals.gd")

@exposed
class Keyboard(Node):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
	def _on_MENU_pressed(self):
		print("Python Menu Pressed!")
		#f = open("myfile.txt", "w")
		#f.write(str(exec(str(self.get_node("../TextEdit").text))))
		#f.close()
		
		f = StringIO()
		with redirect_stdout(f):
			try:
				exec(str(self.get_node("../TextEdit").text))
				s = f.getvalue()
			except:
				s = "Code Failed"
		print("111", s)
		out = self.get_node("../ColorRect/VBoxContainer/Output")
		out.text = s
		#Globals.call("save")
		#exec(str(self.get_node("../TextEdit").text))
		
