import os 
import csv

csv_file=os.path.join("election_data.csv") 


# convert csv to dictionary
with open('election_data.csv','r') as f:
    f.readline() # ignore first line (header)
    reader=csv.reader(f)
    mylist=list(reader)

    #print (mylist[:13])
#Calculation Total number of votes
    total_votes=len(mylist)
    #total_votes=int(total_votes)
    #print('Total Votes:  '+str(total_votes))

#Printing list of candidates
    result = [candidate[2] for candidate in mylist]
    #print(result[:10])
    result_i=result[:10]
    #print(result_i)  #result_ is a sample
#counting votes for each candidate
    votes={i:result_i.count(i) for i in result_i}
    #print(votes)
    
    #converting dictionary result into lists
    keys = votes.keys() 
    values = votes.values()

    #convert values to integers
    values=[int(i) for i in values]
    print(keys)
    print(values)

    #calculate % votes
    percent=[x/total_votes*100 for x in values]
    print(percent)



