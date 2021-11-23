from collections import *
from typing import*
from math import fsum, sqrt
from dis import *
from functools import partial
from pprint import pprint
from pyodbc import*
from statistics import *

x=[78,47,6,13,345]
y=[345,34,64,23,56,45]
def recmed(x,y):
       count=-1

       for l in y:
         count = count + 1
         if(len(x)>(count)):
             print(x[count], l)
         else:
             print(l)



recmed(x,y)
