from os import walk
from os.path import join, getsize
from classes import Directory, File
import sys

def build_directory(directoryName):
    directory = Directory(directoryName)

    for (dirpath, childdirs, filenames) in walk(directory.name): 

        for filename in filenames:
            directory.files.append(File(filename, getsize(join(dirpath, filename))))
            directory.size += filename.size
        for childdir in childdirs:
            directory.children.append(build_directory(join(dirpath, childdir)))
            directory.size += childdir.size
        break
    return directory

def print_directory(directory, depth=0):
    whitespace = 4*' '

    print("{}{}\n".format(depth*whitespace, directory.name))

    for file in directory.files:
        print("{}{}\n".format((depth+1)*whitespace, file.name))
    for child in directory.children:
        print_directory(child, depth+1)


if __name__ == "__main__":
    path = ""
    rootDirectory = build_directory(path)
    print_directory(rootDirectory)


    
