from collections import *
from pprint import *
import csv

Senator=namedtuple('Senator',[('Progress',str), ('Device',str),('Barkod',str)])
acumulated_record=defaultdict(list)
with open('Zenon.csv', encoding='utf-8') as m:
    reader = csv.reader(m)
    veto_topic = next(reader)
    for Area, Way, Progress, Device, Barkod in reader:
        senator=Senator(Progress, Device, Barkod)
        acumulated_record[senator].append(Way)
        print(Area, Progress)
pprint(acumulated_record,width=500)