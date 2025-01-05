from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
l,r = input().split()
l = int(l)
r = int(r)
ans = []
for i in range(r, l-1, -1):
    if is_prime(i):
        ans.append(i)
print(ans)