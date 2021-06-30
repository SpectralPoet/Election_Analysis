#The data we need to retrieve:
# 1. The total number of votes cast.
# 2. A complete list of candidates who revieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.
import csv
import random
import numpy
import sys

print(sys.version)

file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')

