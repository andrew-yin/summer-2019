"""
By: Andrew Yin
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

plt.subplot(1,2,1)
plt.xlabel("n")
plt.ylabel("Q(n)")
plt.plot(range(1,num+1), hofstadters_q_seq(num))

plt.subplot(1,2,2)
plt.xlabel("n")
plt.ylabel("Q(n) - n/2")
plt.plot(range(1,num+1), [m - n for m,n in zip(hofstadters_q_seq(num),[x / 2 for x in range(1,num+1)])])
         
plt.tight_layout()
plt.show()
