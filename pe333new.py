from itertools import *

isprime = [n%2==1 for n in range(1000000)]
isprime[1] = False
isprime[2] = True
for n in range(3, 1000000, 2):
	if isprime[n]:
		for m in range(2*n, 1000000, n):
			isprime[m] = False

P = {2:1, 3:1}

three = [3**(n+1) for n in range(12)]
two = [2**(19-n) for n in range(19)]

for n in range(1, 13):
	print (n)
	for x in combinations(three, n):
		for y in combinations(two, n):
			z = sum(map(lambda a, b: a*b, (1,)+x, y+(1,)))
			if z < 1000000 and isprime[z]:
				if z not in P: P[z] = 0
				P[z] += 1

print (sum([n for n in P if P[n] == 1]))