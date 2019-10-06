from docx import Document
import re

class ReadFile:
    """读取文件的类"""
    def __init__(self, filename):
        self._filename = filename

    def loadfile(self):
        """读取文件并将其内容写进字符串中"""
        global content
        filetype = re.findall('\.(\w+)', self._filename)[0]
        if filetype == 'txt':
            with open(self._filename) as fp:
                content = fp.read()
        elif filetype == 'docx':
            document = Document(self._filename)
            content = ''
            for para in document.paragraphs:
                content = content + para.text

        return content
