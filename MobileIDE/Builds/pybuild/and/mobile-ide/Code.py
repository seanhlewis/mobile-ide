from godot import exposed, export
from godot import *


@exposed
class Code(TextEdit):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	
	rcode = export(str, default='print("hello world!)')
	
	def outputstr(self):
		rcode = "print('hello world!')"
		return exec(rcode)
		
	def _ready(self):
		rcode = "print('hello world!')"
		#output = exec(rcode)
		#self.text = "hello"
		#print(str(output))
		#print("111")
		#print(self.outputstr())
		#print("222")
		#exec'ing the code to the Godot cosole, but it needs to be written to a string...
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		#print(output, "lol")
		pass
		
	

	#def _process(self, delta):
		# ball will move normally for both players
		# even if it's sightly out of sync between them
		# so each player sees the motion as smooth and not jerky
	#	pass
