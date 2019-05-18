import csv
import pandas as pd
import itertools
# D:\Downloads\910ProjectData\perprocessingdata\emw_12.csv
# filee = open('D:/Downloads/910ProjectData/preprocessingdata/emw_12.csv','r')
# emw = csv.reader(filee)

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
count_abo = 0
count_nor = 0
count_no = 0
for pitem in preg:
    if preg.line_num == 1:
        name0 = pitem
        continue
    if str(pitem[9]) == str(2):
        newline = pitem
        newline[9] = 1
        count_abo += 1
        newlist.append(newline)
        # print(newline)
    elif pitem[9] == '':
        count_no += 1
        continue
    else:
        newline = pitem
        newline[9] = 0
        count_nor += 1
        newlist.append(newline)
print(count_abo)
print(count_no)
print(count_nor)
    # writer.writerow(newlist)
# name = ['one','tow','3','4','one','tow','344444','4']
# print(newlist)
test = pd.DataFrame(columns=name0, data=newlist)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/preg0.csv')

