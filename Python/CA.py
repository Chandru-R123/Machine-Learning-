import numpy as np
import pandas as pd

def Candidate_Elimination(concept, target):

    S = concept[0].copy()
    G = ["?" for _ in range(len(S))]
    print("Initail S:", S)
    print("Initail G:", G)

    for i in range(len(concept)):

        if target[i] == 'yes':
            for j in range(len(S)):
                if S[j] != concept[i][j]:
                    S[j] = '?'

        else:
            for j in range(len(S)):
                if S[j] != concept[i][j]:
                    G[j] = S[j]
        print("\nStep :", i+1)
        print("Updated S", S)
        print("Updated G", G)

    return S, G



data = pd.read_csv("data.csv")

concept = data.iloc[:, :-1].values   
target = data.iloc[:, -1].values    


S, G = Candidate_Elimination(concept, target)

print("\nFinal S:", list(S))
print("Final G:", [str(x) for x in G])
