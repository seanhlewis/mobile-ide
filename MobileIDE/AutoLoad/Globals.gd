extends Node

var enter = 0

var debug = false

var execute = false

var keyboard = false
var settings = false
var Sanim = 0.0

static func hello():
	var exec
	exec = !exec
	#print(exec)

static func save(content):
	var file = File.new()
	file.open("user://save_game.dat", File.WRITE)
	file.store_string(content)
	file.close()

func load():
	var file = File.new()
	file.open("user://save_game.dat", File.READ)
	var content = file.get_as_text()
	file.close()
	return content


enum CheckCode{
	NOT_CHECKED, 
	UNKNOWN_OPERAND, 
	WRONG_PLACE, 
	CORRECT, 
}
