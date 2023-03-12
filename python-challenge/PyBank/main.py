import csv
import os
import sys

#Read the CSV file
budget_data = "PyBank/Resources/budget_data.csv"
with open(budget_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    first_line = next(csvreader)
    
    num_months = 1
    
    date_change=[]

    profit = int(first_line[1])
    previous = int(first_line[1])
    previous_date = str(first_line[0])
    current = 0
    sum_change = 0
 
    for row in csvreader:

        #Calculate months
        num_months +=1

        #Calculate profit
        profit = profit + int(row[1])

        #Calculate Average change
        current = int(row[1])
        profit_losses_change = current - previous        
        previous = current
        sum_change += profit_losses_change
        avg_change = sum_change / (num_months - 1)

        #Find the Greatest increase and decrease and dates
        current_list = [row[0], profit_losses_change]
        date_change.append(current_list)
       
        
        
#Sort the change and date        
date_change.sort(key=lambda x: (x[1]))

#Print results
print("Total Month: ", num_months) 
print("Total profit: ", profit)     
print("Average change: ", avg_change)
print("Greatest Increase in Profits: ",date_change[-1])
print("Greatest Decrease in Profits: ",date_change[0])

#Export result to txt file
sys.stdout = open("PyBank/Analysis/Analysis.txt", 'w') 
print("Total Month: ", num_months) 
print("Total profit: ", profit)     
print("Average change: ", avg_change)
print("Greatest Increase in Profits: ",date_change[-1])
print("Greatest Decrease in Profits: ",date_change[0])
sys.stdout.close()