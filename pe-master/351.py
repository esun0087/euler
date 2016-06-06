def getPrime():
    prime = []
    for i in open('prime.txt'):
        if int(i) <= M:
            prime.append(int(i))
        else:
            break
    return prime

def get_phi(i):
    s = i
    if i in setP:
        s = i - 1
        return s
    else:
        for p in prime:
            if p * p > i:
                break
            if i in setP:
                s = s * (i-1)/i
                break
            if i % p == 0:
                s = s * (p-1) / p
            while i%p == 0:
                i /= p
    return s


def sum_phi(M):
    s = 0
    i = 2;
    while i <= M:
        s += get_phi(i)
        i += 1
    return s
    '''
    for p in prime:
        t = p
        while t <= M:
            Array[t] = Array[t] * (p-1) / p
            t += p
    return sum(Array[2:])
    '''

def getDiagonal(M):
    x, i = 0, 1
    while i < M:
        if gcd(i, M-i) == 1:
            x += 1
        i += 1
    return x


from fractions import gcd
from time import clock
if __name__ == '__main__':
    '''
    read prime
    cal sum(phi)
    for point in coords do judge
        if ok x++, count--
    s = count / 2 + x
    n (n-1) / 2 - s
    '''
    M = 10000000
#    Array = range(M+1)
    prime = getPrime()
    setP = set(prime)
    b = clock()
    count = sum_phi(M)
    ans = M * (M - 1) / 2;
    print (ans - count) * 6 + (M - 1) * 6
    print clock() - b


