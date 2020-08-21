
# First import the os and cvs modules allowing us to file paths across systems and to read csv files
import os
import csv

#define ou variables
total_months = 0
total_amount = 0
greatest_increase = 0
best_month = 0
greatest_decrease = 0
worst_month = 0
monthly_change =[]
month_count = []

csv_budget = os.path.join("..", "Resources", "budget_data.csv")

with open(csv_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Identify the header
    budget_header = next(csvreader)
    row = next(csvreader)

#set variables within the "with" function
    total_months += 1
    total_amount += int(row[1])
    previous_month = int(row[1])

    for row in csvreader:
        #calculate the total number of months
        total_months += 1
        #calculate the total amount of profits and losses
        total_amount += int(row[1])
        #calculate the changing from one month the the previous
        profit_change = int(row[1]) - previous_month
        monthly_change.append(profit_change)
        previous_month = int(row[1])
        #find the date and amount of the greatest increase of profits
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            best_month = row[0]
        #find the date and amount for the greatest decrease of profits
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            worst_month = row[0]





        worst = min(monthly_change)
        best = max(monthly_change)

    average_monthly_change = (sum(monthly_change) / len(monthly_change))
    average_monthly_change = round(average_monthly_change, 2)


print("Finacial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Amount: ${total_amount}")
print(f"Average Change: ${average_monthly_change:}")
print(f"Greatest Increase: {best_month}, (${best})")
print(f"Greatest Decrease: {worst_month}, (${worst})")

#set location of txt file
output = os.path.join(".", "PyBank", "Resources", "main.text")

with open(output, "w",) as txtfile:
    txtfile.write("Finacial Analysis")
    txtfile.write("----------------------")
    txtfile.write(f"Total Months: {total_months}")
    txtfile.write(f"Total Amount: ${total_amount}")
    txtfile.write(f"Average Change: ${average_monthly_change:}")
    txtfile.write(f"Greatest Increase: {best_month}, (${best})")
    txtfile.write(f"Greatest Decrease: {worst_month}, (${worst})")