import os
import csv

budget_data = '../Resources/budget_data.csv'

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f'CSV HEADER: {csvheader}')

    months = 0
    profit_loses = 0
    greatest_increase = 0
    greatest_decrease = 0

    # sum the total number of months in dataset
    for row in csvreader:
        months = months + 1
        profit = int(row[1])

    # calculate net total amount of "Profit/Losses"
        profit_loses = profit_loses + profit

    # calculate net total amount of "Profit/Losses"
    average = profit_loses / months

    print("Financial Analysis")
    print("-"*64)
    print(f'Total Months: {months}')
    print(f'Total: ${profit_loses}')
    print(average)
