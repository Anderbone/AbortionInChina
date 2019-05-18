import csv
import pandas as pd

newlist =name0 = name1 = []
filep = open('D:/Downloads/910ProjectData/preprocessingdata/preg_12.csv','r')
preg = csv.reader(filep)
for pitem in preg:
    if preg.line_num == 1:
        name0 = pitem
        continue
    filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv', 'r')
    emw = csv.reader(filee)
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
            newline = pitem + eitem
            newlist.append(newline)
    filee.close()
name = name0 + name1
test = pd.DataFrame(columns=name, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata/final07.csv')

