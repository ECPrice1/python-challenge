import os

# Module for reading CSV files
import csv



csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#print(csvpath)
#print(os.path.isfile(csvpath))

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    #Read the header row first
    #print(f"CSV Header: {csv_header}")

    #skip header row
    csv_header = next(csvreader)

    total_votes = 0
    candidate_list = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    candidate_votes = [0, 0, 0]
    winner = 0


    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            #print(candidate_list)
            #this piece of code was initially used to read through the entire file to determine the number of candidates and their names

        if row[2] == candidate_list[0]:
            candidate_votes[0] += 1
            
        if row[2] == candidate_list[1]:
            candidate_votes[1] += 1
            
        if row[2] == candidate_list[2]:
            candidate_votes[2] += 1
        


    if candidate_votes[0] > 0:
        winner = 'Charles Casper Stockham'
    if candidate_votes[1] > candidate_votes[0]:
        winner = 'Diana DeGette'
    if candidate_votes[2] > candidate_votes[1] and candidate_votes[0]:
        winner = 'Raymon Anthony Doane'
    #print(winner)


       

    

print("Election results")
print("")
print("-------------------------------------------------")
print("")
print(f"Total votes: {total_votes}")
print("")
print("-------------------------------------------------")
print("")
print(f'{candidate_list[0]}: {format(((candidate_votes[0]/ total_votes)*100), ".2f")}%, ({candidate_votes[0]})')
print("")
print(f'{candidate_list[1]}: {format(((candidate_votes[1]/ total_votes)*100), ".2f")}%, ({candidate_votes[1]})')
print("")
print(f'{candidate_list[2]}: {format(((candidate_votes[2]/ total_votes)*100), ".2f")}%, ({candidate_votes[2]})')
print("-------------------------------------------------")
print("")
print(f'Winner: {winner}')
print("")
print("------------------------------------------------")

#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#used this for help in exporting .txt
pollfile = open("PyPoll.txt", 'w')

line1 = ("Election results")
line2 = "\n"
line3 = ("-------------------------------------------------")
line4 = "\n"
line5 = (f"Total votes: {total_votes}")
line6 = "\n"
line7 = ("-------------------------------------------------")
line8 = "\n"
line9 = (f'{candidate_list[0]}: {format(((candidate_votes[0]/ total_votes)*100), ".2f")}%, ({candidate_votes[0]})') 
line10 = "\n"
line11 = "\n"
line12 = (f'{candidate_list[1]}: {format(((candidate_votes[1]/ total_votes)*100), ".2f")}%, ({candidate_votes[1]})')
line13= "\n"
line14 = "\n"
line15 = (f'{candidate_list[2]}: {format(((candidate_votes[2]/ total_votes)*100), ".2f")}%, ({candidate_votes[2]})')
line16 = "\n"
line17 = ("-------------------------------------------------")
line18 = "\n"
line19 = (f'Winner: {winner}')
line20 = "\n"
line21 = ("------------------------------------------------")

pollfile.write(line1 + 
               line2 + 
               line3 + 
               line4 + 
               line5 + 
               line6 + 
               line7 + 
               line8 + 
               line9 +
               line10 + 
               line11 + 
               line12 +
               line13 + 
               line14 + 
               line15 + 
               line16 + 
               line17 + 
               line18 + 
               line19 + 
               line20 + 
               line21) 

