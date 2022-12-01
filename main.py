# import csv # Imports the csv library

# with open("January.csv") as file: # Opens the csv file
#   reader = csv.reader(file) # reads the contents of the csv file into the 'reader' variable
#   line = 0

#   for row in reader: # loop to output each row in the 'reader' variable one at a time.
#     print (row)

# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) # Treats the file as a dictionary 
#   line = 0
#   for row in reader: 
#     print (row["Net Total"])


# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) # Treats the file as a dictionary 
#   line = 0
#   for row in reader: 
#     print (row["Net Total"])
#     total += float(row["Net Total"]) # Keeps a running total

# print(f"Total: {total}") #Outputs


# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
#   line = 0
  
#   for row in reader: 
#     print (row["Net Total"])
#     total += float(row["Net Total"])

# print(f"Total: {total}")


# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
 
  
#   for row in reader: 
#     print(row["Net Total"])
#     total += row["Net Total"] 

# print(f"Total: {total}")


# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
 
  
#   for row in reader: 
#     print (row["Net Total"]) # removed join
#     total += float(row["Net Total"] ) #cast to float

# print(f"Total: {total}")


import csv

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Cost"])

# print()

print(f"Total: ${total}")