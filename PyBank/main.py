import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')

profit_loss = []
pl_difference = []
profits = []
losses = []
p_count = 0
l_count = 0
balance = 0
months = []
csv_list = []

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvfile)

  # csv_list.append(list(csvreader))
  print(f"Header: {csv_header}")

  for row in csvreader:
    profit_loss.append(int(row[1]))
    # difference.append(row[1])
    balance += int(row[1])

    months.append(row[0].split("-"))
    if int(row[1]) > 0:
     profits.append(int(row[1]))
    else:
      losses.append(int(row[1]))


for i in range(len(profit_loss)-1):
  pl_difference.append(profit_loss[i+1] - profit_loss[i])

print()

pl_sum = 0
for i in range(len(pl_difference)):
  pl_sum += pl_difference[i]

print(f"pl_sum: {pl_sum}")
print(f"len( pl_difference ) {len(pl_difference)}")
print(f"avg: {sum(pl_difference)/len(pl_difference)}" )

print(f"max pl_difference: {max(pl_difference)}")
print(f"min pl_difference: {min(pl_difference)}")












