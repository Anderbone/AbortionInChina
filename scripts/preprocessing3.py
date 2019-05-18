# after combine preg and emw,
# after change s114: 1 for induced abortion, 0 for other.
# now for duplicate person.

import csv
import pandas as pd
import itertools

name0 = []
filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
preg1 = csv.reader(filep)
for pitem in preg1:
    if preg1.line_num == 1:
        name0 = pitem
        break
filep.close()

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
preg = csv.DictReader(filep)

newlist = []
newdic = {}
countdic = {}
# name0 = []
name1 = []
count_dup = 0
count_single = 0
# count_no = 0
datas = []
# print(preg)
for pitem in preg:

    # if preg.line_num == 1:
    #     name0 = pitem
    #     print(name0)
    #     continue
    if pitem['IDind_m'] not in countdic and str(pitem['S114']) == str(1):
        datas.append(pitem)
        countdic[pitem['IDind_m']] = pitem['S114']
        continue
        # print(newline)
    # print(pitem)
    #     print(dict(pitem))
    # print()
    # else:
    #     oldyear = countdic[pitem['IDind_m']]
    #     temp0 = pitem['IDind_m']
    #     temp1 = pitem['wave']
    # print(temp0)
    # if temp0 in
    # print(temp1)
    # newdic.update(pitem)
    # datas.append(dict(pitem))
# print(count_dup)
# print(count_single)
# print(count_nor)
    # writer.writerow(newlist)
# print(newlist)
# test = pd.DataFrame(columns=name0, data=newlist)
# test.to_csv('D:/Downloads/910ProjectData/preprocessingdata/final02.csv')
filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
preg = csv.DictReader(filep)
for pitem in preg:
    if pitem['IDind_m'] not in countdic:
        datas.append(pitem)
        countdic[pitem['IDind_m']] = pitem['S114']
        continue

with open('D:/Downloads/910ProjectData/preprocessingdata2/preg_only.csv','w',newline='') as f:
    writer = csv.writer(f)
    # print(name0)
    writer.writerow(name0)
    for myorderdic in datas:
        # print(myorderdic)
        # writer.writerow(dict(myorderdic))
        # print(dict(myorderdic).values())
        writer.writerow(dict(myorderdic).values())
    # for row in datas:
    #     print(row)
    #     writer.writerow(row)
    # writer.writerow(datas)

# keys, values = [], []
# for myorderdic in datas:
#     for key, value in myorderdic.items():
#         keys.append(key)
#         values.append(value)
#
# with open("D:/Downloads/910ProjectData/preprocessingdata/final04.csv", "w") as outfile:
#     csvwriter = csv.writer(outfile)
#     csvwriter.writerow(keys)
#     csvwriter.writerow(values)

