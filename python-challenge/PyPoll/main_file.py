import csv
import os
import sys
#Read the CSV file
voting_data = "PyPoll/Resources/election_data.csv"
with open(voting_data, 'r') as csvfile : 
      csvreader = csv.reader(csvfile, delimiter = ',')
      header = next(csvreader)
      Total_vote = 0
      
      Charles_vote = 0
      Diana_vote = 0
      Raymon_vote = 0 
      #Start the loop through the csv file
      for row in csvreader:
       #calculate total vote
       Total_vote +=1
       #calculate each candidate's vote
       if row[2] == "Charles Casper Stockham":
           Charles_vote +=1
       if row[2] == "Diana DeGette":
           Diana_vote += 1
       if row[2] == "Raymon Anthony Doane":
           Raymon_vote +=1
        #calculate percentage of their votes
        #   
       Percentage_Charles = round(((Charles_vote/Total_vote)*100),3)
       Percentage_Diana = round(((Diana_vote/Total_vote)*100),3)
       Percentage_Raymon = round(((Raymon_vote/Total_vote)*100),3)
       winner_count = max(Charles_vote,Diana_vote,Raymon_vote)
       #Find the winner
       if winner_count == Charles_vote :
           winner = "Charles Casper Stockham"
       if winner_count == Diana_vote :
           winner = "Diana DeGette" 
       if winner_count == Raymon_vote :
           winner = "Raymon Anthony Doane"
#Print the result to the terminal
print ("Total Votes :", Total_vote)
print ("Charles Casper Stockham :", str(Percentage_Charles) +"% "+ "("+str(Charles_vote)+")")
print ("Diana DeGette :", str(Percentage_Diana) +"% "+ "("+str(Diana_vote)+")")
print ("Raymon Anthony Doane :", str(Percentage_Raymon) +"% "+ "("+str(Raymon_vote)+")")
print ("Winner :", winner)
#Export the result to a txt file
sys.stdout = open("PyPoll/Analysis/Analysis.txt", 'w')
print ("Total Votes :", Total_vote)
print ("Charles Casper Stockham :", str(Percentage_Charles) +"% "+ "("+str(Charles_vote)+")")
print ("Diana DeGette :", str(Percentage_Diana) +"% "+ "("+str(Diana_vote)+")")
print ("Raymon Anthony Doane :", str(Percentage_Raymon) +"% "+ "("+str(Raymon_vote)+")")
print ("Winner :", winner)
sys.stdout.close()