import sys

class Directory:
    def __init__(self, directoryName=sys.path[0]):
        self._name = directoryName
        self._children = []
        self._files = []
        self._size = 0

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

        @property
        def dirpath(self):
            return self._dirpath

        def print_directory(directory=self, depth=0):

            whitespace = 4*' ' 
            print("{}{}\n".format(depth*whitespace, directory.name))

            for file in directory.files:
                print("{}{}\n".format((depth+1)*whitespace, file.name))
            for child in directory.children:
                self.print_directory(child, depth+1)

        def print_directory_file(directory=self, depth=0):

            print(("{}{}|{}\n".format(str(depth), directory.name, str(directory.size))), file=dirlog_original)

            for file in directory.files:
                print(str(depth) + file.name + '|' + str(file.size), file=dirlog_original)
            for child in directory.children:
                self.print_directory_file(child, depth+1)

        def build_directory(directoryName=self.name):
            for (dirpath, childdirs, filenames) in walk(directory.name): 

                for filename in filenames:

                    directory.files.append(File(filename, getsize(join(dirpath, filename))))
                    directory.size += getsize(directory.name + '/' + filename)

                for childdir in childdirs:

                    directory.size += getsize(directory.name + '/' + childdir)

                    # Mac
                    # Folders excepted from scan are current stop-gap solution to scan taking upwards of 30 minutes

                    # FIX: Figure out how deep a scan of these folders needs to be (if they need to be scanned at all)
                    # to get useful information for the user and form there do a scan to a certain depth of the folders
                    if system() == "Darwin":
                        if (childdir != 'Volumes' and childdir != 'EFIROOTDIR' and childdir != 'bin' and childdir != 'sbin' 
                            and childdir != 'System' and childdir != 'Library' and childdir != 'usr'): 
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

                    # Windows and Linux (maybe...)           
                    else:
                        directory.children.append(build_directory(join(dirpath, childdir)))
                        directory.size += getsize(childdir)

                break

            return directory

        self.build_directory()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

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

    