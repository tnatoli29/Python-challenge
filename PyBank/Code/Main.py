
#First import the os and cvs modules allowing us to file paths across systems and to read csv files
import os
import csv

#This allows us to pull data from another file
budget_path = os.path.join("..", "Resources","budget_data.csv")

#CSV module
with open(budget_path) as csvfile:

    csvreader = csv.reader(csvfile)
    print(csvreader)

