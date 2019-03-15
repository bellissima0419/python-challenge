import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')
profit_and_losses = []
profit_loss_diff = []
balance = 0
months = []
# csv_list = []

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvfile)

  # cast the file into a python list making the ProfitLoses an int
  csv_list = [[row[0], int(row[1])] for row in csvreader]
  print(f"Header: {csv_header}")

  print(f"csv_list: {csv_list[:5]}")


  for row in csvreader:

    profit_and_losses.append(int(row[1]))
    balance += int(row[1])
    months.append(row[0].split("-"))


for i in range(1, len(csv_list)):

    profit_loss_diff.append([csv_list[i][0], csv_list[i][1] - csv_list[i-1][1]])
    # print(profit_loss_diff)
print(profit_loss_diff[:5])
# print(max(profit_loss_diff[1]))

greatest_profit_increase = max(csv_list, key=lambda x: x[1])
greatest_profit_decrease = min(csv_list, key=lambda x: x[1])


avg = round(sum([x[1] for x in profit_loss_diff])/len(profit_loss_diff),2)

print('avg', {avg})
print(f"(greatest_profit_increase): {(greatest_profit_increase)}")
print(f"greatest_profit_decrease: {greatest_profit_decrease}")
# print(f"avg: {avg}")



# print([max(row[1]) for row in profit_loss_diff if  ])
# for i in range(len(profit_and_losses)-1):
#   profit_loss_diff.append(profit_and_losses[i+1] - profit_and_losses[i])

# print(f"profit_loss_diff: {profit_loss_diff[:-1]}")
# print(len(profit_loss_diff))
# print(f"csv_list: {(csv_list)}")
# print(f"csv_list: {len(csv_list)}")


# ========================================================
# ========================================================

# avg = round(sum(profit_loss_diff)/len(profit_loss_diff),2)
# # greatest_increase_profits = max(profit_loss_diff)
# # greatest_decrease_profits = min(profit_loss_diff)
# total  = sum(profit_and_losses)

# def financial_report(*args):
#   print("Financial Analysis")
#   print("--------------------------")
#   print(f"Total Months: {len(months)} ")
#   print(f"Total: ${total}")
#   print(f"Average Change: ${avg}")
#   print(f"Gratest Increase in Profits: (${greatest_profit_increase})")
#   print(f"Greatest Decrease in Profits: (${greatest_profit_decrease})")

# financial_report(months, total, avg, greatest_profit_increase, greatest_profit_decrease)

