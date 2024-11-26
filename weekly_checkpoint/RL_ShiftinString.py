class csstr(str):
    def __init__(self, in_str):
        self.str = in_str
    #overload >> operator
    def __rshift__(self, input):
        time = int(input) % len(self.str)
        #right shift the string for time
        return self.str[-time:] + self.str[:-time]
    #overload << operator
    def __lshift__(self, input):
        time = int(input) % len(self.str)
        #left shift the string for time
        return self.str[time:] + self.str[:time] 

T = int(input())
for t in range(T):
    print(eval(input()))