from os import walk, lstat
from os.path import join, getsize, lexists
from platform import system
import sys


class InitDirectory:
    def __init__(self, directoryName):
        self._name = directoryName
        self.children = []
        self.files = []
        self._size = 0

    # Attribute encapsulation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size


class BuildDirectory:
    def __init__(self, directoryName):
        self._name = directoryName

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def build_directory_OS_exceptions(self, directory, childdir, dirpath):
        # Mac
        # PROBLEM: Folders have to be excluded from scan to stop scan taking upwards of 30 minutes
        # FIX: Figure out how deep a scan of these folders needs to be (if they need to be scanned at all)
        # to get useful information for the user and form there do a scan to a certain depth of the folders
        cd_except_mac = ['Volumes', 'EFIROOTDIR', 'bin', 'sbin', 'System', 'Library', 'usr']

        if system() == "Darwin":

            cd_except_chosen = cd_except_mac

        else:

            cd_except_chosen = []

        if childdir not in cd_except_chosen: 

            try:
                directory.children.append(self.build_directory_template(join(dirpath, childdir)))
                directory.size += getsize(childdir)
            except PermissionError: 
                pass
            except FileNotFoundError: 
                pass
            except OSError: 
                pass

        else:

            pass

    def build_directory_template(self, directoryName):
        directory = InitDirectory(directoryName)

        for (dirpath, childdirs, filenames) in walk(directory.name): 

            for filename in filenames:
                
                directory.files.append(File(filename, getsize(join(dirpath, filename))))
                directory.size += getsize(directory.name + '/' + filename)

            for childdir in childdirs:

                directory.size += getsize(directory.name + '/' + childdir)
                self.build_directory_OS_exceptions(directory, childdir, dirpath)

            break

        return directory


class PrintDirectory:
    def __init__(self, w_file=None):
        self.file = w_file

    def terminal(self, directory, depth=0):
        whitespace = 4*' ' 
        print("{}{}\n".format(depth*whitespace, self.directory.name))

        for file in self.directory.files:

            print("{}{}\n".format((depth+1)*whitespace, file.name))

        for child in self.directory.children:

            self.terminal(child, depth+1)

    def txt(self, directory, depth=0):
        print(("{}{}|{}\n".format(str(depth), self.directory.name, str(self.directory.size))), file=self.file)

        for file in self.directory.files:

            print("DOING SOMETHING")
            print(str(depth) + file.name + '|' + str(file.size), file=self.file)

        for child in self.directory.children:

            print("DOING SOMETHING")
            self.txt(child, depth+1)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # Attribute encapsulation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size