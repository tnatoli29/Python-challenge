
# First import the os and cvs modules allowing us to file paths across systems and to read csv files
import os
import csv

csv_budget = os.path.join("..", "Resources", "budget_data.csv")

with open(csv_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    budget_header = next(csvreader)
    print(f"Budget Header: {budget_header}")

    for row in csvreader:
        print(row)