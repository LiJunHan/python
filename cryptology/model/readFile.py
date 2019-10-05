class ReadFile:
    """读取文件的类"""
    def __init__(self, filename):
        self._filename = filename

    def loadfile(self):
        """读取文件并将其内容写进字符串中"""
        with open(self._filename) as fp:
            content = fp.read()
        return content
