
from itertools import permutations
def generate_permution(s):
    return set(''.join(i) for i in permutations(s))
        
    


def f(n):
    i_c = 0
    s = 'project'
    permutions = generate_permution(s)
    extend_s = {'':0}
    mod = 10**9
    while i_c < n:
        print (i_c)
        new_extend = {}
        for e_s in extend_s:
            for i in s:
                ex_s = e_s + i
                if len(ex_s) == 7:
                    if not ex_s in permutions:
                        if ex_s[1:] not in new_extend:
                            new_extend[ex_s[1:]] = 0
                        new_extend[ex_s[1:]] += 1
                        if new_extend[ex_s[1:]] > mod:
                            new_extend[ex_s[1:]] %= mod
                if len(ex_s) < 7:
                    if ex_s not in new_extend:
                        new_extend[ex_s] = 0
                    new_extend[ex_s] += 1
                    if new_extend[ex_s] > mod:
                        new_extend[ex_s] %= mod
        extend_s = new_extend
        i_c += 1
        
    print (sum(extend_s.values()))
        
f(10**12)