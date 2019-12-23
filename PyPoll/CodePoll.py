import os 
import csv

csv_file=os.path.join("election_data.csv") 

print('Election Results')
print('----------------------------')
# convert csv to dictionary
with open('election_data.csv','r') as f:
    f.readline() # ignore first line (header)
    reader=csv.reader(f)
    mylist=list(reader)

    #print (mylist[:13])
#Calculation Total number of votes
    total_votes=len(mylist)
    #total_votes=int(total_votes)
    print('Total Votes:  '+str(total_votes))
    print('-------------------------------')

#Printing list of candidates
    result = [candidate[2] for candidate in mylist]
    #print(result[:10])
    result_i=result[:100]
    #print(result_i)  #result_ is a sample
#counting votes for each candidate
    votes={i:result_i.count(i) for i in result_i}
    #votes={candidate:mylist[2].count(candidate) for candidate in mylist}
    #votes=votes[:10]
    #print(votes)

    #converting dictionary result into lists
    keys = votes.keys() 
    values = votes.values()

    #convert values to integers
    values=[int(i) for i in values]
    #print(keys)
    #print(values)

    #calculate % votes
    percent=[x/total_votes*100 for x in values]
    percent=["%.2f" % i for i in percent]
    percent_symb=['%']*len(percent)
    #print(percent_symb)
    #percent=percent("%.3f%%" % ([x/total_votes*100 for x in values]))
    #print(percent)
    
    #creating list of tuples
    sumList=list(zip(keys,values,percent,percent_symb))
    #print(sumList)
    for i in sumList:
        print(*i,sep=' ')
    
    sort_winner=sorted(sumList,key=lambda tup:tup[1])
    winner=sort_winner[len(sort_winner)-1]
    ##print(*sumList,sep='\n')
    print('-------------------------')
    print('Winner')
    print(winner[0])
    print('---------------------------')

#print to .txt file
with open('elections.txt','w') as f:
    print('Election Results',file=f)
    print('----------------------------',file=f)
    print('Total Votes:  '+str(total_votes),file=f)
    print('-------------------------------',file=f)
    #print(*sumList,sep='\n',file=f)
    for i in sumList:
        print(*i,sep=' ',file=f)
    print('-------------------------',file=f)
    print('Winner',file=f)
    print(winner[0],file=f)
    print('---------------------------',file=f)



