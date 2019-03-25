import os
import csv

cereal_csv = os.path.join("cereal.csv")

with open(cereal_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   csvheader = next(csvfile, None)
   print(f"Header: {csvheader}")

   for row in csvreader:
         if float(row[7]) >= 5:
            print(row)
