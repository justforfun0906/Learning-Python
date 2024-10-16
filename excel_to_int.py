cases = int(input())
for case in range(1,cases+1):
    st = input()
    num = 0
    for ch in st:
        num = num*26 + ord(ch)-ord('A')+1
    print(f"Case #{case}: {num}")