cases = int(input())
for i in range(1, cases + 1):
    li = [int(x) for x in input().split()]
    carry = 1
    for j in range(len(li) - 1, -1, -1):
        li[j] += carry
        carry = li[j] // 10
        li[j] = li[j] % 10
    if carry > 0:
        li.insert(0, carry)
    print(f"Case #{i}: {li}")