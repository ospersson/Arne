import json
import sys

filePath = sys.argv[1]
print('Open file: {0}'.format(filePath))

with open(filePath) as data_file:    
    data = json.load(data_file)

# Calculates the Compound Annual Growth Rate(CAGR).
def cagr(firstValue, lastValue, year):
    return (lastValue/firstValue)**(1/year)-1

# Calculate dividend YoY(Year over year growth).
def dividendYoYGrowth(dividendPrevYear, dividen, yearStr):
    dividendStr = str(dividend)

    if dividendPrevYear > 0:
        dividendYoY = round(((dividend / dividendPrevYear) - 1) * 100, 1)
        dividendYoYStr = str(dividendYoY) + " %"
    else:
        dividendYoYStr = "-"

    print(yearStr + " \t" + str(dividendStr) + "\t\t" + str(dividendYoYStr))

# Prints the CAGR(year) xx.x%
def printCAGRPercent(dividendList, year = 0):

    minNoElements = 0
    maxNoElements = len(dividendList)

    if year > 0:
        minNoElements = maxNoElements - year - 1
        noOfYear = year
    else:
        noOfYear = maxNoElements

    cagrStr = str(round(cagr(dividendList[minNoElements], dividendList[maxNoElements -1], noOfYear) * 100, 1))
    print("\nCAGR(" + str(noOfYear) + "): " + cagrStr + " %")
    
print(data['name'] + "\n")
print("Year:" +  "\t" +  "Dividend:" + "\t" + "YoY Growth:")

dividendPrevYear = 0.0
dividendList = []

for year in data['keyDataPerShareYear']:
    yearStr = str(year['year'])
    dividend = year['cashDividend']
    
    dividendYoYGrowth(dividendPrevYear, dividend, yearStr)

    dividendPrevYear = dividend
    dividendList.append(dividend)

printCAGRPercent(dividendList)
printCAGRPercent(dividendList, 5)


