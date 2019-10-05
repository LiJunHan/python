class WriteFile:
    def __init__(self, path):
        self._path = path

    def writeFile(self, content):
        with open(self._path, 'w') as fp:
            fp.write(content)
