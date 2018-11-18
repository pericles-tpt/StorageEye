from os import walk
from os.path import join, getsize
from classes import Directory, File
import sys

def build_directory(directoryName):
    directory = Directory(directoryName)

    for (dirpath, childdirs, filenames) in walk(directory.name): 

        for filename in filenames:\
            newfile = File(filename, getsize(join(dirpath, filename)))
            directory.files.append(newfile)
            directory.size += newfile.size
        for childdir in childdirs:
            newdir = build_directory(join(dirpath, childdir))
            directory.children.append(newdir)
            directory.size += newdir.size
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


    
