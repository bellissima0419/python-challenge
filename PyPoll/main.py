import csv
import os

csvpath = os.path.join('./', 'election_data.csv')

total_votes = 0
candidate_set = set()
list_of_candidates = []
votes_per_candidate = {}
winner = ""
election_results = {}
percentages = {}

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        candidate_set.add(row[2])
        if row[0]:
            total_votes += 1

        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        else:
            votes_per_candidate[row[2]] = 1

    for candidate, votes in votes_per_candidate.items():
        percentages[candidate] = round((votes / total_votes) * 100, 2)

    winner = max(votes_per_candidate, key=lambda x: votes_per_candidate[x])

    election_results["total_votes"] = total_votes
    election_results["candidate_set"] = candidate_set
    election_results["votes_per_candidate"] = votes_per_candidate
    election_results["percentages"] = percentages
    election_results["winner"] = winner


def poll_results(dict):
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {dict['total_votes']}")
    print("-------------------------")

    for k, v in dict["percentages"].items():
        print(f"{k}: {v}% ({dict['votes_per_candidate'][k]})")
    print("-------------------------")
    print(f"Winner: {dict['winner']}")
    print("-------------------------")


poll_results(election_results)
