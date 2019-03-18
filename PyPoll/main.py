import csv
import os

csvpath = os.path.join('./', 'election_data.csv')

total_votes = 0
candidate_set = set()
list_of_candidates = []
votes_per_candidate = {}
winner  = ""

# votes_per_candidate =  {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
# list_of_candidates = ['Correy', 'Li', 'Khan', "O'Tooley"]

# winner = max(votes_per_candidate, key=lambda x: votes_per_candidate[x])

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        candidate_set.add(row[2])
        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        else:
            votes_per_candidate[row[2]] = 1

    print(f"candidate_set: {candidate_set}")

    winner = max(votes_per_candidate, key=lambda x: votes_per_candidate[x])

    print(f"Winner: {winner}")




    # print(len(list(csvreader)[0:10]))

    # for i in range(20):
    #     canidate_set.add(csvreader[i][2])
    #     if csvreader[i][2] in votes_per_candidate:
    #         votes_per_candidate[csvreader[i][2]] = votes_per_candidate[csvreader[i][2]] + 1
    #     else:
    #         votes_per_candidate[csvreader[i][2]] = 1

