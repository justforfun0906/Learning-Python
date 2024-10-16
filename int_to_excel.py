cases = int(input())
for i in range(1,cases+1):
    x = int(input())
    f = int(x//26)
    s = int(x%26)
    ans = ''
    while x > 0:
        x-=1
        ans += chr(ord('A')+x%26)
        x//=26
    print(f"Case #{i}: {ans[::-1]}")