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

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg_only.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/educ_01.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final0.csv',index=False)

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final0.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/emw_12.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final1.csv',index=False)

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final1.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/ins_0.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final2.csv',index=False)

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final2.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/jobs_0.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final3.csv',index=False)

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/final3.csv','r')
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
    filee = open('D:/Downloads/910ProjectData/preprocessingdata2/wages_0.csv', 'r')
    emw = csv.reader(filee)
    flag = 0
    for eitem in emw:
        if emw.line_num == 1:
            name1 = eitem
            continue
        if pitem[0] == eitem[0] and pitem[1] == eitem[1]:
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
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/final4.csv',index=False)

