import sys
import numpy as np
import os.path
class DataInit(object):

    def __init__(self):
        return None

    @staticmethod
    def retrieve():
        arguments = len(sys.argv)
        if arguments > 1:
           # print("retrieving file: %s" % sys.argv[1])
            return DataInit.getDataF(sys.argv[1])
        else:
            return DataInit.getData()

    @staticmethod
    def getData():
        fName = "tests/test1.tvg"
        while True:
            print("1: tests/test1.tvg")
            print("2: tests/test2.tvg")
            print("3: tests/test3.tvg")
            print("Choose a File: 1, 2, 3, (C)ustom, (E)xit")
            valid = False
            g = raw_input(":")
            if g == "1":
                fName = "tests/test1.tvg"
                valid = True
            if g == "2":
                fName = "tests/test2.tvg"
                valid = True
            if g == "3":
                fName = "tests/test3.tvg"
                valid = True

            if g == "c" or g == "C":
                print("What file would you like to use?")
                fName = raw_input(":")
                if os.path.exists(fName):
                    valid = True
                else:
                    print("file does not exist!")
                    continue

            if g == "E" or g == "e":
                print("Exit selected, exiting program!")
                exit(1)

            if valid != True:
                print("Command Invalid!!!")
                continue

            graphInfo = []
            for line in open(fName):
                graphInfo.append(np.array(line.rstrip().split(' ')))
            return graphInfo

    @staticmethod
    def getDataF(fName):
        if os.path.exists(fName):
            graphInfo = []
            for line in open(fName):
                graphInfo.append(np.array(line.rstrip().split(' ')))
            return graphInfo
        else:
            print("file does not exist, perhaps try these options:")

            return DataInit.getData()