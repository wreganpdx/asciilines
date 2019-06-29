from graph import graph
from line import line

class interpret(object):

    def __init__(self):
        return None

    @staticmethod
    def doGraph(a):
        if len(a[0]) < 2:
            print("Invalid file, must have length and width as first two arguments")
            exit(1)

        g = graph(int(a[0][1]), int(a[0][0]))
        for i in range(1, len(a)):
            if len(a[i]) < 5:
                print("Invalid file, line %d, must have format <char> <row> <column> <v or h> <length>")
                exit(1)
            _line = line(a[i][0], int(a[i][1]), int(a[i][2]), a[i][3], int(a[i][4]))
            g.addLine(_line)
        return g


