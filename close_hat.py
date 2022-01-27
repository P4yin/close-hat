from os import system
from keyboard import is_pressed
from time import sleep
# im not sure if this lowers memory usage but I think it does

if __name__ == '__main__':
	letter = 'a' # if they dont use regular letters, it will try to delete something that doesnt exist 
	_special_keys = ['enter', 'escape', 'tab', 'space', 'alt', 'ctrl',
	'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']  # you can add more keys if you want

	keys = set()  # we use a set because it doesn't allow for duplicate members
	# this also lowers the amount of values in our set in case the user types in long strings
	with open('keys.txt', 'r') as f:  # we don't want to hardcode keys so we let them put their own in
		for word in f:  # we go both line by line getting all the 
			temp = word.strip()  # we don't want white space to do anything bad
			if temp.lower() in _special_keys:  # check if they use one of the special keys
				keys.add(temp.lower())
			else:
				for letter in temp:  # letter by letter
					keys.add(letter)  # add to set
	del _special_keys, word, temp, letter, f  # might save some memory, might not
	# we do not use any of the variables again, so we might as well clear them from memory
	# THIS IS ONLY DONE FOR GAME PERFORMANCE REASONS

	print('Ready To Close Hat\n')  # we have loaded all the wanted characters into a set
	while True:
		for i in keys:
			if is_pressed(i):  # they pressed the key
				print('Closing Hat because you pressed ' + i)
				system("TASKKILL /F /IM HatinTimeGame.exe") # some funny thing to close the game
				# also sends default error message if it can't close it or something
				sleep(5)  # don't want them to try it a lot in a row, shouldnt change much