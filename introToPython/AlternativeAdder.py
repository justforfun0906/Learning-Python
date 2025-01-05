def adder (*args):
    if len(args) == 0:
        return 0
    else:
        ans = 0
        for i in range(0, len(args)):
            if(i % 2 == 0):
                ans += int(args[i])
            else :
                ans -= int(args[i])
        return ans