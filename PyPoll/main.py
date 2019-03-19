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

    # print(f"Header: {csv_header}")

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

def poll_results(dict):
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {dict['total_votes']}")
    print("-------------------------")

    for k, v in dict["percentages"].items():
        # if dict[i] == "percentages":
        print(f"{k}: {v}% ({dict['votes_per_candidate'][k]})")
    print("-------------------------")
    print(f"Winner: {dict['winner']}")
    print("-------------------------")
        # print(k,":", v, "%")
        # for j in i:
        #     print(dict[i][j])

            # print(f"k: {k} v: {v}")

            # for candidate, percentage in k.items():
            #     print(f"{candidate}: {percentage}% ")
    print()

poll_results(election_results)


# print(f"election_results: {election_results}")
# print()
# for (k, v) in election_results.items():

#     print(f"{k}: {v}")
#     # print(f"election_results: {election_results}")











# import csv
# import os

# csvpath = os.path.join('./', 'election_data.csv')

# # set variables
# total_votes = 0
# candidate_set = set()
# list_of_candidates = []
# votes_per_candidate = {"candidates": {}}
# candidates = []
# # candidates = ["khan": {votes: 0, percentage:0}]
# winner  = ""
# election_results = {}
# percentages = {}

# with open(csvpath, newline='') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvfile)
#     # csv_toList = list(csvreader) IF UNCOMMENTED CODE BREAKS!!!It doesn't after for loops
#     # print(f"len(list(csvreader)): {len(list(csvreader))}") IF UNCOMMENTED CODE BREAKS!!!It doesn't after for loops

#     # print(f"Header: {csv_header}")

#     for row in csvreader:
#         candidate_set.add(row[2])

#         # check if all rows have a voter id to avoid giving a candidate a vote only based on a row count.
#         if row[0]: total_votes += 1

#         # build a dictionary with the candidate name and a counter
#         # if the candidate already exists in the dictionary add 1 to the counter,
#         # if not, set the counter = 1
#         # if votes_per_candidate["candidates"][row[2]]["votes"]:
#         votes_per_candidate["candidates"][row[2]]["votes"] += 1 | 1
#             # if votes_per_candidate[row[2]]["votes"]:
#             #     votes_per_candidate[row[2]]["votes"] += 1
#         # else:
#         #     votes_per_candidate["candidates"][row[2]]["votes"] = 1

#     # calculate the average of votes per candidate adding this data to a new dictionary
#     # for candidate, votes in votes_per_candidate.items():
#     #     # votes_per_candidate[candidate]["percentage"] =  round((votes/total_votes)*100, 2)
#     #     votes_per_candidate[candidate]["percentage"] =  round((votes_per_candidate[candidate]["votes"]/total_votes)*100, 2)

#     print(f"votes_per_candidate: {votes_per_candidate}")

#     # lambda to calculate the winner with a max function performed on the numeric v of votes in the dictionary
#     # winner = max(votes_per_candidate, key=lambda x: votes_per_candidate["candidate"]["votes"][x])

#     # update the election_results dictionary
#     # election_results["title"] = "Election Results"
#     # election_results["underline"] = "-------------------------------------------------"
#     # election_results["total_votes"] = total_votes
#     # election_results["candidate_set"] = candidate_set
#     # election_results["votes_per_candidate"] = votes_per_candidate
#     # election_results["percentages"] = percentages
#     # election_results["winner"] = winner
#     # print(f"election_results: {election_results}")

# # for (k, v) in election_results.items():
# #     print(f"{k}: {v}")

# # Election Results
# # -------------------------
# # Total Votes: 3521001
# # -------------------------
# # Khan: 63.000% (2218231)
# # Correy: 20.000% (704200)
# # Li: 14.000% (492940)
# # O'Tooley: 3.000% (105630)
# # -------------------------
# # Winner: Khan
# # -------------------------

# def poll_results(dict):
#     print("Election Results")
#     print("-------------------------")
#     print(f"Total Votes: {dict["total_votes"]} ")
#     print("-------------------------")
#     for key, val in dict.items():
#         if key == "percentages":
#             for candidate, percentage in key.items():
#                 print(f"{candidate}: {percentage}% ")
#         print()





# # ==========================================================================================

#     # DOES NOT WORK WITH NUMERIC INDEX FOR EACH ROW IN THE CSV FILE!!!!
#     # for i in range(20):
#     #     candidate_set.add(csvreader[i][2])
#     #     if csvreader[i][2] in votes_per_candidate:
#     #         votes_per_candidate[csvreader[i][2]] = votes_per_candidate[csvreader[i][2]] + 1
#     #     else:
#     #         votes_per_candidate[csvreader[i][2]] = 1

