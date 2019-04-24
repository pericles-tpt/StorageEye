from classes import InitDirectory, BuildDirectory, PrintDirectory, File
from classes import PrintDirectory
from os import walk
from os.path import join, getsize
from platform import system
import sys

write = open("dirlog_original.txt", "a+")

if __name__ == "__main__":
    path = "/"
    rootDirectory = BuildDirectory(path).build_directory_template(path)
    printd = PrintDirectory(write)
    printd.txt(rootDirectory)
    
