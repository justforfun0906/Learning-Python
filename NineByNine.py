def get_products(a=1,b=9,c=1,d=9):
    #a,b = range of first number
    #c,d = range of second number
    ans = []
    for i in range(a,b+1):
        for j in range(c,d+1):
            ans.append(i*j)
    return ans