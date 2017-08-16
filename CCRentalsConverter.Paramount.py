#ExternalRentalsWeeklyConverter.py - A program to convert raw spreadsheet of internal
#rentals to usable form for accounting purposes

import csv, shutil, os

#Read in the raw data file and set output file
input_file = input("Input Filename: ")
output_file = input("Output Month_Directory\\Filename: ")
WeeklyFile = open(input_file, encoding='utf8')
WeeklyReader = csv.reader(WeeklyFile, delimiter = '\t')
ClientDateList = ''

#create output file
outputFile = open(output_file,'w',newline='')
outputWriter = csv.writer(outputFile)
count = 0

outputWriter.writerow(["Date", "Bill Code", "Sent", "Campaign Code", "Raised", "Client","Delivered" , "Clicked", "Opened"])
#Read each row of input file
for row in WeeklyReader:
   stringList = row
   position = 0
   ClientDateList = str(stringList[57])
   
   clientDateList = ClientDateList.split("(")
   #print(clientDateList)
   print(count)
   date = stringList[2].split(' ')
   campaignCode = stringList[39]
   if count != 0:
      print(count)
      print(clientDateList)
      #client = clientDateList[0]
      billCode = stringList[4]
      campaignCode= stringList[39]
      #List = clientDateList[2]
      rentOrRevShare = stringList[4]
      deliveredTotal = stringList[11]
      clickedTotal = stringList[30]
      openedTotal = stringList[34]
      outputWriter.writerow([date[0], billCode, stringList[5], campaignCode, "", clientDateList[:1], deliveredTotal, clickedTotal, openedTotal])
   count += 1
   

   
   #clientDateList = stringList[55].split(' ')
   
   
   
  

outputFile.close()

#shutil.move('C:\\Users\\Bryce\\Desktop\\Python\\' + output_file, 'C:\\Users\\Bryce\\Desktop\\Conservative_Connector\\November2016')



