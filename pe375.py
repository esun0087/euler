def repeat_n():

    s0 = 290797 
    s = set([s0])
    seq = [s0]
    while 1:
        s0 = (s0 * s0) % 50515093
        if s0 in s:
            break
        s.add(s0)
        seq.append(s0)
    print (len(s))
    return seq
def get_min(i, j):
    
    
repeat_n()
