# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:30:03 2019

@author: Andrew
"""

import matplotlib.pyplot as plt

def hofstadters_q_seq(n):
    seq = []
    seq.append(1)
    seq.append(1)
    for i in range(2,n):
        seq.append(seq[i - seq[i-1]] + seq[i - seq[i-2]])
    return seq


num = 500

plt.xlabel('n')
plt.ylabel('Q(n)')
plt.plot(range(1,num+1), hofstadters_q_seq(num))
plt.show()