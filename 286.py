def    calMatrix(M, q, matrix):
    matrix[1][0], matrix[1][1] = 1.0 / q, 1 - 1.0 / q
    for x in xrange(2, M+1):
        for score in xrange(x+1):
            if score > 0:
                matrix[x][score] = matrix[x-1][score] * float(x) / q +\
                        matrix[x-1][score-1] * (1 - float(x) / q)
            else:
                matrix[x][score] = matrix[x-1][score] * float(x) / q

def test():
    #52.6494571953
    M, q = 50, 60
    left, right = 50, 60
    while True:
        q = (left + right) / 2.0
        matrix = [[0 for i in xrange(M+1)] for j in xrange(M+1)]
        calMatrix(M, q, matrix)
        if abs(matrix[50][20] - 0.02) <= 0.0000000001:
            print matrix[50][20]
            break
        if matrix[50][20] > 0.02:
            left = (left + right) / 2.0
        if matrix[50][20] < 0.02:
            right = (left + right) / 2.0
        print matrix[50][20]

def test1():
    M, q = 50, 51
    matrix = [[0 for i in xrange(M+1)] for j in xrange(M+1)]
    calMatrix(M, q, matrix)
    print matrix[50][20]
test()
