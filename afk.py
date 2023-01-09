from concurrent.futures import thread
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import threading
import time

#Create a keyboard object
keyboardx = KeyboardController()
#Create a mouse object
mouse = MouseController()

hatchLoc = (892, 446)
hatchLocOutsideClick = (845, 393)
elite1 = (1010, 305)
elite2 = (968, 355)
elite3 = (960, 404)
elite4 = (959, 460)
champ = (983, 507)

#Gym/E4 Locations
BossButtons = [(968, 355),(960, 404),(959, 460),(983, 507),(983, 560),(892, 446)]


delay = 0.3
clickSpeed = 0.1

#Print hotkeys for each function
print("` = Start\n] = AFK\nTab = Stop\nEsc = Quit")

def clicker():
    while running:
        mouse.click(Button.left, 1)
        time.sleep(clickSpeed)

def fillHatch():
	time.sleep(delay)
	mouse.position = hatchLocOutsideClick
	keyboardx.press("h")
	time.sleep(delay)
	for x in range(90):
		mouse.click(Button.left, 1)
		time.sleep(clickSpeed)
	
def afkClick():
	count = 0
	option = input("1 = E4(1)\n2 = E4(2)\n3 = E4(3)\n4 = E4(4)\n5 = E4 Champ\n6 = Regular AFK\n")
	option = option.replace("]","")
	option = int(option) - 1
	click = BossButtons[option]
	time.sleep(1)
	while running:
		#(count = 600 = 1 minute)
		mouse.position = click
		while count < 4000:
			mouse.click(Button.left, 1)
			time.sleep(clickSpeed)
			count+=1
		fillHatch()
		count = 0

def on_press (key):
	#Global variable to keep track of running state
	global running
	#Find which key was pressed to use according function
	#Set running to 'true', create a thread for the function, then start the thread

	if key == KeyCode.from_char('`'):
		running = True
		a = threading.Thread(target=clicker)
		a.start()
		
	if key == KeyCode.from_char(']'):
		running = True
		b = threading.Thread(target=afkClick)
		b.start()

	if key == Key.tab:
		running = False

	if key == Key.esc:
		quit()

#Creates the listener to be able to stop when needed
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()