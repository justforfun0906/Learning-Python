class Matrix:
    # size: a integer represented the size of the square matrix
    # m: the matrix represented in the 2-d list format
    # create a square matrix
    def __init__(self, size, m):
        # your code here
        self.size = size
        self.m = m[:][:]

    # create a new Matrix with the value of current matrix + rhs matrix
    def __add__(self, rhs):
        size = self.size
        return Matrix(size, [[self.m[i][j] + rhs.m[i][j] for j in range(size)] for i in range(size)])
        # your code here

    # create a new Matrix with the value of current matrix - rhs matrix
    def __sub__(self, rhs):
        # your code here
        size = self.size
        return Matrix(size, [[self.m[i][j] - rhs.m[i][j] for j in range(size)] for i in range(size)])

    # create a new Matrix with the value of current matrix * rhs matrix
    def __mul__(self, rhs):
        # your code here
        size = self.size
        return Matrix(size, [[sum([self.m[i][k] * rhs.m[k][j] for k in range(size)]) for j in range(size)] for i in range(size)])

    # output format of Matrix
    def __repr__(self):
        return '\n'.join([' '.join(map(str, self.m[i])) for i in range(self.size)])

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    k = int(input())
    m1_list = []
    for _ in range(k):
        m1_list.append(list(map(int, input().split())))

    m2_list = []
    for _ in range(k):
        m2_list.append(list(map(int, input().split())))

    m1 = Matrix(k, m1_list)
    m2 = Matrix(k, m2_list)
    print(m1+m2)
    print(m1-m2)
    print(m1*m2)
