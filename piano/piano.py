__author__ = 'naveen'

import os 
from curtsies import Input
#	   sa	   re	   ga	   ma	   pa	 dha	ni	sa
notes = [523.25, 587.33, 659.26, 698.46, 783.99, 880, 987.77, 1046.5]

def beeping(freq, duration):
	os.system("beep -f {} -l {}".format(str(freq), str(duration)))

def pianos(stry):
	if stry== "u'a'":
		beeping(notes[0], 100)	
	elif stry=="u's'":	
		beeping(notes[1], 100)
	elif stry=="u'd'":	
		beeping(notes[2], 100)
	elif stry=="u'f'":	
		beeping(notes[3], 100)
	elif stry=="u'g'":	
		beeping(notes[4], 100)
	elif stry=="u'h'":	
		beeping(notes[5], 100)
	elif stry=="u'j'":	
		beeping(notes[6], 100)
	elif stry=="u'k'":	
		beeping(notes[7], 100)
	else:
		return ;	

def detectkey():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			pianos(repr(e))

if __name__ == '__main__':
	detectkey()
		
