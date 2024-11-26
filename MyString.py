class MyString(str):
    def __lshift__(self,val):
        #Your code here
        val = int(val)
        time = val % len(self) if len(self) != 0 else 0
        return self[time:] + self[:time]
    def __rshift__(self,val):
        #Your code here
        val = int(val)
        time = val % len(self) if len(self) != 0 else 0
        return self[-time:] + self[:-time]