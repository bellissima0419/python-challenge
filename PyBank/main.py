import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')

profit_and_losses = []
profit_loss_diff = []
balance = 0
months = []

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvfile)

  print(f"Header: {csv_header}")

  for row in csvreader:
    profit_and_losses.append(int(row[1]))

    balance += int(row[1])

    months.append(row[0].split("-"))


for i in range(len(profit_and_losses)-1):
  profit_loss_diff.append(profit_and_losses[i+1] - profit_and_losses[i])

avg = round(sum(profit_loss_diff)/len(profit_loss_diff),2)
greatest_increase_profits = max(profit_loss_diff)
greatest_decrease_profits = min(profit_loss_diff)
total  = sum(profit_and_losses)

def financial_report(*args):
  print("Financial Analysis")
  print("--------------------------")
  print(f"Total Months: {len(months)} ")
  print(f"Total: ${total}")
  print(f"Average Change: ${avg}")
  print(f"Gratest Increase in Profits: (${greatest_increase_profits})")
  print(f"Greatest Decrease in Profits: (${greatest_decrease_profits})")

financial_report(months, total, avg, greatest_increase_profits, greatest_decrease_profits)

