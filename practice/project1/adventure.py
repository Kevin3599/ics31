import json

'''
Allows the user to navigate around a (text based) world.
Data comes from adventure.json
'''
START = 'Aldrich Park'
FINISH = "3015"

def main():
	data = json.load(open('adventure.json'))
	play_game(data)

def move_user(data, current, move):
	'''
	data is the whole nested data structure loaded from the JSON file
	current is the current room name (string)
	move is the move( strings)
	function returns the name of the next room (string)
	'''
	# TODO: your code here
	pass

def describe(data, current):
	'''
	data is the whole nested data structure loaded from the JSON file
	current is the current room name (string)
	function returns the string to be printed
	'''
	# TODO: your code here
	pass

def play_game(data):
	print('Welcome to the ICS 31 Adventure Game:\n')
	# TODO: your code here
	print(data)


if __name__ == '__main__':
	main()