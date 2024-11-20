from math import sqrt # you may use this function to calculate the area

class Triangle:
    # accepts the three sides of triangle
    def __init__(self, s0, s1, s2):
        # your code here
        self.s0 = s0
        self.s1 = s1
        self.s2 = s2
    # return the perimeter of this triangle.
    @property
    def perimeter(self):
        return self.s0 + self.s1 + self.s2
        # your code here

    # return the area of this triangle.
    @property
    def area(self):
        a = self.s0
        b = self.s1
        c = self.s2
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area
        # your code here


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    side = list(map(int, input().split()))
    t = Triangle(side[0], side[1], side[2])
    print(f'{t.perimeter} {t.area:.2f}')
