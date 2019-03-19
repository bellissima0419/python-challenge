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

# calculate the max increase in profits. Calculation made with lambda on second item on the profit_loss_diff list, thus creating a list that contains both the month the year and the amount
greatest_profit_increase = max(profit_loss_diff, key=lambda x: x[1])

# print(f"greatest_profit_increase: {greatest_profit_increase}")

# calculate the max decrease in profits
greatest_profit_decrease = min(profit_loss_diff, key=lambda x: x[1])
# calculate the average in profit change
avg = round(sum([x[1] for x in profit_loss_diff]) / len(profit_loss_diff), 2)

# Create the summary of the Financial Analysis
summary = {
  "title": "Financial Analysis",
  "underline": "-------------------------------------------------",
  "Total Months": f":{len(months)}",
  "Total": f"${balance}",
  "Average Change": f"${avg}",
  "Greatest Increase in Profits": f"{greatest_profit_increase[0]}: {greatest_profit_increase[1]}",
  "Greatest Decrease in Profits": f"{greatest_profit_decrease[0]}: {greatest_profit_decrease[1]}"
}


# FinancialAnalysis = "Financial Analysis"
# underline = "-------------------------------------------------"
# total_months = f"Total Months: {len(months)}"
# total = f"Total: ${balance}"
# avg_change = f"Average Change: ${avg}"
# greatest_inc_prof = f"Greatest Increase in Profits: {greatest_profit_increase[0]} ({greatest_profit_increase[1]})"
# greatest_dec_prof = f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} ({greatest_profit_decrease[1]})"

# summary = [FinancialAnalysis, underline, total_months, total, avg_change,
#            greatest_inc_prof, greatest_dec_prof]


def financial_analysis(dict):
    for k,v in dict.items():
      if k == "title" or k == "underline":
        print(v)
      else: print(k,v)

# print("summary length", len(summary))

financial_analysis(summary)



# Open/create file in "write" mode ('w') and add the summary(analysis) to it
file1 = './FinancialAnalysis.txt'
with open(file1, 'w') as text:
  for k, v in summary.items():
      if k == "title" or k == "underline":
        text.writelines([v, "\n"])
      else: text.writelines([k,v, "\n"])

# file2 = './FinancialAnalysis.csv'
# with open(file2, 'w') as csv_file:

#   for k, v in summary.items():
#     if k == "title" or k == "underline":
#         csv_file.writelines([v, "\n"])
#     else: csv_file.writelines([k,v, "\n"])
