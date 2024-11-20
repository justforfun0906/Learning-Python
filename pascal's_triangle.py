def pascal(row, col):
    if col == 0 or row == col:
        return 1
    return pascal(row - 1, col - 1) + pascal(row - 1, col)
def print_pascal(n):
    for i in range(n):
        for j in range(i + 1):
            print(f'{pascal(i,j):3d}', end = '')
        print()
