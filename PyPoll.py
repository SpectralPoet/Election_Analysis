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

#list of all candidates
candidate_options = []
#dict of candidates & vote totals
candidate_votes = {}


#holds total votes
total_votes = 0
#to hold winner
winning_candidate = ""
#count of votes for winner
winning_count = 0
#percentage of votes for winner
winning_percentage = 0

#-----------------------------Read and analyze data:---------------------------

#Create file variable to read from - with
with open(file_to_read) as read_election_data:
    
    #create reader
    file_reader = csv.reader(read_election_data)
    
    #To do: Analysis------------------
    
    #store and skip header data
    header_row=next(file_reader)
    
    for row in file_reader: #for each row in the file being read

        total_votes += 1 #each row of data is one vote

        candidate_name = row[2] #candidate name in each row

        if candidate_name not in candidate_options: #if not in candidate list

            candidate_options.append(candidate_name) #add it

            candidate_votes[candidate_name] = 0 #set initial value in dict to 0

        #add 1 to votes_dict every time name appears in row
        candidate_votes[candidate_name] += 1

    #Close primary data file
    read_election_data.close()

#1. The total number of votes cast. [COMPLETE]
#print(total_votes)

#2. A complete list of candidates who revieved votes. [COMPLETE]
#4. The total number of votes each candidate won. [COMPLETE]
#print(candidate_votes)

#3. The percentage of votes each candidate won. [COMPLETE]
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes,})\n')
    
    #if current candidate name has more # and % of votes, set as temp winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winnning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")

# 5. The winner of the election based on popular vote.
print(winning_candidate_summary)




#--------------------------Write data to file:----------------------------------

#Create file variable to write to - with
with open(file_to_write, "w") as written_election_data:
    
    #To do: output results
    written_election_data.write("Counties in the Election")
    written_election_data.write("\n------------------------")
    written_election_data.write("\nArapahoe\nDenver\nJefferson")


    written_election_data.close()