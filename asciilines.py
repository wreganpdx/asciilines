from DataInit import DataInit
from interpret import interpret
from fillGraph import  fillGraph
import numpy as np
data = DataInit.retrieve()

print (data)

g = interpret.doGraph(data)

a = np.full((g.height, g.width), '.')

print(a)

fillGraph.fill(a, g)



for i in range(len(a)):
    for k in range(len(a[i])):
        print(a[i][k]),
    print("")
