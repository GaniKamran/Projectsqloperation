from collections import *
from pprint import *
import csv
d=defaultdict(list)
d["Raymond"].append("Machine Gun")
d["Silver"].append("Pistol")
d["Raymond"].append("Minigun")
d["Silver"].append("Sniper")
pprint(d)
xd=defaultdict(list)
xd={
    'WayForPayload':['Railway','Airlines','Roadway','Ship'],
    'Information':['EthernetOptic','Phones','WirelessStation'],
    'Powerpayload':['ElectricCabel','Gas'],
}
xd['Information'].append('Nub')
pprint(xd)
b=defaultdict(list)
for key,items in xd.items():
    for item in items:
     b[item].append(key)
pprint(b)
with open('Zenon.csv', encoding='utf-8') as m:
        reader=csv.reader(m)
        veto_topic=next(reader)

        for Area, Way, Progress, Device, Barkod in reader:
            print(Area,Progress)
with open('venv/Revalution.txt',encoding='utf-8') as f:

    for row in f:
        print(row)

t=("Raymond","Richard","Shekspir")
name,fname,ftname=t
print(name)
names="Ruzveld Stalin Chorchill".split()
Lastnames="Uilyam Iosif Winston".split()
Cities="Baku,London,Washington,New-York,Boston,Pekin,Tokio".split(",")
print(names[0])
for i in range(len(names)):
    print(names[i])
for i in range(len(names)):
    print(i,names[i])

print(names[1])
for i , name in enumerate(names ,start=1):
    print(i,name)
for City in reversed(Cities):
    print(City)
m=min(len(names),len(Lastnames))
pprint(m)
for i in range(m):
    print(names[i],Lastnames[i])
for i,l in zip(names, Lastnames):
    print(i,l)
for i,name in enumerate(map(str.upper,reversed(sorted(set(names))))):
    print(i,name)