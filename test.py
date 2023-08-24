import math
import numpy as np 

def asc_des_none(lst, s):

    if(s == "Desc"):
  
        return sorted(lst)
    elif (s == "Asc"):

        return sorted(lst,reverse=True)
    else:
        return lst


print(asc_des_none([1,3,2,4],"asc"))