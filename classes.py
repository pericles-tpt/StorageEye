class Directory:
    def __init__(self, directoryName):
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

    