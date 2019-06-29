class fillGraph(object):

    def __init__(self, a, graph):

        return None

    @staticmethod
    def fill(a, graph):
        for i in range(len(graph.lines)):
            dir = graph.lines[i].dir
            if dir == "V" or dir == "v":
                print("doing vert line")
                fillGraph.fillVert(a, graph.lines[i], graph.width, graph.height)
            if dir == "H" or dir == "h":
                print("doing horizontal line")
                fillGraph.fillHorz(a, graph.lines[i], graph.width, graph.height)
        return a

    @staticmethod
    def fillVert(a, line, width, height):
        if line.column < 0 or line.column >= width:
            return
        for i in range(line.length):
            row = i + line.row
            if row < 0 or row >= height:
                continue
            print (height)
            print (line.char)
            a[row][line.column] = line.char

    @staticmethod
    def fillHorz(a, line, width, height):
        if line.row < 0 or line.row >= height:
            return
        for i in range(line.length):
            column = i + line.column
            if column < 0 or column >= width:
                continue

            print (width)
            print (line.char)
            a[line.row][column] = line.char