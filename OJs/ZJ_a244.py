t = input()
t= int(t)
for i in range(t):
    the_str = input()
    a, b, c= the_str.split()
    a, b, c= int(a), int(b), int(c)
    if a==1:
        print(b+c)
    elif a==2:
        print(b-c)
    elif a==3:
        print(b*c)
    else:
        print(int(b/c))
