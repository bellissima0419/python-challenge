import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')

profit_loss = []
profits = []
losses = []
p_count = 0
l_count = 0
balance = 0
months = []

with open(csvpath, newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  csv_header = next(csvfile)
  print(f"Header: {csv_header}")


  for row in csvreader:
    balance += int(row[1])
    months.append(row[0].split("-"))
    if int(row[1]) > 0:
     profits.append(int(row[1]))
    else:
      losses.append(int(row[1]))



  print(f"banance: {balance}")
  print(f"len(months) {len(months)}")
  print(f"profits sum: {sum(profits)}")
  print(f"losses:  {sum(losses)}")
  print(f"balance: {sum(profits) + sum(losses)} ")


#     if int(row[1]) > 0:
#       # print( int( row[1]) )
#       profits.append(int(row[1]))
#       p_count += int(row[1])
#     else:
#       losses.append(row[1])
#       l_count += int(row[1])


# print(f"profits:  {profits} ")
# print()
# print("======================")
# print(f"losses:  {losses} ")
# print()
# print(f"len(profit_loss): {len(losses)}")
# print("======================")
# print("======================")

# print(f"profits: {[profit for profit in profit_loss if profit > 0]}")

