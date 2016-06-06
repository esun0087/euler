cache = {1:1, 2:1, 3:3}
mod_ = 10**9
def f(n):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        r = f(n//2)
    if n % 4 == 1:
        r = 2 * f(2 * (n - 1) // 4 + 1) - f(n // 4)
    if n % 4 == 3:
        r = 3 * f(2 * (n-3) // 4 + 1) - 2 * f(n // 4)
    r %= mod_
    cache[n] = r
    
    return r
def s_f(n):
    i = 1
    s = 0
    while i <= n:
        t = f(i)
        #print (i, t)
        s += t
        i += 1
    print (s)
import sys

class WeirdRecurrenceRelation():
    def __init__(self):
        self.cached = {}
        self.cached[1] = 1
        self.cached[3] = 3

    def get(self, n):
        if n in self.cached:
            return self.cached[n]
        if n % 2 == 0:
            results = self.get(n // 2)
            self.cached[n] = results
            return results
        elif n % 4 == 1:
            m = n // 4
            results = 2 * self.get(2*m + 1) - self.get(m)
            self.cached[n] = results
            return results
        elif n % 4 == 3:
            m = n // 4
            results = 3 * self.get(2*m + 1) - 2 * self.get(m)
            self.cached[n] = results
            return results

class WeirdRecurrenceSumRelation():
    def __init__(self):
        self.cached = {
            0: 0,
            1: 1,
            2: 2,
            3: 5,
        }
    
    def get(self, n):
        if n in self.cached:
            return self.cached[n]
        results = None
        q, r = divmod(n, 4)
        print (n, q, r)
        if r == 0:
            results = 6 * self.get(2*q) - 5 * self.get(q) - 3 * self.get(q - 1) - 1
        elif r == 1:
            results = 2 * self.get(2*q + 1) + 4 * self.get(2 * q) - 6 * self.get(q) - 2 * self.get(q - 1) - 1
        elif r == 2:
            results = 3 * self.get(2*q + 1) + 3 * self.get(2 * q) - 6 * self.get(q) - 2 * self.get(q - 1) - 1
        elif r == 3:
            results = 6 * self.get(2*q + 1) - 8 * self.get(q) - 1
        self.cached[n] = results
        return results

class Problem():
    def solve(self):
        relation = WeirdRecurrenceSumRelation()
        #assert(relation.get(8) == 22)
        assert(relation.get(100) == 3604)
        #print(relation.get(3**37) % 10**10)

def main():
    problem = Problem()
    problem.solve()
    
'''
if __name__ == '__main__':
    sys.exit(main())
'''
from math import log2
import math
d = {1:1, 2:1}
def new_f(n):
    if n in d:
        return d[n]
    q, r = divmod(n, 2)
    #print (n, q, r)
    if r == 0:
        ans = new_f(q)
    else:
        ans = new_f(q) + 2 ** int(math.log2(n))
    d[n] = ans
    return ans
def s(n):
    return sum(4 ** i for i in range(n+1))

def special_f(n):
    #print (n)
    if n == 0:
        return 1
    log_base = int(math.log2(n))
    if 2 ** log_base == n:
        return 1
    if 2 ** (log_base+1) == n + 1:
        return 4 ** log_base
    q, r = divmod(n, 2)
    if r == 1:
        return 2 * (special_f(q)) + 2 ** log_base * (n - 2 ** log_base + 1) // 2
    return special_f(n - 1) + new_f(n)
def s_s(n):
    mod_v = 10**9 
    n_2 = int(log2(n))
    n_2 -= 1
    base = s(n_2) % mod_v
    ext = special_f(n) % mod_v
    
    print ('base:',base)
    print ('ext:',ext)
    print ((ext + base) % mod_v)

s_s(3**37)
s_s(8)
s_s(100)
s_f(7)