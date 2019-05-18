import csv
import pandas as pd
import itertools
# D:\Downloads\910ProjectData\perprocessingdata\emw_12.csv
filee = open('D:/Downloads/910ProjectData/preprocessingdata/test1.csv','r')
emw = csv.reader(filee)

filep = open('D:/Downloads/910ProjectData/preprocessingdata/test2.csv','r')
preg = csv.reader(filep)

filecomb = open('D:/Downloads/910ProjectData/preprocessingdata/combtest.csv','w')
writer = csv.writer(filecomb, dialect='excel')
# writer.writerow(list)

count = 0
# [pitem,eitem for pitem in preg for eitem in emw]:
newlist = []
for pitem in preg:
    if preg.line_num == 1:
        continue
    # print(pitem[0])
    #     print(item)
    # print(pitem)
    #     print(item[1])
    #     print(item[0])
    # print(pitem[0])
    # for eitem in itertools.cycle(emw):
    filee = open('D:/Downloads/910ProjectData/preprocessingdata/test1.csv', 'r')
    emw = csv.reader(filee)
    for eitem in emw:
        if emw.line_num == 1:
            continue
        # print(type(eitem[0]))
        # print(pitem[0])
        # print(eitem[0])
        # print(eitem)
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
            count += 1
        # if (pitem[0]) == (eitem[0]):

            # print(pitem[0])
            # print(type(pitem))
            # print(pitem)
            # print(eitem)
            # newline = list(pitem).extend(list(eitem))
            newline = pitem + eitem
            print(newline)
            newlist.append(newline)
        # print(newlist)
    filee.close()
            # newlist.append(eitem)

    # writer.writerow(newlist)
name = ['one','tow','3','4','one','tow','344444','4']
# writer.writerow(emw)
print(newlist)
test = pd.DataFrame(columns=name, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata/testcombpd.csv')

print(count)
# filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv','r')
# emw = csv.DictReader(filee)
#
# filep = open('D:/Downloads/910ProjectData/preprocessingdata/preg_12.csv','r')
# preg = csv.DictReader(filep)
#
# filecomb = open('D:/Downloads/910ProjectData/preprocessingdata/comb.csv','w')
# # writer = csv.DictWriter(filecomb)
# # print(type(preg))
# # print(preg)
# for ie in emw:
#     print(ie)





# with open('D:/Downloads/910ProjectData/preprocessingdata/combine.csv','w'):
