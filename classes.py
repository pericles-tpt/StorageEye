class Directory:
    def __init__(self, directoryName):
        self.name = directoryName
        self.children = []
        self.files = []
        self.size = 0

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size