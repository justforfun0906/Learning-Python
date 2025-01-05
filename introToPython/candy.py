cases = int(input())
for i in range(1,cases+1):
    in_li = [int(x) for x in input().split()]
    n = len(in_li)
    set_li = set(in_li)
    ans = min(int(n/2), len(set_li))
    print(f"Case #{i}: {ans}")