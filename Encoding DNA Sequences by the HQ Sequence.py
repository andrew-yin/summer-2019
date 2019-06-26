# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:41:19 2019

@author: CommanderPokerFace
"""

import matplotlib.pyplot as plt

def DNA_encode(seq):
    mapping = {'A':[1,1], 'T':[0,1], 'C':[1,0], 'G':[0,0]}  
    R = []
    S = []
    n = len(seq)
    for i in range(n):
        R.append(mapping[seq[i]][0])
        S.append(mapping[seq[i]][1])
        
    Q = []
    P = []
    for i in range(2):
        Q.append(1)
        P.append(1)
    
    for i in range(2,n):
        Q.append(Q[i - Q[i-1]] + Q[i - Q[i-2]] + R[i])
        P.append(P[i - P[i-1]] + P[i - Q[i-2]] + S[i])
    return Q, P

betaglobin = 'GAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCGTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC'

q, p = DNA_encode(betaglobin)

print('Q =', q)
print('P =', p)

plt.figure(figsize = (10,8))
plt.xlabel("Q(n)")
plt.ylabel("P(n)")
plt.plot(q,p)


