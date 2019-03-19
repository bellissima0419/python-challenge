import csv
import os

csvpath = os.path.join('./', 'election_data.csv')

total_votes = 0
candidate_set = set()
list_of_candidates = []
votes_per_candidate = {}
winner  = ""
election_results = {}
percentages = {}

# votes_per_candidate =  {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
# list_of_candidates = ['Correy', 'Li', 'Khan', "O'Tooley"]

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # csv_toList = list(csvreader) IF UNCOMMENTED CODE BREAKS!!!
    # print(f"len(list(csvreader)): {len(list(csvreader))}") IF UNCOMMENTED CODE BREAKS!!!

    print(f"Header: {csv_header}")

    for row in csvreader:
        candidate_set.add(row[2])
        if row[0]: total_votes += 1

        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        else:
            votes_per_candidate[row[2]] = 1

    for candidate, votes in votes_per_candidate.items():
        percentages[candidate] =  round((votes/total_votes)*100, 2)

    # csv_toList = list(csvreader)
    # print(f"type of csvreader: {csvreader}")

    # print(f"candidate_set: {candidate_set}")
    # list_of_candidates = list(candidate_set)
    # print(f"list_of_candidates: {list_of_candidates}")

    winner = max(votes_per_candidate, key=lambda x: votes_per_candidate[x])

    election_results["total_votes"] = total_votes
    election_results["candidate_set"] = candidate_set
    election_results["votes_per_candidate"] = votes_per_candidate
    election_results["percentages"] = percentages
    # election_results["list_of_candidates"] = list_of_candidates
    # for k, v  in election_results["votes_per_candidate"].items():
    #     election_results["votes_per_candidate"]["percentage"] =
    # election_results["votes_per_candidate"]["percentage"] = votes_per_candidate
    election_results["winner"] = winner

    # print(f"election_results: {election_results}")

for (k, v) in election_results.items():

    print(f"{k}: {v}")
    # print(f"election_results: {election_results}")












    # DOES NOT WORK WITH NUMERIC INDEX FOR EACH ROW IN THE CSV FILE!!!!
    # for i in range(20):
    #     candidate_set.add(csvreader[i][2])
    #     if csvreader[i][2] in votes_per_candidate:
    #         votes_per_candidate[csvreader[i][2]] = votes_per_candidate[csvreader[i][2]] + 1
    #     else:
    #         votes_per_candidate[csvreader[i][2]] = 1

