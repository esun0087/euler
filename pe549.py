import codecs

n = 10 ** 5
primes = []
for i in codecs.open('prime.txt', 'r', 'utf-8'):
    if int(i.strip()) < n:
        primes.append(int(i))
    else:
        break

print ('read prime over')
def divisior(x):
    p_s = []
    for p in primes:
        if x < p or x <= 1:
            break
        if x % p == 0:
            k = 0
            while x % p == 0:
                x //= p
                k += 1
            p_s.append((p, k))
    return p_s
    
def all_div(n):
    p_p_s = [[] for i in range(n+1)]
    for p in primes:
        for i in range(p, n + 1, p):
            k = 0
            tmp = i
            while tmp % p == 0:
                tmp //= p
                k += 1
            p_p_s[i].append((p, k))
    return p_p_s
from time import clock
def test_1():
    bb = clock()
    data = [i for i in range(n+1)]
    s = 0
    for i in range(1, n + 1):
        if i % 1000 == 0:
            print (i)
        prime_div = divisior(i)
        for p, k in prime_div:
            for L in range(p, n + 1, p):
                tmp = data[L]
                if tmp == 1:
                    continue
                tmp_k = 1
                while tmp_k <= k and tmp % p == 0:
                    tmp //= p
                    tmp_k += 1
                data[L] = tmp
                if tmp == 1:
                    s += i
                

    print (s)
    print (clock() - bb)

def test_2():
    bb = clock()
    data = [i for i in range(n+1)]
    p_p_s = all_div(n)
    print ('div over')
    s = 0
    for i in range(1, n + 1):
        if i % 1000 == 0:
            print (i)
        prime_div = p_p_s[i]
        for p, k in prime_div:
            for L in range(p, n + 1, p):
                tmp = data[L]
                if tmp == 1:
                    continue
                tmp_k = 1
                while tmp_k <= k and tmp % p == 0:
                    tmp //= p
                    tmp_k += 1
                data[L] = tmp
                if tmp == 1:
                    s += i
        p_p_s[i] = []
    print (s)
    print (clock() - bb)


import sys

class Problem():
    def solve(self):
        assert(self.get(100) == 2012)
        print(self.get(10**8))
        
    def get(self, n):
        m_values = [1 for i in range(n + 1)]
        m_values[0] = m_values[1] = 0
        for i in range(2, n + 1):
            if m_values[i] == 1:
                d = i
                e = 1
                while d <= n:
                    m = self.__get_smallest_number_m(i, e)
                    for j in range(d, n + 1, d):
                        m_values[j] = max(m_values[j], m)
                    d = d * i
                    e += 1
        return sum(m_values)

    def __get_smallest_number_m(self, prime, exponent):
        lower_bound, upper_bound = 1, exponent 
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2
            middle_value = self.__adic_valuation(middle * prime, prime)
            if middle_value < exponent:
                lower_bound = middle + 1
            elif middle_value == exponent:
                return middle * prime
            else:
                upper_bound = middle - 1
        return lower_bound * prime

    def __adic_valuation(self, factorial_n, prime):
        output = 0
        d, k = prime, 1
        while d <= factorial_n: 
            output += factorial_n // d
            d *= prime
        return output

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())