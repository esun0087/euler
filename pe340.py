a, b, c = 21**7, 7**21, 12**7
#a, b, c = 50, 2000, 40
#7**11
d = {}
def f(n):
    if n in d:
        return d[n]
    if n > b:
        d[n] = n - c
        return d[n]
    d[n] = f(a + f(a + f(a + f(a + n))))
    return d[n]



#print (iter_d)
mod_data = 10**10
def sum_x(a1, d, n):
    an = a1 + (n-1) * d
    t = (a1 + an) * n // 2
    t = t % mod_data
    return t

def cal():
    #iter_d = f(a+1) - f(1)
    iter_d = -5295770199
    max_iter = (b // a)
    #begin = f(1)
    begin = get_begin(b // (7**11) - 1)
    f_0 = get_f_0(b // (7**11) - 1)
    #print (begin)
    s = 0
    print (max_iter)
    for i in range(max_iter):
        if i % 1000 == 0:
            print (i)
        s += sum_x(begin, 1, a)
        begin = begin + iter_d
    s += sum_x(begin, 1, b % a)
    s += f_0
    print (s, s % (mod_data))

    '''
    for i in range(len(ans)):
        t = ans[i]
        print (i, t)
    '''

def get_f_0(iter_times):
    this_f_0 = 14157885672
    for i in range(iter_times):
        if i % 10 == 9:
            this_f_0 += 14193717480
        else:
            this_f_0 += 7096858740
    return this_f_0
def get_begin(iter_times):
    this_begin = 14157885673
    for i in range(iter_times):
        if i % 10 == 9:
            this_begin += 21290576220
        else:
            this_begin += 14193717480
    return this_begin
def test_1():
    global b
    bs = [b]
    for i in range(400):
        bs.append(bs[-1] + b)
    global d
    data_1 = []
    data_2 = []
    for x in bs:
        b = x
        d = {}
        #data_1.append(f(0))
        data_2.append(f(a+1) - f(1))
    #print (data_1[0])
    
    #for i in range(1, len(data_1)):
    #    print (data_1[i] - data_1[i-1])
    
    for i in range(len(data_2)):
    
        print (data_2[i])
    

import sys

class CrazyFunction():
    def get(self, n, a, b, c):
        if n > b:
            return n - c
        delta = 1 - 4*a + 3*c
        delta_pos, in_delta_pos = divmod(b - n, a) 
        return b - c + 1 - (delta_pos + 1) * delta - in_delta_pos - (a - 1) * delta_pos

    def get_sum(self, a, b, c):
        good_part_count = (b + 1) // a
        good_part_delta = self.get(b - a, a, b, c) - self.get(b, a, b, c)

        good_begin_pos = b - a + 1
        good_end_pos = b
        good_begin_value = self.get(good_begin_pos, a, b, c)
        good_end_value = self.get(good_end_pos, a, b, c)
        good_part_sum = (good_begin_value + good_end_value) * a // 2
        good_sum = (2 * good_part_sum + good_part_delta * (good_part_count - 1) * a) * good_part_count // 2

        rest_begin_pos = 0
        rest_end_pos = b - a * good_part_count
        rest_begin_value = self.get(rest_begin_pos, a, b, c)
        rest_end_value = self.get(rest_end_pos, a, b, c)
        rest_sum = (rest_begin_value + rest_end_value) * (rest_end_pos - rest_begin_pos + 1) // 2

        return rest_sum + good_sum

class Problem():
    def solve(self):
        self.sanity_check()
        self.get()

    def get(self):
        function = CrazyFunction()
        result = function.get_sum(21**7, 7**21, 12**7)
        print(result, result % 10**9)

    def sanity_check(self):
        function = CrazyFunction()
        assert(function.get(0, 50, 2000, 40) == 3240)
        assert(function.get(2000, 50, 2000, 40) == 2040)
        assert(function.get_sum(50, 2000, 40) == 5204240)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())