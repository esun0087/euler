from copy import *

def getPrime(M):
    prime = [0] * M
    for i in open('prime.txt'):
        if int(i) < M:
            prime[int(i)] = 1
        else:
            break
    return prime
def getArray(pos, M):
    array = [0] * M
    array[pos] = 1
    d = {}
    p = 2 / 3.0
    for cycle in xrange(15):
        arrayTmp = [0 for i in xrange(M)]
        dtmp = {}
        for i in xrange(1, M):
            if array[i] > 0:
                if d == {}:
                    if prime[i] == True:
                        dtmp['P'] = array[i] * p
                        dtmp['N'] = array[i] * (1 - p)
                    else:
                        dtmp['P'] = array[i] * (1 - p)
                        dtmp['N'] = array[i] * p
                else:
                    for data in d:
                        if prime[i] == True:
                            if (data+'P') not in dtmp:
                                dtmp[data + 'P'] = array[i] * p * d[data]
                            else:
                                dtmp[data + 'P'] += array[i] * p * d[data]
                            if (data+'N') not in dtmp:
                                dtmp[data + 'N'] = array[i] * (1 - p) * d[data]
                            else:
                                dtmp[data + 'N'] += array[i] * (1 - p) * d[data]
                        else:
                            if (data+'P') not in dtmp:
                                dtmp[data + 'P'] = array[i] * (1 - p) * d[data]
                            else:
                                dtmp[data + 'P'] += array[i] * (1 - p) * d[data]
                            if (data+'N') not in dtmp:
                                dtmp[data + 'N'] = array[i] * p * d[data]
                            else:
                                dtmp[data + 'N'] += array[i] * p * d[data]
            if i == 1:
                arrayTmp[i+1] += array[i]
                array[i] = 0;
            if i == M - 1:
                arrayTmp[i-1] += array[i]
                array[i] = 0
            else:
                arrayTmp[i-1] += array[i] * 1 / 2.0
                arrayTmp[i+1] += array[i] * 1 / 2.0
        
        array = copy(arrayTmp)
        d = copy(dtmp)
    
    return d['PPPPNNPPPNPPNPN']
M = 501
prime = getPrime(M)
def test():
    s = 0
    for pos in xrange(1, M):
        s += getArray(pos, M)
    print s
test()


            
        
        
