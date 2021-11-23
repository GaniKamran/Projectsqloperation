from typing import *
from math import fsum
from pprint import pprint
from collections import OrderedDict,defaultdict
def unit(rg,stk:Optional[int]=None)-> int:
    if(stk==None):
        stk=60
    return rg+stk
print(unit(6))
d={"raymond":"wejf"}
e=defaultdict(lambda :"secular")
e["Segment"]="Baku"
print(e["ewf"])
Furry=defaultdict(set)
Furry["Fifty"].add("Name1")
Furry["Fifty"].add("Name2")
Furry["Fifty1"].add("Name3")
Furry["Fifty1"].add("Name4")
pprint(Furry)
for i in Furry:
    print(Furry[i])
NewCyberNova=defaultdict(list)
NewCyberNova["resurs"].append("Nova")
NewCyberNova["Feridanse"].append("Security Service connection")
pprint(NewCyberNova)
names=('''Feruda Sedaka Landrivers Satelite Carbon Jerusalim Atomic Mason Enerji Vertical Modern Warfare'''.split())
Zerdo=defaultdict(list)
for name in names:
    fulter=name[0]
    Zerdo[fulter].append(name)

pprint(Zerdo)
print(list(zip("abdbl","jvns")))
pprint(list(zip([100,225,350],[475,600,725],[1000,1125,1250])),width=30)
it=iter('abcd')
print(list(it))