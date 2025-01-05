cases = int(input())
for case in range(1, cases+1):
    li = [int(x) for x in input().split()]
    cnt = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                cnt += 1
    print(f"Case #{case}: {cnt}")   