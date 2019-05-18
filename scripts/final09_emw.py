import csv
import pandas as pd

name1 = []
all = 0

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/emw4.csv','r')
preg = csv.reader(filep)
abortion = 0
normal = 0
# pro = str(pro)
new = []
notwant = 0
want = 0
for pitem in preg:
    if pitem[7] == str(0):
        notwant += 1
    elif pitem[7] == str(1):
        want += 1

print("abor-------")
print(want)
print(notwant)
all = want + notwant
print(want/all)
# new.append(count)