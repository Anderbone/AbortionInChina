import csv
import pandas as pd
import itertools
# D:\Downloads\910ProjectData\perprocessingdata\emw_12.csv
# filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv','r')
# emw = csv.reader(filee)

#combine edu to final04
#then health to final6
# then jobs to final7
# TODO then wage to final9

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg_12.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata/carec_0.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[5] == eitem[0] and pitem[1] == eitem[1]:
            # and pitem[2] == eitem[2]
            newline = pitem + eitem
            # print(newline)
            newlist.append(newline)
            flag = 1
            break
    filee.close()
    if flag == 0:
        newlist.append(pitem)

    # writer.writerow(newlist)
name = name0 + name1
# name = ['one','tow','3','4','one','tow','344444','4']
# print(newlist)
test = pd.DataFrame(columns=name, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata/final14.csv')

