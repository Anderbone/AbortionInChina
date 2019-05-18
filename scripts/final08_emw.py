import pandas as pd
import numpy as np
import csv
newlist = []
name0 = []
filep = open('D:/Downloads/910ProjectData/preprocessingdata2/emw.csv','r')
preg = csv.reader(filep)
# son = 0
# daughter = 0
# pro = str(pro)
new = []
count = 0
for pitem in preg:
    newline = pitem
    if preg.line_num == 1:
        name0 = pitem
        continue
    if pitem[1].isdigit() and pitem[3].isdigit():
        son = int(pitem[1]) + int(pitem[3])
    else:
        son = ''
    if pitem[2].isdigit() and pitem[4].isdigit():
        daughter = int(pitem[2]) + int(pitem[4])
    else:
        daughter = ''
    newline.append(son)
    newline.append(daughter)
    newlist.append(newline)

print(name0)
name0 = name0+list('s')
name0 = name0+list('d')
test = pd.DataFrame(columns=name0, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/emw2.csv')
