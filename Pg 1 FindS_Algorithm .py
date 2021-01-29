#Find-S Algorithm 
import pandas as pd
import csv

#Your code goes hear to Read csv file
def read_data(filename):
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        traindata = []
        for row in datareader:
            traindata.append(row)
    return (traindata)

h = ['0', '0', '0', '0', '0', '0'] #intialize with specific hypothesis
data=read_data('dataset1.csv')

def Generalize(h, a):
    for i in range(len(a)):
        if (h[i] != a[i]):
            h[i] = '?'
        else:
            h[i] = a[i]
    return(h)

    #Your Code goes here 
def isConsistent(h,d):
    if len(h)!=len(d)-1:
        print('Number of attributes are not same in hypothesis.')
        return False
    else:
        matched=0        
        for i in range(len(h)):
            if ( (h[i]==d[i]) | (h[i]=='any') ):    
                matched=matched+1
            if matched==len(h):
                return True
            else:
                return False
def makeConsistent(h,d):
    for i in range(len(h)):
        if((h[i] == 'phi')):
            h[i]=d[i]
        elif(h[i]!=d[i]):
            h[i]='any'
    return h
    print('Begin : Hypothesis :',h)
    
print('==========================================')
for d in data:
    if d[len(d)-1]=='Yes':
        if ( isConsistent(h,d)):
            pass 
        else:
            h=makeConsistent(h,d)
        print ('Training data         :',d)
        print ('Updated Hypothesis    :',h)
        print()
        print('--------------------------------')
        print('==========================================')

print("The Maximally Specific Hypothesis is: ", h)

#Assign: Create a test case and classify "Yes" or "No"
TestCase = ["Sunny", "Warm", "Normal", "Strong", "Cool", "Change"]

#Your code goes here
Outcome = d[7]

print("EnjoySport =", Outcome )
