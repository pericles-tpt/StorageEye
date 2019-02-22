import sys
sys.path.append("/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/hurry/filesize/__init__.py")
from os.path import join, getsize
from main import build_directory
from hurry.filesize import size, si

dirpath = sys.path[0]
# exceptionDirectoryName = os.environ['HOME'] Getting user directory which goes 3 layers deep as opposed to 2

# Need a dirlog_old and a dirlog_new
dirlog_old = open("dirlog_old.txt", "a+")
dirlog_new = open("dirlog_new.txt", "a+")
properties = open("properties.txt", "a+")

name_dirlog_old = "dirlog_old.txt"
name_dirlog_new = "dirlog_new.txt"
name_properties = "properties.txt"

# Gets relevant user information for directory scan
if getsize(join(dirpath, name_dirlog_old)) == 0:
	
	# Finding out what drive the user wants to run the program on
	drive_letter = '0'

	while (not(drive_letter >= 'A' and drive_letter <= 'Z') or not(drive_letter >= 'a' and drive_letter <= 'z')):
		print("Which drive (please input drive letter) do you want to monitor space on?")
		drive_letter = input()

	if (drive_letter > 90):
		drive_letter  -= 32

	directoryName = drive_letter + ":\\" 

	# Finding out how much space the user wants to monitor on the drive
	print("How much space (in gigabtytes) do you want to reserve?")
	threshold = int(input())
	print >> properties, "threshold: " + str(threshold)

# Determines how deep a directory is within the drive (i.e. +1 for every \ in the directory)
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

		for child in childdirs:
			size_bytes = getsize(directoryName + '\\' + child)
			print >> directory_old, directoryName + '\\' + child + '|' + size_bytes
			log_DirectoryOld(directoryName)

#def log_DirectoryNew(directoryName, exceptionDirectoryName):

