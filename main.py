from collections import *
from statistics import *
from random import *
x=300
Al=1005
print("airlanes have {0} km/hour speed {1} metrs highway " .format(x,Al))
c=Counter("red,green,red,green,yellow,yellow,yellow".split(","))
print(list(c))
print(list(c.most_common(1)))
print(mean([60,62,64,65]))
print(median([56,59,76,87]))
print(mode([65,66,67,76,88,66]))
print(stdev([50,50,50,50]))
print(pstdev([60,61,62,63]))
f=lambda x:x**2
print(f(20))
z=[10,23,24,356,7,45,6]
print(sorted(z))
Miama="Lambada"
i=Miama.index("a")
Miama.count("a")
def Rt(Guard):
    Guard=lambda x,y:x+y
    return  Guard

print(Rt((3,2)))
Zenit=lambda y,z:x+y
print(random())
print(uniform(150,160))
print(triangular(100,299,766))
print(gauss(100,20))
print(expovariate(23))
data=[uniform(1000,1200) for i in range(1,1000)]
print(mean(data))
print(stdev(data))
print(pstdev(data))
lmm=choice(['red','green','red','green','yellow','yellow','yellow'])
deck=Counter(Age=12, Name=12)
deck=list(deck.elements())
deal=sample(deck,24)
print(deal)