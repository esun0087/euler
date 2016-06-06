def get_lat_digit(digits):
    state = [1, -1]
    index = 0
    step = state[index]
    s = 0
    while len(digits) > 1:
        digits = digits[::step]
        digits = digits[1::2]
        digits = digits[::step]
        index = 1 - index
        step = state[index]
        s += 1
    return digits[0]

def test(n):
    for k in range(2, n+1, 2):
        a = get_lat_digit([i for i in range(1, k+1)])
        print (k, a)

#get_lat_digit([i for i in range(1, 10)])
test(1000)