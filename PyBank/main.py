#Import necessary modules
import os
import csv

#Establishing path to csv file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#Opening csv file
with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skipping csv header row
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

    #Read each row of data after the header   
    for row in csvreader:
        #Counting "Total months"
        mo_count += 1
        #Summing "Total"
        total_pl += int(row[1])
        
        #For each month, after the initial month, calculating the monthly change by subtracting prev month from current month
        if prev_month != 0:
            mo_change = int(row[1]) - prev_month
            net_change_tot += mo_change
            prev_month = int(row[1])
            #Establishing the "Greatest increase" value and capturing corresponding month
            if mo_change > greatest_increase:
                    greatest_increase = mo_change
                    gi_mo = row[0]
            #Establishing the "Greatest decrease" value and capturing corresponding month
            if mo_change < greatest_decrease:
                    greatest_decrease = mo_change
                    gd_mo = row[0]

        #This sets the prev_month variable for the first month
        elif prev_month == 0:
            prev_month = int(row[1])

#Print values
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

#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#used this for help in exporting .txt
bankfile = open("PyBank.txt", 'w')

line1 = ("Financial Analysis")
line2 = "\n"
line3 = ("-------------------------------------------------")
line4 = "\n"
line5 = (f"Total months: {mo_count}")
line6 = "\n"
line7 = "\n"
line8 = (f"Total: ${total_pl}")
line9 = "\n"
line10 = "\n"
line11 = (f"Average change: ${format(net_change_tot/(mo_count-1), ".2f")}")
line12 = "\n"
line13 = "\n"
line14 = (f"Greatest increase in profits: {gi_mo} (${greatest_increase})")
line15 = "\n"
line16 = "\n"
line17 = (f"Greatest decrease in profits: {gd_mo} (${greatest_decrease})")


bankfile.write(line1+
               line2+
               line3+
               line4+
               line5+
               line6+
               line7+
               line8+
               line9+
               line10+
               line11+
               line12+
               line13+
               line14+
               line15+
               line16+
               line17
) 
