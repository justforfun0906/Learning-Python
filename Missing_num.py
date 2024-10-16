cases = int(input())
for case in range(1, cases+1):
    li = [int(x) for x in input().split()]
    n = len(li)
    missing = 0
    for i in range(1, n+1):
        if i not in li:
            missing = i
            break
    print(f"Case #{case}: {missing}")