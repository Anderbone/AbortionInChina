from sas7bdat import SAS7BDAT

with SAS7BDAT('D:/Downloads/910ProjectData/Master_EverMarriedWomen_201804/emw_12.sas7bdat') as f:
    with open('D:/Downloads/910ProjectData/Master_EverMarriedWomen_201804/emw_12.txt','w') as f2:
        for row in f:
            print(row, file=f2)
