
#import the os and csv models
import os
import csv

#define the varibale we will be using
total_votes = 0
nominees = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

#set path
csv_poll = os.path.join("Resources","election_data.csv")
#open the data
with open(csv_poll) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

#identify the header
    poll_header = next(csvreader)
#for loop the data
    for row in csvreader:
#Total votes
        total_votes += 1
#calculate the votes for each nominee
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        elif (row[2] == "O'Tooley"):
            OTooley_votes += 1

#variables for nominess percents
        khan_per = 0
        correy_per = 0
        li_per = 0
        otooley_per = 0
#calculate the percentages of votes per nominee
        khan_per = Khan_votes / total_votes
        correy_per = Correy_votes / total_votes
        li_per = Li_votes / total_votes
        otooley_per = OTooley_votes/ total_votes
#Determine election winner
        winner = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)
        if winner == Khan_votes:
                winner_name = "Khan"
        elif winner == Correy_votes:
                winner_name = "Correy"
        elif winner == Li_votes:
                winner_name = "Li"
        elif winner == OTooley_votes:
                winner_name = "O'Tooley"

#Print the results
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
print(f"Khan:{khan_per:.3%},({Khan_votes})")
print(f"Correy:{correy_per:.3%},({Correy_votes})")
print(f"Li:{li_per:.3%},({Li_votes})")
print(f"O'Tooley:{otooley_per:.3%},({OTooley_votes})")
print("---------------------")
print(f"Winner: {winner_name}")

#set location of txt file
output = os.path.join("..", "Analysis")

with open(output, "w",) as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Khan:{khan_per:.3%},({Khan_votes})\n")
    txtfile.write(f"Correy:{correy_per:.3%},({Correy_votes})\n")
    txtfile.write(f"Li:{li_per:.3%},({Li_votes})\n")
    txtfile.write(f"O'Tooley:{otooley_per:.3%},({OTooley_votes})\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")

