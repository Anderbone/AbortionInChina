import csv
import itertools
# D:\Downloads\910ProjectData\perprocessingdata\emw_12.csv
filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv','r')
emw = csv.reader(filee)

filep = open('D:/Downloads/910ProjectData/preprocessingdata/preg_12.csv','r')
preg = csv.reader(filep)

filecomb = open('D:/Downloads/910ProjectData/preprocessingdata/comb.csv','w')
writer = csv.writer(filecomb)
# writer.writerow(list)

count = 0
# [pitem,eitem for pitem in preg for eitem in emw]:

for pitem in preg:
    if preg.line_num == 1:
        continue
    # print(pitem[0])
    #     print(item)
    #     print(item[1])
    #     print(item[0])
    # print(pitem[0])
    # for eitem in itertools.cycle(emw):
    filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv', 'r')
    emw = csv.reader(filee)
    newlist = []
    for eitem in emw:
        if emw.line_num == 1:
            continue
        # print(type(eitem[0]))
        if pitem[0] == eitem[0] and pitem[23]== eitem[15]:
            count += 1
        # if (pitem[0]) == (eitem[0]):

            # print(pitem[0])
            # print(type(pitem))
            newline = list(pitem).extend(list(eitem))
            newlist.append(newline)
            # newlist.append(eitem)

    writer.writerow(newlist)

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
