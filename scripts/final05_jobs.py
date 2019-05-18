
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
        if pitem[5] == pro:
            count += 1
    print(pro+"-------")
    new.append(count)
    return new

listall = []

for year in range(1,15):
    i = computepro(year)
    listall.extend(i)

sum = 0
for i in listall:
    sum += int(i)
print(sum)
ratio = []
for i in listall:
    ratio.append(i/sum)
print(ratio)


name1 = ['education year','abortion ratio']
print(listall)

# test = pd.DataFrame(columns=name1, data=listall)
# test.to_csv('D:/Downloads/910ProjectData/preprocessingdata2/jobfinal.csv',index=False)
