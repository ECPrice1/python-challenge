import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    winner = 0

    candidate_list = [
        {'name': 'Charles Casper Stockham', 'votes': 0},
        {'name': 'Diana DeGette', 'votes': 0},
        {'name': 'Raymon Anthony Doane', 'votes': 0}
    ]

    for row in csvreader:
        total_votes += 1
        #if row[2] not in candidate_list:
            #candidate_list.append(row[2])
            #print(candidate_list)
            #this piece of code was initially used to read through the entire file to determine the number of candidates and their names
         
        if row[2] == candidate_list[0]['name']:
            candidate_list[0]['votes'] += 1

        if row[2] == candidate_list[1]['name']:
            candidate_list[1]['votes'] += 1
            
        if row[2] == candidate_list[2]['name']:
            candidate_list[2]['votes'] += 1

   
    if candidate_list[0]['votes'] > candidate_list[1]['votes'] and candidate_list[2]['votes']:
        winner = candidate_list[0]['name']
    if candidate_list[1]['votes'] > candidate_list[0]['votes'] and candidate_list[2]['votes']:
        winner = candidate_list[1]['name']
    if candidate_list[2]['votes'] > candidate_list[0]['votes'] and candidate_list[1]['votes']:
        winner = candidate_list[2]['name']


    def output(candidate):
        output = f'{candidate['name']}: {format(((candidate['votes']/ total_votes)*100), ".2f")}%, ({candidate['votes']})'
        print(output)

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
line9 = (f'{candidate_list[0]['name']}: {format(((candidate_list[0]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[0]['votes']})')
line10 = "\n"
line11 = "\n"
line12 = (f'{candidate_list[1]['name']}: {format(((candidate_list[1]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[1]['votes']})')
line13 = "\n"
line14 = "\n"
line15 = (f'{candidate_list[2]['name']}: {format(((candidate_list[2]['votes']/ total_votes)*100), ".2f")}%, ({candidate_list[2]['votes']})')
line16 = "\n"
line17 = ("-------------------------------------------------")
line18 = "\n"
line19 = "\n"
line20 = (f'Winner: {winner}')
line21 = "\n"
line22 = "\n"
line23 = ("------------------------------------------------")

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
               line23
) 

