#Main.py

import os
import csv

print("Financial Analysis")
print("----------------------------")

BD_csv = os.path.join("../", "budget_data.csv")

with open(BD_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   BD_csvheader = next(csvfile, None)

   Total = 0
   Total_Months = 0
   Increase = 0
   Decrease = 0

   first = True
   for row in csvreader:
      Total += int(row[1])
      Total_Months += 1
      
      if first:
         First = row[1]
         first = False
      Last = row[1]

      if (int(row[1]) > int(Increase)):  
         Increase = row[1]
         Increase_print = ("Greatest Increase in Profits: " + str(row[0]) 
         + " ($" + str(row[1]) + ")")
      if (int(row[1]) < int(Decrease)):  
         Decrease = row[1]
         Decrease_print = ("Greatest Decrease in Profits: " + str(row[0])
         + " ($" + str(row[1]) + ")")
   
   Change = (int(Last) - int(First)) / (Total_Months - 1)
   
   print("Total Months:" + str(Total_Months))
   print("Total: $" + str(Total))
   print("Average Change: $" + str("{0:.2f}".format(Change)))
   print(Increase_print)
   print(Decrease_print)

with open("budget_data.txt", "w") as text_file:
   print("Financial Analysis", file = text_file)
   print("----------------------------",file = text_file)
   print("Total Months:" + str(Total_Months), file = text_file)
   print("Total: $" + str(Total), file = text_file)
   print("Average Change: $" + str("{0:.2f}".format(Change)), 
   file = text_file)
   print(Increase_print, file = text_file)
   print(Decrease_print, file = text_file)