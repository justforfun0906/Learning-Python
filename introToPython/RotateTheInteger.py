testcases = int(input())
for i in range(testcases):
    x = int(input())
    #turn the integer into a string of its binary representation
    binary = "{:08b}".format(x)
    #make its len = 8
    #rotate the string
    binary = binary[1:] + binary[:1]
    #turn it back into an integer
    answer = int(binary, 2)
    print("Case #{}: {}".format(i+1, answer))