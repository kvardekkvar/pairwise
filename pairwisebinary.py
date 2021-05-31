import itertools
import numpy as np
import scipy.special

k=1
cnt=0
A = []

n=int(input("Число столбцов:"))

while(scipy.special.binom(2*k, k)<2*n):
    k=k+1

for bits in itertools.combinations(range(2*k), k):
    if 0 not in bits:
        continue
    s = ['0'] * 2*k
    for bit in bits:
        s[bit] = '1'
    A.append(''.join(s))
    cnt=cnt+1
    if cnt>=n:
        break

res=np.empty((0,2*k), dtype=int)
for a in A:
    res=np.vstack((res, list(a)))
res=res.transpose()
for s in res:
    print("".join(s))
