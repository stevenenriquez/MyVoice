# Import necessary libraries to make the magic happen
import os
import time
import functions


# What file are we looking for that contains our commands?
#file_dir = "C:/Users/Steven/Desktop/Commands/command.txt"
file_dir = "C:/Users/Steven/Dropbox/MyVoice/command.txt"


# GLOBAL CONSTANTS
COMMAND = 0		# What are we doing? (opening an application most likely)
CONTENT = 1		# What application are we applying the initial command to? (Skype)


def main():

	while True:

		try:
			file = open(file_dir, 'r')		# Open the file for reading


			# split any commands by line/split the two components of each command
			command_list = [line.strip().split(" ") for line in file]

			print(command_list)

			for instruction_tuple in command_list:
				functions.handle_decision(instruction_tuple)
				time.sleep(.5)


			# closing/deleting file
			closeListener(file)

		# Handle the case in which the .txt file was not created
		except FileNotFoundError:
			pass

		# Handle the case in which an invalid command was used in the .txt file  
		except IOError as e:
			print(e)

		# Catch all incase any other problems arose 
		except Exception as e:
			print(e)
			closeListener(file)

			for file in os.listdir("C:/Users/Steven/Dropbox/MyVoice/"):
				try:
					os.remove("C:/Users/Steven/Dropbox/MyVoice/" + file)
				except:
					pass


# Helper function to delete a .txt file that contains commands 
def closeListener(file):
	time.sleep(.1)
	file.close()
	os.remove(file_dir)


# Run the application 
main()

