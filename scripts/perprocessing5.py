import csv
import pandas as pd

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final4.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/urban_0.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[24] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final5.csv',index=False)