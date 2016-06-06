import sys

seq = {1:1}
n = int(sys.argv[1])
count_seq = [0 for i in range(n+1)]
for i in range(n):
    tmp_seq = {}
    tag = False
    for x in seq:
        for y in range(2, n+1):
            if x * y > n:
                break
            tag = True
            t = x * y
            if t not in tmp_seq:
                tmp_seq[t] = 0
            tmp_seq[t] += seq[x]
            count_seq[t] += seq[x]
    if not tag:
        break
    seq = tmp_seq

for i, c in enumerate(count_seq):
    if i == c:
        print (i, c, end = ' ')
        input()