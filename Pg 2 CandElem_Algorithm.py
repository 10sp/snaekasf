#Candidate-Elimination Algoirthm
#Steps 
#1 Generalize S
#2 Specialize G
#2.2 Construct G
#2.3 Prune G

import pandas as pd

def Generalize(S_in, Exin):
    features = len(Exin)
    for i in range(features):
        if(S_in[i] != Exin[i]):
            S_in[i] = '?'
        else:
            S_in[i] = Exin[i]
    return(S_in)

def Specialize(G, S, Ex, NegCount):
    if(NegCount == 1):
        G = ConstructG(G,S,Ex)
    else:
        G = Pruning(G, Ex)
    return(G)          

def ConstructG(G,S,ex):
    #Your Code Goes Here
    if(S[0] != ex[0] and S[0] != '?'):
        G.append([S[0], '?', '?', '?', '?' , '?'])
    if(S[1] != ex[1] and S[1] != '?'): 
        G.append(['?', S[1], '?', '?', '?', '?' ])
    if(S[2] != ex[2] and S[2] != '?'):
        G.append(['?', '?', S[2], '?', '?', '?' ])
    if(S[3] != ex[3] and S[3] != '?'):
        G.append(['?', '?', '?', S[3], '?' , '?'])
    if(S[4] != ex[4] and S[4] != '?'):
        G.append(['?', '?', '?', '?', S[4], '?'])
    if(S[5] != ex[5] and S[5] != '?'):
        G.append(['?', '?', '?', '?', '?', S[5] ])
        return(G)
    

def Pruning(G, Ex):
    #Your Code Goes Here
    ind = []
    features = len(Ex)
    for i in range(len(G)):
        for k in range(features):
            if G[i][k] == Ex[k]:
                ind.append(i)
    Prune_G = [G[i] for i in ind]
    return(Prune_G)
                

G = []
S = ['?', '?', '?', '?', '?', '?']
df = pd.read_csv('dataset1.csv')

X = df.values[:, 1:7]
Y = df.values[:, -1]

if Y[0] == 'Yes':
    S = X[0,:]
else:
    print("Error: First Example is not positive")

    
NegCount = 0

for i in range(len(X)-1):
    if(Y[i+1] == "Yes"):
        S = Generalize(S, X[i+1,:])
        if(NegCount > 0):
            G = Specialize(G,S,X[i+1,:],NegCount = 0)
    else:
        NegCount = NegCount + 1
        G = Specialize(G,S,X[i+1,:],NegCount)
               
print('Specific Hypothesis = ', S)
print('\n')
print('General Hypothesis = ', G)
