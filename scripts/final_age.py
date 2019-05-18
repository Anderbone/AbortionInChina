import csv
import pandas as pd
import itertools
# D:\Downloads\910ProjectData\perprocessingdata\emw_12.csv
# filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv','r')
# emw = csv.reader(filee)

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final6.csv','r')
preg = csv.reader(filep)
# for item in preg:
#     if preg.line_num == 2:
#         print(item[0])

# filecomb = open('D:/Downloads/910ProjectData/preprocessingdata/combfff.csv','w')
# writer = csv.writer(filecomb)

newlist = []
name0 = []
name1 = []
for pitem in preg:
    if preg.line_num == 1:
        name0 = pitem
        continue
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/age.csv', 'r')
    emw = csv.reader(filee)
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1].isdigit() and eitem[1].isdigit():
            eitem_age = int(pitem[1]) - int(eitem[1])
            newline = pitem + [eitem_age]
            # print(newline)
            newlist.append(newline)
    filee.close()

    # writer.writerow(newlist)
name = name0 + ['a']
# name = ['one','tow','3','4','one','tow','344444','4']
# print(newlist)
test = pd.DataFrame(columns=name, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata/final7.csv')

