import sys
from os import listdir, walk
from main import build_directory, print_directory
from os.path import join, getsize, isdir
from classes import Directory, File
from platform import system

dirpath = sys.path[0]
disks = []
OS = system() # Darwin = Mac, Linux = Linux, Windows = Windows


# Need a dirlog_old and a dirlog_new
dirlog_old = open("dirlog_old.txt", "a+")
dirlog_new = open("dirlog_new.txt", "a+")
properties = open("properties.txt", "a+")

name_dirlog_old = "dirlog_old.txt"
name_dirlog_new = "dirlog_new.txt"
name_properties = "properties.txt"

#Determines how deep a directory is within the drive (i.e. +1 for every \ in the directory)
def depth_Directory(directoryName):
    i = 0
    depth = 0
    while (directoryName[i] != '\0'):

        if directoryName[i] == '\'':

            depth+=1
            i+=1

        else:
            i+=1

    return depth

# Writes directory information to the dirlog_old.txt file when dirlog_new.txt doesn't exist 
def log_DirectoryOld(directoryName):
	
	build_Directory(directoryName)

	while (depth <= 2):
		depth = depth_directory(directoryName)
		for file in filenames: 
			size_bytes = getsize(directoryName + '\\' + file)
			print >> directory_old, directoryName + '\\' + file + '|' + size_bytes

		for childdir in childdirs:
			size_bytes = getsize(directoryName + '\\' + child)
			print >> directory_old, directoryName + '\\' + child + '|' + size_bytes
			log_DirectoryOld(directoryName)

#def log_DirectoryNew(directoryName, exceptionDirectoryName): - TEMPORARILY DISABLED TO COMPILE
def print_selection(OS):

	i = 0
	# Anthony you'll have to test this on your computer
	if "Windows" in OS: 
		print("I'm Windows")
		dl = char('A')
		while (dl <= 90):
			if (isdir(dl + ':\\') == 1):
				print(dl + ':\\')
				dl += 1
			elif (isdir(dl + ':\\') == 0):
				dl += 1

	if "Darwin" in OS: #It's a Mac
		disks = listdir("/Volumes")
		for names in disks:
			print(disks[i])
			i += 1

	# Will deal with Linux case later seems to be a bit of a pain...	
	"""if "Linux" in OS:
	directory = Directory(/Volumes)
	for child in childdirs:
		print()"""

selected = ""
def uinput_drive():

	print("Which drive do you want to monitor space on?\n")
	print_selection(OS)
	print("")
	selected = input()
	print('drive: ' + str(selected), file=properties)
	return selected

def uinput_space():	
	print("How much space (in gigabtytes) do you want to reserve?\n")
	threshold = input()
	print('threshold: ' + str(threshold), file=properties)
	return threshold

# Gets relevant user information for directory scan
if getsize(join(dirpath, name_dirlog_old)) == 0:
	
	drive = uinput_drive()

	""" BELOW: Must run a check for a user drive with a space in it, if a 
	space exists inserts the combination of chars that denote a space on Mac """

	spaced = False
	for i in range(len(drive)):
		if drive[i] == " ":
			space_pos = i
			spaced = True

	if spaced == True:
		new_drive = drive[:i] + "\ " + drive[i:] + "/"

	""" ABOVE: This fix for Mac shouldn't affect Windows since Windows uses a 
	single drive letter so there are no spaces anyway. Also this fix only works
	for drives with one space in them because I was too lazy to make it work for
	drives which have more than one space in them. What sort of madman would name 
	a drive with more than one space anyway?"""

	size = uinput_space()

	if "Darwin" in OS:
		new_log = build_directory("/Volumes/" + drive)
		print_directory(new_log)

	if "Windows" in OS:
		new_log = build_directory(drive)
		print_directory(new_log)


