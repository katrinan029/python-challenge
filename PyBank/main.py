import os
import csv

budget_data = '../Resources/budget_data.csv'

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    months = 0
    profit_loses = 0
    greatest_increase = -999999999
    greatest_decrease = 999999999
    net_profit = 0

    # skip the first months data
    first_row = next(csvreader)

    # set initial values
    last_profit = int(first_row[1])
    total_profit = int(first_row[1])
    greatest_month = first_row[0]
    worst_month = first_row[0]

    # loop thru remaining months and begin calculating new values
    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        net = profit - last_profit

        if net > greatest_increase:
            greatest_increase = net
            greatest_month = month

        if net < greatest_decrease:
            greatest_decrease = net
            worst_month = month

        last_profit = profit
        total_profit = profit + total_profit
        net_profit += net
        months += 1

    average = net_profit / months

    print("Financial Analysis")
    print("-"*64)
    print(f'Total Months: {months+1}')  # adding 1 to capture first month
    print(f'Total: ${total_profit:,.2f}')
    print(f'Average Change: ${average:,.2f}')
    print(
        f'Greatest Increase in Profits: {greatest_month} ${greatest_increase:,.2f}')
    print(
        f'Greatest Decrease in Profits: {worst_month} ${greatest_decrease:,.2f}')

    financial_analysis = "Financial Analysis"
    total_months = f'Total Months: {months+1}'
    total_profit = f'Total: ${total_profit:,.2f}'
    average_change = f'Average Change: ${average:,.2f}'
    greatest_increase = f'Greatest Increase in Profits: {greatest_month} ${greatest_increase:,.2f}'
    greatest_decrease = f'Greatest Decrease in Profits: {worst_month} ${greatest_decrease:,.2f}'

# exporting results to text file in the same directory
with open("./analysis.txt", "w+") as analysis:
    analysis.write(f'{financial_analysis}\n')
    analysis.write(f'{"-" * 64}\n')
    analysis.write(f'{total_months}\n')
    analysis.write(f'{total_profit}\n')
    analysis.write(f'{average_change}\n')
    analysis.write(f'{greatest_increase}\n')
    analysis.write(f'{greatest_decrease}\n')
