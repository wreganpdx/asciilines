import sys
import numpy as np
import os.path
# count the arguments
class DataInit(object):

    def __init__(self):
        return None

    @staticmethod
    # simple class to quantify data based on command line input for data.
    def getData():
        fName = "tests/test1.tvg"
        while ready != True:
            print("1: tests/test1.tvg")
            print("2: tests/test2.tvg")
            print("3: tests/test3.tvg")
            print("Choose a File: 1, 2, 3, (C)ustom, (E)xit")
            g = raw_input(":")
            if g == "1":
                fName = "tests/test1.tvg"
                ready = True
            if g == "2":
                fName = "tests/test2.tvg"
                ready = True

            if g == "3":
                fName = "tests/test3.tvg"
                ready = True


            if g == "c" or g == "C":
                print("What file would you like to use?")
                fName = raw_input(":")
                if os.path.exists(fName):
                    ready = True
                else:
                    print("file does not exist!")

            if g == "E" or g == "e":
                print("Exit selected, exiting program!")
                exit(1)

        return fName
