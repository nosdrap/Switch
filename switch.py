from array import *
def switch(variable,array):
    for x in array:
        if variable == x[0] or x[0] == "default":
            return x[1]