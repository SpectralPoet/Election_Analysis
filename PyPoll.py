#-------------The data we need to retrieve:-----------------------------------
# 1. The total number of votes cast.
# 2. A complete list of candidates who revieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


#------------------------Import dependencies:----------------------------------

import csv
import random
import os
#import numpy (numpy can't be resolved, anaconda issue..?)


#---------------------------Create variables:-------------------------------

#Get filepath to read, as string
file_to_read = os.path.join("Resources","election_results.csv")
#Get filepath to write to, as string
file_to_write = os.path.join("analysis","election_analysis.txt")


#-----------------------------Read and analyze data:---------------------------

#Create file variable to read from
with open(file_to_read) as read_election_data:
    
    #create reader
    file_reader = csv.reader(read_election_data)
    
    #To do: Analysis

    #Close primary data file
    read_election_data.close()


#--------------------------Write data to file:----------------------------------

#Create file variable to write to 
with open(file_to_write, "w") as written_election_data:
    
    #To do: output results
    written_election_data.write("Counties in the Election")
    written_election_data.write("\n------------------------")
    written_election_data.write("\nArapahoe\nDenver\nJefferson")


    written_election_data.close()