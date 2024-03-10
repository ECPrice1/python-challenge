# Tips for how to open and link the CSV referenced from class exercise 08-Ins_ReadCSV
#Import necessary modules
#import os allows us to create file paths across operating systems
import os

#import csv module allows for reading CSV files
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#print(csvpath)
#print(os.path.isfile(csvpath))
#these commented commands help to check that the path is correct

with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    #Read the header row first
    #print(f"CSV Header: {csv_header}")
    
    #skip header row
    csv_header = next(csvreader)

#Establishing some initial variables    
    mo_count = 0
    total_pl = 0
    net_change_tot = 0
    prev_month = 0
    mo_change = 0
    greatest_increase = 0
    gi_mo = None
    greatest_decrease = 0
    gd_mo = None
### =+ , SAME AS monthly_change = monthly_change + net_change

# Read each row of data after the header   
    for row in csvreader:
        #print(row)
        mo_count += 1
        total_pl += int(row[1])
        
        if prev_month != 0:
            mo_change = int(row[1]) - prev_month
            net_change_tot += mo_change
            prev_month = int(row[1])
            if mo_change > greatest_increase:
                    greatest_increase = mo_change
                    gi_mo = row[0]
            if mo_change < greatest_decrease:
                    greatest_decrease = mo_change
                    gd_mo = row[0]

        elif prev_month == 0:
            prev_month = int(row[1])

#print values
print("Financial Analysis")
print(" ")
print("-------------------------------")
print(" ")
print(f"Total months: {mo_count}")
print(" ")
print(f"Total: ${total_pl}")
print(" ")
## format this to 2 decimal places
#https://www.javatpoint.com/how-to-get-2-decimal-places-in-python
print(f"Average change: ${format(net_change_tot/(mo_count-1), ".2f")}")
print(" ")
print(f"Greatest increase in profits: {gi_mo} (${greatest_increase})")
print(" ")
print(f"Greatest decrease in profits: {gd_mo} (${greatest_decrease})")

#Still need to export .txt file
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#used this for help in exporting .txt
bankfile = open("PyBank.txt", 'w')

line1 = ("Financial Analysis")
line2 = "\n"
line3 = ("-------------------------------------------------")
line4 = "\n"
line5 = (f"Total months: {mo_count}")
line6 = "\n"
line7 = (f"Total: ${total_pl}")
line8 = "\n"
line9 = (f"Average change: ${format(net_change_tot/(mo_count-1), ".2f")}")
line10 = "\n"
line11 = (f"Greatest increase in profits: {gi_mo} (${greatest_increase})")
line12 = "\n"
line13 = (f"Greatest decrease in profits: {gd_mo} (${greatest_decrease})")


bankfile.write(line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 + line12 + line13) 
