
import json, requests, sys, csv, os


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




# Place data into list, write headers to output, delete headers from list
listed = list(MonthlyReader)
outputWriter.writerow(listed[0])
del(listed[0])

# Sort by message name
listed = sorted(listed, key=lambda x: x[57])



totalSent = 0
totalDelivered = 0
totalClicked = 0
totalOpened = 0
sentTotalHtml = 0
sentTotalPlain = 0
deliveredHtml = 0
deliveredPlain = 0
bouncedHtml = 0
bouncedPlain = 0
invalidTotal = 0
optoutTotal = 0
withheldTotal = 0
globallySurpressedTotal = 0
supressedTotal = 0
clickedUnique = 0
openedUniqued = 0

print(len(listed))
# Loop through each row
for i in listed:

    # Skip to writing output when Resend found
    if i[58] != "Resend":


        if count > 0:
            # Combine Tiers
            if i[57] == client:

                totalSent += int(i[5])
                totalDelivered += int(i[11])
                totalClicked += int(i[30])
                totalOpened += int(i[34])
                sentTotalHtml += int(i[6])
                sentTotalPlain += float(i[7])
                deliveredHtml += int(i[12])
                deliveredPlain += int(i[13])
                bouncedHtml += int(i[18])
                bouncedPlain += int(i[19])
                bouncedTotal += int(i[17])
                invalidTotal += int(i[23])
                optoutTotal += int(i[25])
                withheldTotal += int(i[27])
                globallySurpressedTotal += int(i[28])
                supressedTotal += int(i[29])
                clickedUnique += int(i[31])
                openedUniqued += int(i[35])
                campaignType += i[40]
                hasDynamicContent += int(i[41])
                hasDeliveryReport += int(i[42])
                linkAppendStatement += i[43]
                timezone += i[44]
                ftfForwarded += int(i[45])
                ftfSignups += int(i[46])
                ftfConversionScore += int(i[47])
                includedStaticSegments += '*' + i[48] # "*" deliminator to keep tiered items separated, not necessary
                includedDynamicSegments += '*' + i[49]
                exludedStaticSegments += '*' + i[50]
                exludedDynamicSegments += '*' + i[51]
                roiConversions += float(i[52])
                roiAverage += float(i[53])
                roiTotal += float(i[54])
                bindingTier += '*' + i[55]
                binding += '*' + i[56]

            # New message name, write combined tiers to output
            else:
                # Avoid dividing by 0
                if totalSent > 0:
                    sentRateHTML = sentTotalHtml/totalSent*100
                    deliveredRateTotal = totalDelivered/totalSent*100
                    deliveredRateHTML = deliveredHtml/totalSent*100
                    bouncedRateTotal = bouncedTotal/totalSent*100
                    invalidRateTotal = invalidTotal/totalSent*100
                    optoutRateTotal = optoutTotal/totalSent*100
                sentRatePlain = (sentRateHTML - sentRateHTML)*100


                if sentTotalPlain > 0:
                    deliveredRatePlain = deliveredPlain/sentTotalPlain
                else:
                    deliveredRatePlain = 0

                bouncedRateHTML = bouncedHtml/sentTotalHtml*100
                if sentTotalPlain > 0:
                    bounceRatePlain = bouncedPlain/sentTotalPlain
                else:
                    bounceRatePlain = 0


                clickedRateUnique = clickedUnique/openedUniqued*100
                
                if clickedUnique > 0:
                    clickedRateAPS = totalClicked/clickedUnique
                else:
                    clickedRateAPS = 0
                openedRateUnique = openedUniqued/totalDelivered*100
                openedRateAPS = totalOpened/openedUniqued

                if "Revshare" in BillCode:

                    BillCodeCheck = BillCode.split("-")

                    if len(BillCodeCheck[1]) > 2:
                        campaignCode = BillCodeCheck[1]
                        BillCode = BillCodeCheck[0]

                outputWriter.writerow([messID, messageSubject, date, messageNotes, BillCode, totalSent, sentTotalHtml, sentTotalPlain, '100', sentRateHTML, sentRatePlain, totalDelivered, deliveredHtml, deliveredPlain, deliveredRateTotal, deliveredRateHTML, deliveredRatePlain, bouncedTotal, bouncedHtml, bouncedPlain, bouncedRateTotal, bouncedRateHTML, bounceRatePlain, invalidTotal, invalidRateTotal, optoutTotal, optoutRateTotal, withheldTotal, globallySurpressedTotal, supressedTotal, totalClicked, clickedUnique, clickedRateUnique, clickedRateAPS, totalOpened, openedUniqued, openedRateUnique, openedRateAPS, '', campaignCode, campaignType, hasDynamicContent, hasDeliveryReport,linkAppendStatement,timezone,ftfForwarded,ftfSignups,ftfConversionScore,includedStaticSegments,includedDynamicSegments, exludedStaticSegments,exludedDynamicSegments,roiConversions, roiAverage, roiTotal,bindingTier,'', client])

                # Save variables for tier combination
                messID = i[0]
                messageSubject = i[1]
                date = i[2]
                messageNotes = i[3]
                BillCode = i[4]
                campaignCode = i[39]
                client = i[57]
                totalSent = int(i[5])
                totalDelivered = int(i[11])
                totalClicked = int(i[30])
                totalOpened = int(i[34])
                sentTotalHtml = int(i[6])
                sentTotalPlain = float(i[7])
                deliveredHtml = int(i[12])
                deliveredPlain = int(i[13])
                bouncedHtml = int(i[18])
                bouncedPlain = int(i[19])
                bouncedTotal = int(i[17])
                invalidTotal = int(i[23])
                optoutTotal = int(i[25])
                withheldTotal = int(i[27])
                globallySurpressedTotal = int(i[28])
                supressedTotal = int(i[29])
                clickedUnique = int(i[31])
                openedUniqued = int(i[35])
                campaignType = i[40]
                hasDynamicContent = int(i[41])
                hasDeliveryReport = int(i[42])
                linkAppendStatement = i[43]
                timezone = i[44]
                ftfForwarded = int(i[45])
                ftfSignups = int(i[46])
                ftfConversionScore = int(i[47])
                includedStaticSegments = i[48]
                includedDynamicSegments = i[49]
                exludedStaticSegments = i[50]
                exludedDynamicSegments = i[51]
                roiConversions = float(i[52])
                roiAverage = float(i[53])
                roiTotal = float(i[54])
                bindingTier = i[55]
                binding = i[56]

         # Initial save of tier for combining
        else:

            messID = i[0]
            messageSubject = i[1]
            date = i[2]
            messageNotes = i[3]
            BillCode = i[4]
            campaignCode = i[39]
            client = i[57]
            totalSent = int(i[5])
            totalDelivered = int(i[11])
            totalClicked = int(i[30])
            totalOpened = int(i[34])
            sentTotalHtml = int(i[6])
            sentTotalPlain = float(i[7])
            deliveredHtml = int(i[12])
            deliveredPlain = int(i[13])
            bouncedHtml = int(i[18])
            bouncedPlain = int(i[19])
            bouncedTotal = int(i[17])
            invalidTotal = int(i[23])
            optoutTotal = int(i[25])
            withheldTotal = int(i[27])
            globallySurpressedTotal = int(i[28])
            supressedTotal = int(i[29])
            clickedUnique = int(i[31])
            openedUniqued = int(i[35])
            campaignType = i[40]
            hasDynamicContent = int(i[41])
            hasDeliveryReport = int(i[42])
            linkAppendStatement = i[43]
            timezone = i[44]
            ftfForwarded = int(i[45])
            ftfSignups = int(i[46])
            ftfConversionScore = int(i[47])
            includedStaticSegments = i[48]
            includedDynamicSegments = i[49]
            exludedStaticSegments = i[50]
            exludedDynamicSegments = i[51]
            roiConversions = float(i[52])
            roiAverage = float(i[53])
            roiTotal = float(i[54])
            bindingTier = i[55]
            binding = i[56]



    else:
        outputWriter.writerow(i)
    count +=1
    if(count == len(listed)):
        outputWriter.writerow(i)





outputFile.close()
MonthlyFile.close()
