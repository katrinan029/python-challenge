# import os
# import csv

# budget_data = '../Resources/budget_data.csv'

# with open(budget_data, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csvheader = next(csvreader)
#     print(f'CSV HEADER: {csvheader}')
#     # csv_list = list(csvreader)
# current_profit = 0
# profit_date = ''

# for i in range(len(csv_list) - 1):
#     next_date = csv_list[i + 1][0]
#     current_item = csv_list[i][1]
#     next_item = csv_list[i + 1][1]
#     profit = int(next_item) - int(current_item)

#     if current_profit < profit:
#         current_profit = profit
#         profit_date = next_date

# print(current_profit)
# print(profit_date)

name = str(input("What's your name? "))
question = str(input(
    "Hi " + name + ". Do you understand Python while loops? \n(Enter yes or no?) "))

while question != "yes":
    message = input("Okay " + name + ", while loops in Python repeat as long as a certain Boolean condition is meet. \n" +
                    name + ", now do you unerstand Python while loops? \n(Enter yes or no?) ")

print("Congratulations " + name + " for understanding while loops!")
