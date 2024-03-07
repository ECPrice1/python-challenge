import os

# Module for reading CSV files
import csv



csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

print(csvpath)
print(os.path.isfile(csvpath))