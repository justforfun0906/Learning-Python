# import random
# ans = random.randint(1,100)
# while (temp:=int(input())) !=ans:
#     if(temp<ans):
#         print("bigger")
#     if(temp>ans):
#         print("smaller")
#     if(temp==-1):
#         print(ans)
# print("bingo")
# arr = [1,2,3,4,5]
# for i,val in enumerate(arr):
#     print(i, val, sep=': ')
# for i in range(m=input(), n=input(), m):
#     print(i)
m = int(input())
for i in range(0,m+1):
    print(' '*(m-i)+'*'*(2*i-1))
for i in range (m, -1, -1):
    print(' '*(m-i)+'*'*(2*i-1))
        