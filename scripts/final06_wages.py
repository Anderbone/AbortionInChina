
import csv
import pandas as pd

name1 = []
all = 0
def computepro(pro):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/jobs.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    pro = str(pro)
    new = []
    count = 0
    for pitem in preg:
        if preg.line_num == 1:
            # name0 = pitem
            continue
        if pitem[7] == pro:
            if pitem[6].isdigit():
                # print(pitem[2])
                num = float(pitem[6])
                abortion += num
                count += 1
                # print(count)
    # print(pro+"-------")
    # print(abortion)
    # print(count)
    ave = abortion/count
    new.append(ave)
    return new

listall = []

def avg(num):
    i = computepro(num)
    listall.extend(i)
    print(listall)

avg(2015)
avg(2011)
avg(2009)
avg(2006)
avg(2004)
avg(2000)
avg(1997)
avg(1993)
avg(1991)

# test = pd.DataFrame(columns=name1, data=listall)
# test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/jobfinal.csv',index=False)
