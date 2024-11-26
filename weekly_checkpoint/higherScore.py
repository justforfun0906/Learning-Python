class Player:
    id = 1
    def __init__(self):
        self.record = []
        self.id = Player.id
        self.score = 0
        Player.id += 1
        #print("INIT", self.id)
    def add(self, val):
        #update the record and score
        val = int(val)
        self.score = sum(self.record) + pow(val, len(self.record))
        #print(f"{sum(self.record)} + {pow(val, len(self.record))} = {self.score}")
        self.record.append(val)
    def getval(self):
        return len(self.record)
    def getpoly(self):
        return self.score

n = int(input())
p1 = Player()
p2 = Player()
for i in range(n):
    player, value = input().split()
    if int(player) == 1:
        p1.add(int(value))

    else:
        p2.add(int(value))

#choose the winner
winner = None
if int(player) == 1:
    p1.add(int(value))
else:
    p2.add(int(value))

#choose the winner
if p1.getpoly() > p2.getpoly():
    winner = "1"
elif p1.getpoly() < p2.getpoly():
    winner = "2"
else:
    if len(p1.record) > len(p2.record):
        winner = "1"
    elif len(p1.record) < len(p2.record):
        winner = "2"
    else:
        winner = "DRAW"

print(winner)