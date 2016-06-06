'''
(x-n/2) ** 2 + (y-n/2) ** 2 = n** 2 / 2
'''
from math import sqrt
from time import clock
sqrt2 = sqrt(2)
def get_y(x, n):
	return sqrt((n ** 2 / 2 - (x - n/2.0) ** 2)) + n / 2.0

def get_n(n):
	x = n / 2.0
	count = 0
	while  x <= n / 2.0 * (1 + sqrt2):
		y = get_y(x, n)
		if int(x) == x and int(y) == y:
			count += 1
		x += 1
	return count

if __name__ == '__main__':
        start = clock()
        print get_n(10**7) * 4
        print clock() - start
