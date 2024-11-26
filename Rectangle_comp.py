class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h

    def __gt__(self, other):
        return self.area > other.area and ((self.w >= other.w and self.h >= other.h) or (self.w >= other.h and self.h >= other.w))

    def __lt__(self, other):
        # your code here
        return self.area < other.area and ((self.w <= other.w and self.h <= other.h) or (self.w <= other.h and self.h <= other.w))

    def __eq__(self, other):
        # your code here
        return self.area == other.area and ((self.w == other.w and self.h == other.h) or (self.w == other.h and self.h == other.w))

T = int(input())
for t in range(T):
    s = input()
    print(eval(s))