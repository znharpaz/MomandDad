import math
import numpy as np

def my_activation(i):
    if i < 1 and i >=0:
        return(i)
    if i < 0 and i > -1:
        return(abs(i))
    else:
        return(abs(1/i))
def mysigmoid(x):
    return ( 1/(1 + math.exp(-x)) )

def Nuralnet():
    NN = np.zeros ( (6, 6) )
    NN[0][2] = 1
    NN[0][3] = 1
    NN[0][4] = 1
    NN[1][2] = 1
    NN[1][3] = 1
    NN[1][4] = 1
    NN[2][5] = 1
    NN[3][5] = 1
    NN[4][5] = 1
    print(NN)
    Values = np.zeros ((6))
    print(Values)
    Values[0] = 1
    Values[1] = 1
    print(Values)
    for i in range (0,6):
        for j in range (0,6):
            #print("NN", i, j)
            if (NN[i][j] == 1):
                print (i, "is connected to", j)
                k = mysigmoid(Values[i]) + Values[j]
                Values[j] = k
                print(Values)
                print(k)





Nuralnet()
#while True:
    #x = float(input("Pick a number: "))
    #print("Sigmoid ")
    #print( mysigmoid(x) )
    #print("my activation")
    #print( my_activation(x))
