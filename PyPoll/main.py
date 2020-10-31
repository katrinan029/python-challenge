import os
import csv

election_data = '../Resources/election_data.csv'

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # setting counter to 0
    total_votes = 0
    # assigning candidate list as set
    candidates_list = set()
    percentage_votes = 0.00
    winnning_count = 0
    winner = ""
    votes = {}

    for row in csvreader:
        # count total number of votes cast per row
        total_votes += 1
        # log candidates in each row
        candidates = row[2]

        # votes for each candidate
        if candidates not in votes:
            votes[candidates] = 1

        else:
            votes[candidates] += 1

        # count the greatest number of votes for each candiate
        for candidate in votes:
            if votes[candidates] > winnning_count:
                winnning_count = votes[candidates]
                winner = candidate

        # A complete list of candidates who received votes
        candidates_list.add(candidates)

    # print to terminal
    print("Election Results")
    print('-'*64)
    print(f'Total votes {total_votes:,.0f}')
    print('-'*64)

    for candidates in votes:
        fstring = f'{candidates}: %{votes[candidates] / total_votes * 100:,.3f} ({votes[candidates]:,.0f})'
        print(fstring)

    print('-'*64)
    print(f'Winner: {winner}')
    print('-'*64)

# print to text file
with open("./analysis.txt", "w+") as analysis:
    total_votes_string = f'Total votes {total_votes:,.0f}'
    winner = f'Winner: {winner}'
    analysis.write(f'Election Results\n')
    analysis.write(f'{"-" * 64}\n')
    analysis.write(f'{total_votes_string}\n')
    analysis.write(f'{"-" * 64}\n')
    for candidates in votes:
        analysis.write(
            f'{candidates}: %{votes[candidates] / total_votes * 100:,.3f} ({votes[candidates]:,.0f})\n')
    analysis.write(f'{"-" * 64}\n')
    analysis.write(f'{winner}\n')
    analysis.write(f'{"-" * 64}\n')
