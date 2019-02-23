from os import walk, lstat
from os.path import join, getsize, lexists
from classes import Directory, File
from platform import system
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
            directory.size += getsize(directory.name + '/' + filename)

        for childdir in childdirs:

            directory.size += getsize(directory.name + '/' + childdir)
            if system() == "Darwin":
                if (childdir != 'Volumes' and childdir != 'EFIROOTDIR' and childdir != 'bin' and childdir != 'sbin' and childdir != 'System' and childdir != 'Library' and childdir != 'usr'): #Without these last 4 exceptions for folders to scan it take up to an hour to scan only 90GB of files on an SSD
                    try:
                        directory.children.append(build_directory(join(dirpath, childdir)))
                        directory.size += getsize(childdir)
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
                directory.size += getsize(childdir)

        break

    return directory

def print_directory(directory, depth=0):
    whitespace = 4*' ' 

    print("{}{}\n".format(depth*whitespace, directory.name))

    for file in directory.files:
        print("{}{}\n".format((depth+1)*whitespace, file.name))
    for child in directory.children:
        print_directory(child, depth+1)

dirlog_original = open("dirlog_original.txt", "a+")

def print_directory_file(directory, depth=0):

    print(("{}{}|{}\n".format(str(depth), directory.name, str(directory.size))), file=dirlog_original)

    for file in directory.files:
        print(str(depth) + file.name + '|' + str(file.size), file=dirlog_original)
    for child in directory.children:
        print_directory_file(child, depth+1)

if __name__ == "__main__":
    path = ""
    rootDirectory = build_directory(path)
    print_directory(rootDirectory)
    
