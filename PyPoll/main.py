from collections import Counter

candidates = {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}


totalVotes = [sum([v]) for k,v in candidates.items()]
print(f"totalVotes: {totalVotes}")
votes = Counter(candidates)

print(f"votes sum: {sum(votes)}")
print('Khan votes', votes['Khan'])
print(votes)
for k, v in votes.items():
    print(f"k,v: {k}: {v}")



git remote add origin git@github.com:bellissima0419/GTDATAGITLAB.git
git push -u origin master


# import csv
# import os

# csvpath = os.path.join('./', 'election_data.csv')

# total_votes = 0
# candidate_set = set()
# votes_per_candidate = {}
# winner = ""
# election_results = {}
# percentages = {}

# with open(csvpath, newline='') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvfile)

#     for row in csvreader:
#         candidate_set.add(row[2])
#         # check if all rows have a voter id to avoid giving a candidate a vote
#         # only based on a row count.
#         if len(row) == 3:
#             total_votes += 1

#         # build a dictionary with the candidate name and a counter
#         # if the candidate already exists in the dictionary add 1 to the counter,
#         # if not, set the counter = 1
#         if row[2] in votes_per_candidate:
#             # votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
#             votes_per_candidate[row[2]] += 1
#         else:
#             votes_per_candidate[row[2]] = 1

# # calculate the percentage of votes per candidate adding this data to a
# # new dictionary
# for candidate, votes in votes_per_candidate.items():
#     percentages[candidate] = round((votes / total_votes) * 100, 2)

# # lambda to calculate the winner with a max function performed on
# # thenumeric value of votes in the dictionary
# winner = max(votes_per_candidate, key=lambda x: votes_per_candidate[x])

# # update the election_results dictionary
# election_results["total_votes"] = total_votes
# election_results["candidate_set"] = candidate_set
# election_results["votes_per_candidate"] = votes_per_candidate
# election_results["percentages"] = percentages
# election_results["winner"] = winner


# # function to print the report to the terminal
# def poll_results(dict):
#     print()
#     print("Election Results")
#     print("-------------------------")
#     print(f"Total Votes: {dict['total_votes']}")
#     print("-------------------------")

#     for k, v in dict["percentages"].items():
#         print(f"{k}: {v}% ({dict['votes_per_candidate'][k]})")
#     print("-------------------------")
#     print(f"Winner: {dict['winner']}")
#     print("-------------------------")

# # data cleaning step 1: save relevant report data  into lists
# name = [k for k, v in election_results["votes_per_candidate"].items()]
# vote_count = [v for k, v in election_results["votes_per_candidate"].items()]
# vote_percentage = [v for k, v in election_results["percentages"].items()]

# # data cleaning step 2: zip the three lists to export them into csv file
# zipped = zip(name, vote_count, vote_percentage)

# # Open/create file in "write" mode ('w') and add the summary(analysis) to it
# output_file = os.path.join('poll_results.csv')
# with open(output_file, 'w', newline="") as datafile:

#     writer = csv.writer(datafile)
#     writer.writerow(["name", "vote_count", "vote_percentage"])
#     writer.writerows(zipped)

# poll_results(election_results)

# # =======================================================
# # print()
# # print(f"election_results: {election_results}")
# # print()
# # Election Results
# # -------------------------
# # Total Votes: 3521001
# # -------------------------
# # Khan: 63.0% (2218231)
# # Correy: 20.0% (704200)
# # Li: 14.0% (492940)
# # O'Tooley: 3.0% (105630)
# # -------------------------
# # Winner: Khan
# # -------------------------