from statistics import mean # you may use this function to find the average of a list of number

def average(scores):
    # your code here
    # scores is a list of lists
    # after unziping the list of lists, we can find the average of each list
    avg = list(map(mean, zip(*scores)))
    return avg

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    k = int(input())
    scores = [map(int, input().split()) for _ in range(k)]
    avers = average(scores)
    for m in avers:
        print(f'{m:.2f}', end=' ')
    print()
