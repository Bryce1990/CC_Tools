
import json, requests, sys, csv, os

CAMPAIGN_KEYS = {
    "Company Name": 'API_KEY',
    }
# Read in the raw data file and set output file
input_file = input("Input Filename: ")
output_file = input("Output Filename: ")
MonthlyFile = open(input_file)
MonthlyReader = csv.reader(MonthlyFile)
ClientDateList = ''

# Create output file
outputFile = open(output_file,'w',newline='')
outputWriter = csv.writer(outputFile)
count = 0


# Read each row of input file
for row in MonthlyReader:

    stringList = row
    client = stringList[5]
    campaignCode = stringList[3]
    raised = stringList[4]
    print(campaignCode)

    # Skip header row
    if count != 0:

        # Check for a campaign code
        if campaignCode != "0" and raised == '':
            apiKey = CAMPAIGN_KEYS[client]
            print(apiKey)
            # TA API for campaign totals
            url = 'https://transaxt.com/api/1/campaigntotals/%s/json?apikey=%s' % (campaignCode, apiKey)
            response = requests.get(url)
            
            

            data = json.loads(response.text)

            if data['ResultCode'] == 0:
                # Add Gross Donations to row
                stringList[4] = data['GrossTotal']
            
    # Write row to output file    
    outputWriter.writerow(stringList)
    count += 1



outputFile.close()
MonthlyFile.close()
