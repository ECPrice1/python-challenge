#Importing necessary modules
import os
import csv

#Establishing path to csv file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#Opening csv file
with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skipping csv header row
    csv_header = next(csvreader)

    #Establishing some initial variables 
    total_votes = 0
    winner = 0

    #List of dictionaries with name and votes for each candidate.
    candidate_list = [
        {'name': 'Charles Casper Stockham', 'votes': 0},
        {'name': 'Diana DeGette', 'votes': 0},
        {'name': 'Raymon Anthony Doane', 'votes': 0}
    ]

    #Read each row of data after the header  
    for row in csvreader:
        #Counting "Total votes"
        total_votes += 1
        
        #Counting votes for candidates, storing results
        if row[2] == candidate_list[0]['name']:
            candidate_list[0]['votes'] += 1

        if row[2] == candidate_list[1]['name']:
            candidate_list[1]['votes'] += 1
            
        if row[2] == candidate_list[2]['name']:
            candidate_list[2]['votes'] += 1

   
    #Comparing results to determine winner
    if candidate_list[0]['votes'] > candidate_list[1]['votes'] and candidate_list[2]['votes']:
        winner = candidate_list[0]['name']
    if candidate_list[1]['votes'] > candidate_list[0]['votes'] and candidate_list[2]['votes']:
        winner = candidate_list[1]['name']
    if candidate_list[2]['votes'] > candidate_list[0]['votes'] and candidate_list[1]['votes']:
        winner = candidate_list[2]['name']


    #Calculating percentage of votes and creating output for candidate name, percentage of votes won and candidate total votes
    def output(candidate):
        output = f'{candidate['name']}: {format(((candidate['votes']/ total_votes)*100), ".2f")}%, ({candidate['votes']})'
        print(output)

#Print results
print("Election results")
print("")
print("-------------------------------------------------")
print("")
print(f"Total votes: {total_votes}")
print("")
print("-------------------------------------------------")
print("")
output(candidate_list[0])
print("")
output(candidate_list[1])
print("")
output(candidate_list[2])
print("-------------------------------------------------")
print("")
print(f'Winner: {winner}')
print("")
print("------------------------------------------------")

#Exporting results to .txt
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

pollfile = open("PyPoll.txt", 'w')

line1 = ("Election results")
line2 = "\n"
line3 = ("-------------------------------------------------")
line4 = "\n"
line5 = "\n"
line6 = (f"Total votes: {total_votes}")
line7 = "\n"
line8 = "\n"
line9 = ("-------------------------------------------------")
line10 = "\n"
line11 = "\n"
line12 = (f'{candidate_list[0]['name']}: {format(((candidate_list[0]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[0]['votes']})')
line13 = "\n"
line14 = "\n"
line15 = (f'{candidate_list[1]['name']}: {format(((candidate_list[1]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[1]['votes']})')
line16 = "\n"
line17 = "\n"
line18 = (f'{candidate_list[2]['name']}: {format(((candidate_list[2]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[2]['votes']})')
line19 = "\n"
line20 = "\n"
line21 = ("-------------------------------------------------")
line22 = "\n"
line23 = "\n"
line24 = (f'Winner: {winner}')
line25 = "\n"
line26 = "\n"
line27 = ("------------------------------------------------")

pollfile.write(line1+
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
               line17+
               line18+
               line19+
               line20+
               line21+
               line22+
               line23+
               line24+
               line25+
               line26+
               line27
) 

