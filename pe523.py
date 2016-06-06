
from itertools import permutations
def generate_permution(s):
    return [i for i in permutations(s)]
    
def F(L):
    L = list(L)
    c = 0
    while 1:
        tag = True
        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                tmp = L[i]
                L[1:i+1] = L[0:i]
                L[0] = tmp
                tag = False
                c += 1
                break
        if tag:
            break
    return c


def E(n):
    #base_l = [i+1 for i in range(n)]
    base_l = [1,3,4,5,6]
    #for L in generate_permution(base_l):
    #    print (L, F(L))
    print (sum(F(L) for L in generate_permution(base_l)) / 24)
import sys

class Problem():
    def solve(self):
        count = 0
        factorial = 1
        # F(n) = n F(n - 1) + (n - 1)! (2^{n - 1} - 1)
        for n in range(2, 30 + 1):
            count = count * n + (2**(n - 1) - 1) * factorial
            factorial = factorial * n
            expected_value = 1.0 * count / factorial
            print(n, '=>', expected_value)

def main():
    problem = Problem()
    problem.solve()

from itertools import combinations
from math import factorial
if __name__ == '__main__':
    n = 10
    b = [i+1 for i in range(n)]
    for c in range(3, n):
        for base_l in combinations(b, c):
            print (c, sum(F(L) for L in generate_permution(base_l)) / factorial(c))
    #for i in range(4, 10):
    #    E(i)
    #sys.exit(main())
