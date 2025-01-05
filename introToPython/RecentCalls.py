class RecentCounter:

    def __init__(self):
        self.calls = []
    def ping(self, t):
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.pop(0)
        return len(self.calls)

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(1,T+1):
    counter = RecentCounter()
    calls = list(map(int,input().split()))
    for ind,time in enumerate(calls):
        print(f'Case #{t}_{ind}: {counter.ping(time)}')