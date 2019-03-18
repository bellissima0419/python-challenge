import csv
import os

csvpath = os.path.join('./', 'election_data.csv')

total_votes = 0
canidate_set = set()
list_of_candidates = []
votes_per_candidate = {}
election_winner  = ""

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        canidate_set.add(row[2])
        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        else:
            votes_per_candidate[row[2]] = 1


    print(f"votes_per_candidate: {votes_per_candidate}")
    list_of_candidates = list(canidate_set)
    print(f"list_of_candidates: {list_of_candidates}")


    # print(len(list(csvreader)[0:10]))

    # for i in range(20):
    #     canidate_set.add(csvreader[i][2])
    #     if csvreader[i][2] in votes_per_candidate:
    #         votes_per_candidate[csvreader[i][2]] = votes_per_candidate[csvreader[i][2]] + 1
    #     else:
    #         votes_per_candidate[csvreader[i][2]] = 1

