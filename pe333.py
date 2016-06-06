from copy import copy
from math import log
def get_all_data(n):
    L = []
    for i in range(int(log(n,2))+1):
        for j in range(int(log(n,3))+1):
            if 2 ** i * 3 ** j <= n:
                L.append(2 ** i * 3 ** j)
    return sorted(L)
    
def get_relation(L):
    d = {}
    d1 = {}
    for i in range(len(L)):
        d[L[i]] = []
        d1[L[i]] = set()
        for j in range(i+1, len(L)):
            if L[j] % L[i] != 0:
                d[L[i]].append(L[j])
            else:
                d1[L[i]].add(L[j])
    return d, d1
    
d, d1 = get_relation(get_all_data(1000000 ))

def ok_v(ans, v):
    return not v in ans
def get_partition(x, key, d, ans):
    if x <= 0:
        if x < 0:
            return 0
        if x == 0:
            return 1
    c = 0
    for i in d[key]:
        if i > x:
            break
        if not ok_v(ans, i):
            continue
        c += get_partition(x - i, i, d, ans | d1[i])
        if c > 1:
            break
    return c
    
def cal_n(n):
    s = 0
    for k in d:
        s += get_partition(n - k, k, d, d1[k])
    return s
if __name__ == '__main__':

    s = 0
    for i in open('..\\prime.txt'):
        if int(i) < 1000000:
            print(int(i))
            if cal_n(int(i)) == 1:
                s += int(i)
        else:
            break
    print(s)

    