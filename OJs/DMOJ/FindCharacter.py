t = int(input())
for i in range(t):
    x = i + 1
    data = input().split()
    str = data[0]
    c = data[1]
    ans = -1
    for j in range(len(str)):
        if str[j] == c:
            ans = j
            break
    print("Case #%d: %d" % (x, ans)) 
    