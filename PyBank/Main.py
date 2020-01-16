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

    keys = list(mydict.keys()) 
    values = list(mydict.values()) 

    
#convert values to integer and sum
    values=[int(i) for i in values]
    #print("converted list:"+str(values))

#getting Sum of values Total P&L
    total_pl=sum(values)
    print("Total: "+str(total_pl))

#Calculating Average Change
    
    dif=[values[i+1]-values[i] for i in range(len(values)-1)]
    average_change=round(sum(dif)/len(dif),2)
    print("Average Change: "+str(average_change))

#Calculating Greatest Increase in Profit
    max_i=max(dif)
    index_max=dif.index(max_i)
    index_key=keys[index_max+1]
    print("Greatest Increase in Profits: "+str(index_key)+"   "+"$"+"("+str(max_i)+")")

#Calculating Greatest Decrease in Profit
    min_i=min(dif)
    index_min=dif.index(min_i)
    index_val=keys[index_min+1]
    """min_i=[(value,key) for key,value in mydict.items()]
    min_k=(min(min_i)[1])
    min_v=(min(values))"""
    print("Greatest Decrease in Profits: "+str(index_val)+"   "+"("+"$"+str(min_i)+")")
#printing to .txt file
with open('out.txt', 'w') as f:
    print('Financial Analysis',file=f)
    print('----------------------------',file=f)
    print('Total Months: ',len(mydict),file=f)
    print('Average Change: '+str(average_change),file=f)
    print("Greatest Increase in Profits: "+str(index_key)+"   "+"$"+"("+str(max_i)+")",file=f)
    print("Greatest Decrease in Profits: "+str(index_val)+"   "+"("+"$"+str(min_i)+")",file=f)
 