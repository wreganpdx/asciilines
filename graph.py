class Graph(object):

    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.lines = []
        return None

    def addLine(self, line):
        self.lines.append(line)

    