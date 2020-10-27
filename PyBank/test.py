import os
import csv

budget_data = './Resources/budget_data.csv'

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f'CSV HEADER: {csvheader}')
    csv_list = list(csvreader)
    c = 0
    d = ''

    for i in range(len(csv_list) - 1):
        next_date = csv_list[i + 1][0]
        current_item = csv_list[i][1]
        next_item = csv_list[i + 1][1]
        profit = int(next_item) - int(current_item)

        if c < profit:
            c = profit
            d = next_date

    print(c)
    print(d)
    # print(current_item)
    # print(next_item)
    # print('-----')
