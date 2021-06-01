import itertools
import numpy as np
import scipy.special

k = 1
cnt = 0

n = int(input("Число столбцов (должно быть >=6):"))
while scipy.special.binom(2*k, k) < 2*n:
    k = k + 1

res = np.zeros((2*k, n), dtype=int)

for bits in itertools.combinations(range(2*k), k):
    if 0 not in bits:
        continue
    for bit in bits:
        res[bit, cnt] = 1
    cnt = cnt+1
    if cnt >= n:
        break


for i in res:
    for j in i:
        print(j, end='')
    print()
