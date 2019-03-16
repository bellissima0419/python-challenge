import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')
profit_and_losses = []
profit_loss_diff = []
balance = 0
months = []
csv_list = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    for row in csvreader:

        profit_and_losses.append(int(row[1]))
        balance += int(row[1])
        # save the months into a list
        months.append(row[0].split("-"))
    # cast the file into a python list making the ProfitLoses an int
        csv_list.append([row[0], int(row[1])])


for i in range(1, len(csv_list)):
        # calculate the  profit change and append it along with its  month
    profit_loss_diff.append(
        [csv_list[i][0], csv_list[i][1] - csv_list[i - 1][1]])

# calculate the max increase in profits
greatest_profit_increase = max(profit_loss_diff, key=lambda x: x[1])
# calculate the max decrease in profits
greatest_profit_decrease = min(profit_loss_diff, key=lambda x: x[1])
# calculate the average in profit change
avg = round(sum([x[1] for x in profit_loss_diff]) / len(profit_loss_diff), 2)

# Print the summary of the Financial Analysis
print()
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {len(months)} ")
print(f"Total: ${balance}")
print(f"Average Change: ${avg}")
print(
    f"Greatest Increase in Profits: {greatest_profit_increase[0]} ({greatest_profit_increase[1]})")
print(
    f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} ({greatest_profit_decrease[1]})")
