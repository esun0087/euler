import codecs

from math import gcd
from functools import reduce
import sys
n = 10**8


def old_test(x):
    d = {}
    left = 1
    i = 0
    while 1:
        q, r = left // x, left % x
        i += 1
        if left in d:
            return i - d[left]
        
        d[left] = i
        left = r * 10
primes = [int(i) for i in codecs.open('prime.txt', 'r', 'utf-8') if i.strip() and int(i.strip()) < n]
primes_set = set(primes)

print ('read prime over')


def divisior(x):
    p_s = []
    for i, p in enumerate(primes):
        if x < p or x <= 1:
            break
        if x % p == 0:
            k = 0
            while x % p == 0:
                x //= p
                k += 1
            p_s.append((p, k))
    divs = [1]
    for p, k in p_s:
        tmp_divs = []
        for d in divs:
            tt = 1
            for t in range(k+1):
                tmp_divs.append(d * tt)
                tt *= p
        divs = tmp_divs
    divs.sort()
    return divs

min_divs = [0 for i in range(n+10)]

for i in range(1, n+1):
    if i % 100 == 0:
        print (i)
    for j in range(i, n + 1, i):
        if j + 1 not in primes_set:
            continue
        if min_divs[j+1] == 0:
            if pow(10, i, j + 1) == 1:
                min_divs[j+1] = i
        else:
            continue

print ('min_divs over')
def get_prime_feq(p):
    return min_divs[p]
primes_f = []

for p in primes:
    if p == 2 or p == 5:
        primes_f.append(1)
        continue
    primes_f.append(get_prime_feq(p))
    
print('get_prime_feq over')


def k_primes(i, k):
    p = primes[i]
    if p == 3: 
        if k <= 2:
            return primes_f[i]
        return p ** (k-2) * primes_f[i]
    if p == 487:
        if k <= 2:
            return primes_f[i]
        return p ** (k-2) * primes_f[i]
    return p ** (k-1) * primes_f[i]

def lcm(x, y):
        return x // gcd(x, y) * y

def red_lcm(seq):
    return reduce(lcm ,seq)

def get_seq(seq):
    s = []
    for i, k in seq:
        s.append(k_primes(i, k))
    return s
def sum_f(m ,n):
    s = 0
    for i in range(m ,n+1):
        if i % 1000 == 0:
            print (i)
        seq = p_p_s[i]
        seq = get_seq(seq)
        if seq != []:
            s += red_lcm(seq)
    print (s)
    

def test(m ,n):
    for i in range(m ,n+1):
        if i % 1000 == 0:
            print (i)
        seq = p_p_s[i]
        
        seq = get_seq(seq)
        if seq != []:
            if  red_lcm(seq) != old_test(i):
                print(i, p_p_s[i], get_seq(p_p_s[i]), red_lcm(seq), old_test(i))
                input()
        
lcm_seq = [0 for i in range(n+1)]
for i, p in enumerate(primes):
    if i % 100 == 0:
        print (i, p)
    for kk in range(p, n+1, p):
        x = kk
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        if i != 0 and i != 2:
            tmp = k_primes(i, k)
            if lcm_seq[kk] == 0:
                lcm_seq[kk] = tmp
            else:
                lcm_seq[kk] = lcm(lcm_seq[kk], tmp)
print (sum(lcm_seq))

