import csv
import os

csvpath = os.path.join('../', 'budget_data.csv')
profit_and_losses = []
profit_loss_diff = []
balance = 0
months = []
csv_list = []

with open(csvpath, 'r', newline='') as csvfile:

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

# print(f"months: {months}")
for i in range(1, len(csv_list)):
        # calculate the  profit change and append it along with its  month
    profit_loss_diff.append(
        [csv_list[i][0], csv_list[i][1] - csv_list[i - 1][1]])

# calculate the max increase in profits. Calculation made with lambda on
# second item on the profit_loss_diff list, thus creating a list that
# contains both the month the year and the amount
greatest_profit_increase = max(profit_loss_diff, key=lambda x: x[1])
# print(f"greatest_profit_increase: {greatest_profit_increase}")
# calculate the max decrease in profits
greatest_profit_decrease = min(profit_loss_diff, key=lambda x: x[1])
# print(f"greatest_profit_decrease: {greatest_profit_decrease}")
# calculate the average in profit change
avg = round(sum([x[1] for x in profit_loss_diff]) / len(profit_loss_diff), 2)

# Create the summary of the Financial Analysis
summary = {
    "title": "Financial Analysis",
    "underline": "-------------------------------------------------",
    "Total Months": f"{len(months)}",
    "Total": f"${balance}",
    "Average Change": f"${avg}",
    "Greatest Increase in Profits": f"{greatest_profit_increase[0]} ({greatest_profit_increase[1]})",
    "Greatest Decrease in Profits": f"{greatest_profit_decrease[0]} ({greatest_profit_decrease[1]})"
}

# function that prints the report to the terminal
def financial_analysis(dict):
    print()
    for k, v in dict.items():
        if k == "title" or k == "underline":
            print(v)
        else:
            print(f"{k}: {v}")

# run the function that prints report to the terminal
financial_analysis(summary)
# terminal print out matches the homework README

# Financial Analysis
# -------------------------------------------------
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 (1926159)
# Greatest Decrease in Profits: Sep-2013 (-2196167)

# Open/create file in "write" mode ('w') and add the summary(analysis) to it
file1 = './FinancialAnalysis.txt'
with open(file1, 'w') as text:
    for k, v in summary.items():
        if k == "title" or k == "underline":
            text.writelines([v, "\n"])
        else:
            text.writelines([k,":", " ", v, "\n"])


