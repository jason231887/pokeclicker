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

clickSpeed = 0.1

#Print hotkeys for each function
print("` = Start\nTab = Stop")

def clicker():
    while running:
        mouse.click(Button.left, 1)
        time.sleep(clickSpeed)

def on_press (key):
	#Global variable to keep track of running state
	global running
	#Find which key was pressed to use according function
	#Set running to 'true', create a thread for the function, then start the thread

	if key == KeyCode.from_char('`'):
		running = True
		a = threading.Thread(target=clicker)
		a.start()

	if key == Key.tab:
		running = False

#Creates the listener to be able to stop when needed
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()