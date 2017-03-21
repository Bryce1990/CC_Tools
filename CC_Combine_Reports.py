import csv, os, shutil

ownerReports = os.listdir('C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Owner_Reports')
GeoReports = os.listdir('C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Geotarget_Reports')



for report in ownerReports:
    # Use else statement and shutil.move for non geo matches, move files to "Monthly_Reports"
    if report in GeoReports:
        owner_file = 'C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Owner_Reports\\' + report
        geo_file = 'C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Geotarget_Reports\\' + report
        ownerFile = open(owner_file)
        geoFile = open(geo_file)

        ownerReader = csv.reader(ownerFile)
        geoReader = csv.reader(geoFile)
        output_file = './/Monthly_Reports//' + report
        outputFile = open(output_file, 'w', newline = '')
        outputWriter = csv.writer(outputFile)
        

        for row in ownerFile:
            output = row.split(',')
            end = len(output)
            
            output[end-1] = output[end-1].rstrip('\n')
           
            #print(output)
            outputWriter.writerow(output)
        count = 0
        for row in geoFile:
            if count != 0:
                stringList = row.split(',')
                end = len(stringList)
                stringList[end-1] = stringList[end-1].rstrip('\n')
                
                outputWriter.writerow(stringList)
            count += 1
        outputFile.close()
        ownerFile.close()
        geoFile.close()

    else:
        shutil.move('.\\Owner_Reports\\' + report, 'C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Monthly_Reports')

#Output Payment totals
monthlyReports = os.listdir('C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Monthly_Reports')
for report in monthlyReports:
    monthly_file = 'C:\\Users\\Bryce\\Desktop\\Python\\Conservative Connector Tools\\Monthly_Reports\\' + report
    monthlyFile = open(monthly_file)

    monthlyReader = csv.reader(monthlyFile)
    total = 0
    count = 0
    for row in monthlyReader:
        
        
        ownerPayment = row[10]
        owner = row[0]
        if count != 0:
            
            if ownerPayment != 'N/A':
                total += float(ownerPayment)
                
        count += 1
    
    print('%s: $%.2f ' % (owner, total))
    monthlyFile.close()
