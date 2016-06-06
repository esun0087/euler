'''

'''
from math import sqrt

def get_prime(M, N):
    prime = []
    for i in open('prime.txt'):
        if int(i) >= M and int(i) <= N:
            prime.append(int(i))
        if int(i) >= N:
            break
    return prime

def get_next_data(x):
    x = list(str(x))
    x = [int(i) for i in x]
    return sum(x)

def max_way(x):
    if x in d:
        return d[x]
    else:
        if x <= 9:
            return open_close_digital(x, 'close')
        else:
            sqrtx = get_next_data(x)
            d[x] = cal_this_cost(x, sqrtx) + max_way(sqrtx)
            return d[x]

def cal_this_cost(x, sqrtx):
    xlist, sqrtxlist = list(str(x)), list(str(sqrtx))
    xlist.reverse(); sqrtxlist.reverse()
    lenx = len(sqrtxlist)
    count = 0
    for i in xrange(lenx):
        diff = cal(int(xlist[i]), int(sqrtxlist[i]))
        count += diff
    iLast = len(xlist) - len(sqrtxlist)
    for i in xrange(len(sqrtxlist), len(xlist)):
        s = bin(digital[int(xlist[i])])
        count += s.count('1')
    return count

def cal(a, b):
    data = digital[a] ^ digital[b]
    data = str(bin(data))
    return data.count('1')

def open_close_digital(x, opt = 'close'):
    if x < 10:
        return bin(digital[x]).count('1')
    xlist = list(str(x))
    count = 0
    for i in xlist:
        s = bin(digital[int(i)])
        count += s.count('1')
    return count

def sam_need(prime):
    count = 0
    for p in prime:
        count += sam_way(p)
    return count

def sam_way(x):
    count = 0
    while x >= 10:
        count += open_close_digital(x) * 2
        x = get_next_data(x)
    return open_close_digital(x) * 2 + count

def max_need(prime):
    count = 0
    for p in prime:
        count += open_close_digital(p) + max_way(p)
    return count

if __name__ == '__main__':
    M, N = 10 ** 7, 2 * 10**7
    d = {}
    digital = {0:int('00111111',2),  1:int('00000011',2), 
           2:int('01101101', 2), 3:int('01100111', 2),
           4:int('01010010', 2), 5:int('01110110', 2),
           6:int('01111110', 2), 7:int('00110011', 2),
           8:int('01111111', 2), 9:int('01110111', 2)}
    
    prime = get_prime(M, N)
    a = max_need(prime)
    d = {}
    b = sam_need(prime)
    print a - b

