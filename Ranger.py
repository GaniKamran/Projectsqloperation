from typing import Iterable,Tuple
from math import fsum,sqrt
from pprint import pprint
from collections import *
from functools import partial
from statistics import *
from dis import *

martinals=[
    (10,34,65),
    (46,34,56),
    (34,63,24)
]
p=(10,5,6)
q=(30,15,65)
def mean(data:Iterable[float])->float:
        data=list(data)
        return fsum(data)/len(data)
def dist(p:Tuple[int,...], q:Tuple[int,...], fsum=fsum, sqrt=sqrt,zip=zip):
    return sqrt(fsum([(x-y)**2 for x,y in zip(q,p)]))
zema=sqrt(fsum([(x-y)**2 for x,y in zip(q,p)]))
print(zema)
for martinal in martinals:
    print(martinal,dist(martinal,(23,43,43)))
def assihg(centroids , data):
    d=defaultdict(list)
    for martinal in data:
        closest_centroids=min(centroids, key = partial(dist,martinal))
        d[closest_centroids].append(martinal)
    return d
def cmputingmes(groups):
    return [tuple(map(mean,zip(*group))) for group in groups]