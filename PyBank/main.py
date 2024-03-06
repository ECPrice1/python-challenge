# 08-Ins_ReadCSV
#First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv



csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#print(csvpath)
#print(os.path.isfile(csvpath))


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    mo_count = 0
    total_pl = 0
    greatest_increase = None
    gi_mo = None
    greatest_decrease = None
    gd_mo = None
    for row in csvreader:
        #print(row)
        mo_count = mo_count + 1
        total_pl = total_pl + int(row[1])

        if greatest_increase is None : 
            greatest_increase = int(row[1])
            gi_mo = row[0]
            #print(greatest_increase)
            #print statement confirmed this is working


        if greatest_decrease is None :
            greatest_decrease = int(row[1])
            gd_mo = row[0]
            #print(greatest_decrease)
            #print statement confirmed this is working
        
        if int(row[1]) > greatest_increase :
            greatest_increase = int(row[1])
            gi_mo = row[0]
            #print(f"Greatest increase {greatest_increase}, {gi_mo}")
            #print(gi_mo)

        if int(row[1]) < greatest_decrease :
            greatest_decrease = int(row[1])
            gd_mo = row[0]
            #print(f"Greatest decrease {greatest_decrease}, {gd_mo}")
            #print(gd_mo)


#print values
    print("Financial Analysis")
    print(" ")
    print("-------------------------------")
    print(" ")
    print(f"Total months: {mo_count}")
    print(" ")
    print(f"Total: ${total_pl}")
    print(" ")
    print("Average change: ***placeholder***")
    print(" ")
    print(f"Greatest increase in profits: {gi_mo} (${greatest_increase})")
    print(" ")
    print(f"Greatest decrease in profits: {gd_mo} (${greatest_decrease})")