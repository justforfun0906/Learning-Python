cases = int(input())
for i in range(1, cases+1):
    li1 = [int(s) for s in input().split()]
    li2 = [int(s) for s in input().split()]
    set1 = set(li1)
    set2 = set(li2)
    inter_set = set1.intersection(set2)
    li_inter = list(inter_set)
    li_inter.sort()
    print(f"Case #{i}: {li_inter}")