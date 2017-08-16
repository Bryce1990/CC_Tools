import json, requests, sys, csv, os

count = 0
paymentTotal = 0.0
HEADERS = ["Owner", "List", "Client", "Send Date", "Month", "Sent", "Total Raised", "Transaxt Fee", "Rev Share Price", "Rental Price", "Owner Payment", "Delivered", "Clicked", "Opened"]


# Set up input/ouput files
input_file = input("Input Filename: ")
MonthlyFile = open(input_file)
MonthlyReader = csv.reader(MonthlyFile)

# Read each row of input file
for row in MonthlyReader:
    
    
    stringList = row
    owner = stringList[0]
    if count != 0:

        owner = stringList[0]
        emailList = stringList[1]
        client = stringList[2]
        date = stringList[3]
        month = stringList[4]
        sent = stringList[5]
        totalRaised = stringList[7]
        TAfee = stringList[8]
        revSharePrice = stringList[9]
        rentalPrice = stringList[10]
        ownerPayment = stringList[14]
        delivered = stringList[19]
        clicked = stringList[20]
        opened = stringList[21]

        
        if owner == previous:

            outputWriter.writerow([owner, emailList,client, date, month, sent, totalRaised, TAfee, revSharePrice, rentalPrice, ownerPayment, delivered, clicked, opened])
            
        else:
            # skip for first round to avoid header
            if count > 2:
                # Close output file for particular owner report
                # outputWriter.writerow(['', '','', '', '', '', '', '', '', 'Total', paymentTotal])
                outputFile.close()
                paymentTotal = 0
                
            # Create next output file
            output_file = ".//Owner_Reports//" + owner + month + ".2017.csv"
            outputFile = open(output_file, 'w', newline='')
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(HEADERS)
            outputWriter.writerow([owner, emailList,client, date, month, sent, totalRaised, TAfee, revSharePrice, rentalPrice, ownerPayment])
           
            # write header to file
            # write list to file
            # close output file
            # create new output file
            # Add row to list(1st row of new Owner)
            
        
    previous = owner

    count += 1

