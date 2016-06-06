

def f(n):
    o_f = open('rarb.txt', 'w+')
    s = 0
    k = 1
    d = set()
    while k < n:
        p = 1
        tag = True
        while p * p * k <= n:
            q = p
            while k * q * q * (p + q) * (p + q) <= n:
                ra = k * p * p * (p + q) * (p + q)
                rb = k * q * q * (p + q) * (p + q)
                rc = k * p * p * q * q
                tag = False
                if ra <= rb and rb <= n and (ra, rb, rc) not in d:                    
                    d.add((ra,rb,rc))
                    
                q += 1
            p += 1
        if tag:
            break
        k += 1
    o_f.close()
    print (s)


f(10**7)
    