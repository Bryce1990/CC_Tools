
import json, requests, sys, csv, os

CAMPAIGN_KEYS = {
    "AmericanAgenda": '9b7e9a8b90ee441c8f50',
    'Clarke': '0271935274824eb4b6fa',
    'Mandel': '43c72a2ab423484abc48',
    'RJC': 'cd879a6c1b744f47814a',
    'GAAPAC': '11949b76da534d56b71a',
    'Gillespie': '71daec5c34f34378b992',
    'Love': '4078e908af3d42ae94f1',
    'Rogers': '98b6101a0a5d40fb937d',
    'LI': '5178dc8efcf54b52bafd',
    'Norman': '80e4999f910942cdaa3b',
    'TPP': 'bf3be9ec610746858a0b',
    'Brakey': 'c057fa34c1ae4b51a285',
    'Brooks': '7e7949c518b845c09565',
    'Lena': 'e600fa9c6de84de0a7cb',
    'Fischer': '10c72658d6a9403f92da',
    'SSC': 'fe850c8bc23441c79a92',
    'Little': '6151138be2e4429aa04c',
    'Wicker': '61bf5df089254c5fb929',
    'Kingston': 'dd5e452bb36d49928663',
    'Kobach': 'e38e22acff214f558aa7',
    'Rinaldi': 'c070928719ec409fbff8',
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
            #print(apiKey)
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
