import os
import csv

election_csv = os.path.join("..", "election_data.csv")

with open(election_csv, newline="") as electionfile:
    ereader = csv.reader(electionfile, delimiter=",")

    election_header = next(electionfile, None)

    Total_Votes = 0
    Khan_Votes = 0
    Correy_Votes = 0 
    Li_Votes = 0
    OTooley_Votes = 0

    for row in ereader:
        Total_Votes += 1
        if row[2] == "Khan":
            Khan_Votes += 1
        elif (row[2] == "Correy"):
            Correy_Votes += 1
        elif (row[2] == "Li"):
            Li_Votes += 1
        elif (row[2] == "O'Tooley"):
            OTooley_Votes += 1

Khan_Percentage = round(100 * Khan_Votes/Total_Votes, 3)
Correy_Percentage = round(100 * Correy_Votes/Total_Votes, 3)
Li_Percentage = round(100 * Li_Votes/Total_Votes, 3)
OTooley_Percentage = round(100 * OTooley_Votes/Total_Votes, 3)

candidates = {'Khan': Khan_Percentage, 'Correy': Correy_Percentage, 'Li': Li_Percentage, 'OTooley': OTooley_Percentage}
winner = max(candidates, key=candidates.get)

print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(Total_Votes))
print("-------------------------")
print("Khan: " +  str(Khan_Percentage) +"%  (" + str(Khan_Votes)+ ")")
print("Correy: " +  str(Correy_Percentage) +"%  (" + str(Correy_Votes)+ ")")
print("Li: " +  str(Li_Percentage) + "%  (" + str(Li_Votes)+ ")")
print("OTooley: " +  str(OTooley_Percentage) +"%  (" + str(Khan_Votes)+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

with open("elecation_data.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print("Total Votes: "+ str(Total_Votes), file = text_file)
    print("-------------------------", file = text_file)
    print("Khan: " +  str(Khan_Percentage) +"%  (" + str(Khan_Votes)+ ")", file = text_file)
    print("Correy: " +  str(Correy_Percentage) +"%  (" + str(Correy_Votes)+ ")", file = text_file)
    print("Li: " +  str(Li_Percentage) + "%  (" + str(Li_Votes)+ ")", file = text_file)
    print("OTooley: " +  str(OTooley_Percentage) +"%  (" + str(Khan_Votes)+ ")", file = text_file)
    print("-------------------------", file = text_file)
    print("Winner: " + winner, file = text_file)
    print("-------------------------", file = text_file)