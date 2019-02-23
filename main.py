from os import walk, lstat
from os.path import join, getsize, lexists
from classes import Directory, File
from platform import system
import log
import sys

dirpath = sys.path[0]

""" NOTE: Below "filename.size" and "childdir.size" are commented out to prevent
error messages as they are being interpreted as "filename" and "chilldir" are 
being interpreted as strings... Are they supposted to be part of a class or
somethign with their own attributes like size? """

def build_directory(directoryName):
    directory = Directory(directoryName)

    for (dirpath, childdirs, filenames) in walk(directory.name): 

        for filename in filenames:

            directory.files.append(File(filename, getsize(join(dirpath, filename))))
            directory.size += 0 #filename.size 

        for childdir in childdirs:

            if system() == "Darwin":
                if (childdir != 'Volumes' and childdir != 'EFIROOTDIR' and childdir != 'bin' and childdir != 'sbin' and childdir != 'System' and childdir != 'Library' and childdir != 'usr'):
                    try:
                        directory.children.append(build_directory(join(dirpath, childdir)))
                        directory.size += 0 #childdir.size
                        #print(directory.name)
                    except PermissionError: 
                        pass
                    except FileNotFoundError: 
                        pass
                    except OSError: 
                        pass
                else:
                    pass
                        
            else:
                directory.children.append(build_directory(join(dirpath, childdir)))
                directory.size += 0 #childdir.sizes

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
    
