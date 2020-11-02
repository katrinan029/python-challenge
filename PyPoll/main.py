# import os
# import csv

# election_data = '../Resources/election_data.csv'

# with open(election_data, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csvheader = next(csvreader)

#     print(list(csvreader))

name = str(input("What's your name? "))
question = str(input(
    "Hi " + name + ". Do you understand Python while loops? \n(Enter yes or no?) "))

while question != "yes":
    print("Okay " + name +
          ", while loops in Python repeat as long as a certain Boolean condition is meet.")
    question = input(
        name + ", now do you unerstand Python while loops? \n(Enter yes or no?) ")
print("Congratulations " + name + " for understanding while loops!")
