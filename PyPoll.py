#The data we need to retrieve:
# 1. The total number of votes cast.
# 2. A complete list of candidates who revieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.
#----------------------------------------------------------

import csv
import random
import os
#import numpy (numpy can't be resolved)

#for some reason this is running in the 'resources' folder,
#so the first argument is unnecessary
file_to_read = os.path.join("election_results.csv")

#for some reason this is running from the recources folder..?
file_to_write = os.path.join("..","analysis","election_analysis.txt")

#file to write to
open(file_to_write, "w")

#Open primary data file
with open(file_to_read) as read_election_data:
    
    #To do: Analysis

    #Close primary data file
    read_election_data.close()