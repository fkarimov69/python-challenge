import os 
import csv

csv_file=os.path.join("budget_data.csv") 
    


# convert csv to dictionary
with open('budget_data.csv') as f:
    f.readline() # ignore first line (header)
    mydict = dict(csv.reader(f, delimiter=','))

#print (mydict)
#print Header
    print("Financial Analysis")
    print("----------------------------")
#for key in mydict:
    #print(key)
#calculating and printingTotal numbers of months
    print("Total Months: ",len(mydict))

    keys = mydict.keys() 
    values = mydict.values() 
   
    
#convert values to integer and sum
    values=[int(i) for i in values]
    #print("converted list:"+str(values))

#getting Sum of values Total P&L
    total_pl=sum(values)
    print("Total: "+str(total_pl))

#Calculating Average Change
    average_change=round(total_pl/len(mydict),2)
    print("Average Change: "+str(average_change))

#Calculating Greatest Increase in Profit
    max_i=[(value,key) for key,value in mydict.items()]
    max_k=(max(max_i)[1])
    max_v=(max(values))
    print("Greatest Increase in Profits: "+str(max_k)+"   "+"("+str(max_v)+")")

#Calculating Greatest Decrease in Profit
    min_i=[(value,key) for key,value in mydict.items()]
    min_k=(min(min_i)[1])
    min_v=(min(values))
    print("Greatest Decrease in Profits: "+str(min_k)+"   "+"("+str(min_v)+")")
#printing to .txt file
with open('out.txt', 'w') as f:
    print('Financial Analysis',file=f)
    print('----------------------------',file=f)
    print('Total Months: ',len(mydict),file=f)
    print('Average Change: '+str(average_change),file=f)
    print('Greatest Increase in Profits: '+str(max_k)+'   '+'('+str(max_v)+')',file=f)
    print('Greatest Decrease in Profits: '+str(min_k)+'   '+'('+str(min_v)+')',file=f)
