import json, requests, sys, csv, os

count = 0
paymentTotal = 0.0
HEADERS = ["Owner", "List", "Client", "Send Date", "Month", "Sent", "Total Raised", "Transaxt Fee", "Rev Share Price", "Rental Price", "Owner Payment"]


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
        month = stringList[3]
        rentalPrice = stringList[4]
        ownerPayment = stringList[5]

        if owner == previous:

            outputWriter.writerow([owner, emailList,'N/A', 'N/A', month, 'N/A', 'N/A', 'N/A', 'N/A', rentalPrice, ownerPayment])

        else:
            # skip for first round to avoid header
            if count > 2:
                # Close output file for particular owner report
                outputFile.close()
            # Create next output file
            output_file = ".//Geotarget_Reports//" + owner + month + ".2017.csv"
            outputFile = open(output_file, 'w', newline='')
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(HEADERS)
            outputWriter.writerow([owner, emailList,'N/A', 'N/A', month, 'N/A', 'N/A', 'N/A', 'N/A', rentalPrice, ownerPayment])     
            # write header to file
            # write list to file
            # close output file
            # create new output file
            # Add row to list(1st row of new Owner)
            
        
    previous = owner

    count += 1

