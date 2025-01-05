cases = int(input())
for i in range(1,cases+1):
    target = int(input())
    in_li = [int(x) for x in input().split()]
    for x in range(len(in_li)):
        for y in range(x+1,len(in_li)):
            if in_li[x] + in_li[y] == target:
                print(f"Case #{i}: {[x,y]}")
                break