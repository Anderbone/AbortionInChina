
import csv
import pandas as pd

filep = open('D:/Downloads/910ProjectData/preprocessingdata2/ins2.csv' ,'r')
preg = csv.reader(filep)
abortion = 0
normal = 0
# pro = str(pro)
new = []
eduyear = {}
level = {}
have = 0
no = 0
for pitem in preg:
    if pitem[5] == str(1):
        have += 1
    elif pitem[5] == str(0):
        no += 1
print(no)
print(have)
all = no + have
print(all)
print(have/all)

