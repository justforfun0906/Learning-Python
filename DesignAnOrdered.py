class OrderedStream:
    def __init__ (self, n: int):
        self.list = [None]* (n+1)
        self.pointer = 0
    def insert(self, id: int, value: str):
        id -= 1
        self.list[id] = value
        if self.list[id] == None:
            return []
        else:
            ret_val = []
            while self.list[self.pointer] != None and self.pointer < len(self.list):
                ret_val.append(self.list[self.pointer])
                self.pointer += 1
            return ret_val

stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))
    