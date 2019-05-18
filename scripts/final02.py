
import csv
import pandas as pd

name1 = []
def computepro(pro):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/edu.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    pro = str(pro)
    new = []
    eduyear = {}
    level = {}
    for pitem in preg:
        if pitem[0] == pro:
            if pitem[2]== str(1):
                abortion += 1
            elif pitem[2] == str(0):
                normal += 1

    thisyearall = abortion + normal
    ratio = abortion/thisyearall
    print(pro+"-------")
    print(thisyearall)
    # print(normal)
    # print(abortion)
    print(ratio)
    new.append(pro)
    new.append(ratio)
    return new

listall = []
list0 = computepro(0)
listall.append(list0)
for year in range(11,17):
    i = computepro(year)
    listall.append(i)
for year in range(21,30):
    computepro(year)
    i = computepro(year)
    listall.append(i)
print('ll')
for year in range(32,37):
    computepro(year)
    i = computepro(year)
    listall.append(i)

name1 = ['education year','abortion ratio']
print(listall)

test = pd.DataFrame(columns=name1, data=listall)
test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/edufinal.csv',index=False)
