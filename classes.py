class Directory:
    def __init__(self, directoryName, parentDir=None):
        self.parent = parentDir
        self.name = directoryName

    children = []
    files = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size