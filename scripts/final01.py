# using preg1. the year and province.
import csv
import pandas as pd
def computeyear(year):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    year = str(year)
    for pitem in preg:
        if pitem[1] == year:
            if pitem[9] == str(0):
                normal += 1
            if pitem[9] == str(1):
                abortion += 1
    thisyearall = abortion + normal
    ratio = abortion/thisyearall
    print(year+"-------")
    print(thisyearall)
    print(normal)
    print(abortion)
    print(ratio)
# computeyear(2015)
# computeyear(2011)
# computeyear(2009)
# computeyear(2006)
# computeyear(2004)
# computeyear(2000)
# computeyear(1997)
# computeyear(1993)
# computeyear(1991)


def computepro(pro):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    pro = str(pro)
    for pitem in preg:
        if pitem[25] == pro:
            if pitem[9] == str(0):
                normal += 1
            if pitem[9] == str(1):
                abortion += 1
    thisyearall = abortion + normal
    ratio = abortion/thisyearall
    print(pro+"-------")
    print(thisyearall)
    print(normal)
    print(abortion)
    print(ratio)

# computepro(11)
# computepro(21)
# computepro(23)
# computepro(31)
# computepro(32)
# computepro(37)
# computepro(41)
# computepro(42)
# computepro(43)
# computepro(45)
# computepro(52)
# computepro(55)

# rural/urban
def computepro1(pro):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    pro = str(pro)
    for pitem in preg:
        if pitem[26] == pro:
            if pitem[9] == str(0):
                normal += 1
            if pitem[9] == str(1):
                abortion += 1
    thisyearall = abortion + normal
    ratio = abortion/thisyearall
    print(pro+"-------")
    print(thisyearall)
    print(normal)
    print(abortion)
    print(ratio)
# computepro1(1)
# computepro1(2)

# gender
def computepro2(pro):
    filep = open('D:/Downloads/910ProjectData/preprocessingdata2/preg1.csv','r')
    preg = csv.reader(filep)
    abortion = 0
    normal = 0
    pro = str(pro)
    for pitem in preg:
        if pitem[10] == pro:
            if pitem[9] == str(0):
                normal += 1
            if pitem[9] == str(1):
                abortion += 1
    thisyearall = abortion + normal
    ratio = abortion/thisyearall
    print(pro+"-------")
    print(thisyearall)
    print(normal)
    print(abortion)
    print(ratio)

computepro2(1)
computepro2(2)