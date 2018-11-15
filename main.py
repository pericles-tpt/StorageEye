import sys #Can get rid of this later
from os import walk
from os.path import join, getsize
from classes import Directory, File
import sys

# Need a dirlog_old and a dirlog_new
dirlog_old = open("dirlog_old.txt", "a+");
dirlog_new = open("dirlog_new.txt", "a+");
properties = open("properties.txt", "a+");

name_dirlog_old = "dirlog_old.txt"
name_dirlog_new = "dirlog_new.txt"
name_properties = "properties.txt"


dirpath = sys.path[0]

def build_Directory(directoryName):
    directory = Directory(directoryName)

    for (dirpath, childdirs, filenames) in walk(directory.name): 

        for file in filenames:
            directory.files.append(File(file, getsize(join(dirpath, file))))
        directory.files.extend(filenames)

        for child in childdirs:
            directory.children.append(build_Directory(join(directory.name, child)))

        break
    
    return directory

if __name__ == "__main__":
    path = ""
    rootDirectory = build_Directory(path)

if getsize(join(dirpath, name_dirlog_old)) == 0:
    print("How much space (in gigabtytes) do you want to reserve?")
    threshold = input()
    print >> properties, "threshold: " + str(threshold)