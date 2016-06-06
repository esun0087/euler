

max_c = 10**3 + 1
primes = [int(i) for i in open('prime.txt') if i.strip()]
prime_set = set(primes)
from itertools import combinations


def be_antinas(x):
    x = sorted(x)
    for i, d in enumerate(x):
        for v in x[i+1:]:
            if v % d == 0:
                return False
    return True
def generate_div(x):
    prime_d = []
    if x in prime_set:
        return [x]
    for p in primes:
        if p > x:
            break
        L = 0
        while x % p == 0:
            x //= p
            L += 1
        if L != 0:
            prime_d.append((p, L))
    ans = [1]
    prime_pos = 0
    while prime_pos < len(prime_d):
        this_primes = [prime_d[prime_pos][0] ** i for i in range(prime_d[prime_pos][1] + 1)]
        tmp_ans = []
        for v in ans:
            for x in this_primes:
                tmp_ans.append(x * v)
        prime_pos += 1
        ans = tmp_ans
    return sorted(ans)
    #return [i for i in range(1, x+1) if x % i == 0]
    
def ok(L, v):
    for i in L:
        if v % i == 0:
            return False
    return True
def new_normal_way(n):
    seq = generate_div(n)
    ans_stack = [((v,), i) for i, v in enumerate(seq[1:])]
    while 1:
        this_stack = []
        tag = False    
        for L, i in ans_stack:
            tmp = list(L)
            for j in range(i+1, len(seq)):
                v = seq[j]
                if ok(tmp, v):
                    tag = True
                    tmp.append(v)
                    this_stack.append((tuple(tmp), j))
                    tmp.pop()
        if not tag:
            break
        ans_stack = this_stack
    if len(ans_stack) == 0:
        return 0
    return (len(ans_stack[0][0]))        

if __name__ == '__main__':
    myans = 0
    for i in range(1, 10**8+1):
        if i % 1000 == 0:
            print (i)
        myans += new_normal_way(i)
    print (myans)
    #print (i, new_normal_way(i))
