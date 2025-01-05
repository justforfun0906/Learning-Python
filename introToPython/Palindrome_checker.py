cases = int(input())
for i in range(1,cases+1):
    in_str = input()
    li = in_str.split()
    #print(li)
    rev_li = list(reversed(li))
    #print(rev_li)
    if li == rev_li:
        print("Case #{}: Yes".format(i))
    else:
        print("Case #{}: No".format(i))
