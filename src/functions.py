import pyautogui
import time
import subprocess
# from appjar import gui
# from coordinates import *
from multiprocessing import Process

SCREEN_SIZE_X_VALUE = 0
SCREEN_SIZE_Y_VALUE = 1

# The top left of the screen 
X_TOP_LEFT = 0
Y_TOP_LEFT = 0

COMMAND = 0		# What are we doing? (opening an application most likely)
CONTENT = 1		# What application are we applying the initial command to? (Skype)

# What is the screen resolution we are working with?
SCREEN_SIZE_TUPLE = screen_size_tuple = pyautogui.size()


# Helper function to perform the initial setup of the application
def perform_initial_application_setup(application):
	open(application)
	maximize_application()
	center_mouse_on_screen()
	pyautogui.press('esc')



# Helper function to open the application specified by the user 
def open(application):
	pyautogui.press('win')
	pyautogui.typewrite(application)
	pyautogui.press('enter')


# Helper function to maximize the application to take up the full screen
def maximize_application():
	pyautogui.keyDown('win')
	pyautogui.press('up')
	pyautogui.keyUp('win')


# Helper function to move the mouse to the center of a user's screen 
def center_mouse_on_screen():
	# Divide the x, and y pair we get my 2 to get the center of the screen 
	x_center_location = SCREEN_SIZE_TUPLE[SCREEN_SIZE_X_VALUE] / 2
	y_center_location= SCREEN_SIZE_TUPLE[SCREEN_SIZE_Y_VALUE] / 2

	print(x_center_location, y_center_location)

	# Move the mouse to the center of the screen 
	pyautogui.moveTo(x_center_location, y_center_location)




# Helper function to assist in executing further commands 
def handle_decision(instruction_tuple):

	# extract the information of value 
	command = instruction_tuple[COMMAND].strip()
	content = instruction_tuple[CONTENT].strip()


	if command == "open":
		print("IN OPEN BLOCK")
		perform_initial_application_setup(content)
		return

	# TODO: Conditional statements to handle each command
	if command == "click":
		print("IN CLICK BLOCK")
		if content == "contacts_tab":
			click_contacts_tab()
		return

	if command == "search":
		click_search_bar()
		search_for_person(content)
		right_click_person()
		call_person()
		return


	else:
		print("IN THE ELSE BLOCK")
		return


# Helper function to click on the contacts tab within skype 
def click_contacts_tab():
	# Setup the region of the screen to search

	# We want to search the 33% in the x and y direction based on the screen resolution
	x_end_value = .33 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_X_VALUE]
	y_end_value = .33 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_Y_VALUE]

	# Don't do anyything if the program isnt fully loaded
	while pyautogui.locateCenterOnScreen('screenshots/setting_dots.png', region=(X_TOP_LEFT, Y_TOP_LEFT, x_end_value, y_end_value)) is None:
		continue

	# The location of the contact tab will be found via a search of the region we specified 
	contact_tab_x, contact_tab_y = pyautogui.locateCenterOnScreen('screenshots/unselected_contact_tab.png', region=(X_TOP_LEFT, Y_TOP_LEFT, x_end_value, y_end_value))
	print(contact_tab_x, contact_tab_y)
	pyautogui.moveTo(contact_tab_x, contact_tab_y, .5)
	pyautogui.click()
	return


# Helper function for locating search bar 
def click_search_bar():
	# We want to search the 33% in the x and y direction based on the screen resolution
	x_end_value = .33 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_X_VALUE]
	y_end_value = .33 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_Y_VALUE]

	# The location of the contact tab will be found via a search of the region we specified 
	search_glass_x, search_glass_y = pyautogui.locateCenterOnScreen('screenshots/search_glass.png', region=(X_TOP_LEFT, Y_TOP_LEFT, x_end_value, y_end_value))
	print(search_glass_x, search_glass_y)
	pyautogui.moveTo(search_glass_x, search_glass_y, .5)
	pyautogui.click()
	time.sleep(.5)
	return


# Helper function to search for individual
def search_for_person(person):
	pyautogui.typewrite(person)
	return

# Helper function for right clicking on a person we have searched
def right_click_person():

	x_end_value = .2 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_X_VALUE]
	y_end_value = .5 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_Y_VALUE]

	people_tag_x, people_tag_y = pyautogui.locateCenterOnScreen('screenshots/people_tag.png', region=(X_TOP_LEFT, Y_TOP_LEFT, x_end_value, y_end_value))
	pyautogui.moveTo(people_tag_x, people_tag_y - 35, .5)
	pyautogui.click(button='right')
	time.sleep(.5)
	return

def call_person():

	x_end_value = .2 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_X_VALUE]
	y_end_value = .5 * SCREEN_SIZE_TUPLE[SCREEN_SIZE_Y_VALUE]

	view_profile_x, view_profile_y = pyautogui.locateCenterOnScreen('screenshots/view_profile.png', region=(X_TOP_LEFT, Y_TOP_LEFT, x_end_value, y_end_value))
	pyautogui.moveTo(view_profile_x, view_profile_y, .4)
	pyautogui.doubleClick()
	time.sleep(.5)
	start_call_x, start_call_y = pyautogui.locateCenterOnScreen('screenshots/start_call.png')
	pyautogui.moveTo(start_call_x, start_call_y, .4)
	pyautogui.click()
	return