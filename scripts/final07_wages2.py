import numpy as np
import csv

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
        if pitem[3] == pro:
            if pitem[2].isdigit():
                # print(pitem[2])
                num = float(pitem[2])
                new.append(num)
    print(pro+"-------")
    # new.append(count)
    # print(new)
    mean = np.mean(new)
    med = np.median(new)
    return mean,med

listall = []


def avg(num):
    i = computepro(num)
    print(i)
    listall.extend(i)
    # print(listall)

avg(2015)
avg(2011)
avg(2009)
avg(2006)
avg(2004)
avg(2000)
avg(1997)
avg(1993)
avg(1991)