from os import walk
from os.path import join, getsize
from classes import Directory, File
import sys

def build_Directory(directoryName):
    directory = Directory(directoryName)

    for (dirpath, childdirs, filenames) in walk(directory.name): 

        for filename in filenames:
            directory.files.append(File(filename, getsize(join(dirpath, filename))))

        for childdir in childdirs:
            directory.children.append(build_Directory(join(dirpath, childdir)))

        break
    
    return directory

if __name__ == "__main__":
    path = ""
    rootDirectory = build_Directory(path)



    