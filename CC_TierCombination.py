
import json, requests, sys, csv, os
import pandas as pd
from pandas import DataFrame

# Read in the raw data file and set output file
input_file = input("Input Filename: ")
output_file = input("Output Filename: ")
MonthlyFile = open(input_file)
MonthlyReader = csv.reader(MonthlyFile)
ClientDateList = ''

# Create output file
outputFile = open(output_file,'w', newline='')
outputWriter = csv.writer(outputFile)
count = 0





listed = list(MonthlyReader)


listed = sorted(listed, key=lambda x: x[5])



totalSent = 0
totalDelivered = 0
totalClicked = 0
totalOpened = 0

# Sorted, ready to combine tiers
for i in listed:

    if count == 0:
        outputWriter.writerow(i)
    if count > 1:
        if i[5] == client:

            totalSent += int(i[2])
            totalDelivered += int(i[6])
            totalClicked += int(i[7])
            totalOpened += int(i[8])

        else:
            outputWriter.writerow([date, BillCode, totalSent, campaignCode, "", client, totalDelivered, totalClicked, totalOpened])
            date = i[0]
            BillCode = i[1]
            campaignCode = i[3]
            client = i[5]
            totalSent = int(i[2])
            totalDelivered = int(i[6])
            totalClicked = int(i[7])
            totalOpened = int(i[8])

    elif count != 0:

        date = i[0]
        BillCode = i[1]
        campaignCode = i[3]
        client = i[5]
        totalSent = int(i[2])
        totalDelivered = int(i[6])
        totalClicked = int(i[7])
        totalOpened = int(i[8])
    count +=1




outputFile.close()
MonthlyFile.close()
