
import codecs
n = 10**8
primes = []
for i in codecs.open('prime.txt', 'r', 'utf-8'):
    if int(i.strip()) < n:
        primes.append(int(i))
    else:
        break

print ('read primes over')
d = {}
for i, p in enumerate(primes):
    if i % 100 == 0:
        print (i, p)
    k = 0
    for kk in range(p, n+1, p):
        x = kk
        while x > 0 and x % p == 0:
            x //= p
            k += 1
            if p**k > n:
                break
            d[p**k] = kk
        if p**k > n:
            break
print ('d cal over')
def divisior(x):
    ans = -1
    for i, p in enumerate(primes):
        if x < p or x <= 1:
            break
        if x % p == 0:
            k = p
            while x % k == 0:
                k *= p
            k //= p
            x //= k
            if ans == -1:
                ans = d[k]
            else:
                ans = max(d[k], ans) 
    return ans            

def cal():
    s = 0
    for i in range(2, n+1):
        if i % 1000 == 0:
            print (i)
        s += divisior(i)
    print (s)
    
def cal_2():
    myans = [0 for i in range(n+10)]
    for i_i, p in enumerate(primes):
        if i_i % 100 == 0:
            print(i_i, p)
        for i in range(p, n+1, p):
            x = i
            k = p
            while x%k == 0:
                k *= p
            k //= p
            if myans[i] == 0:
                myans[i] = d[k]
            else:
                myans[i] = max(myans[i], d[k])
    print (sum(myans))
cal_2()
