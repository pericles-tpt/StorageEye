from os import walk
from os.path import join, getsize
from classes import Directory, File
import sys

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