# Assign a variable for the file to lead and the path.
#file_to_load = r'C:\Users\Kaylaa\Documents\Bootcamp\03-Python\Resources\election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
#To do: perform analysis.
# Close the file.
#election_data.close()
# Open the election results and read the file
#with open(file_to_load) as election_data:

    #To do: perform analysis.
    #print(election_data)
# The data we need to retrieve.
import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join(".", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_date:
    # Print the file object.
    # print(election_data)
#Import the datetime classs  from the datetime module
import datetime
#Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#Print the present time
#print("The time right now is ", now)
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
    # Using the open() function with the "w" mode we will write data to the file
    #outfile = open(file_to_save,"w")
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
# Write some data to the file
    #outfile.write("Hello World")
#txt_file.write("Hello World")
    #Close file
    #outfile.close()
# Write three counties to the file
    #txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of th election based on popular vote. 