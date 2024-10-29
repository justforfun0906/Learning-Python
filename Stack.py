summation = 0
stack = None
def top():
    global stack
    return stack[-1]
def pop():
    global stack
    global summation
    summation -= (stack[-1]*stack[-1])
    stack.pop(-1)
    return None
def push(val):
    global stack
    global summation
    stack.append(val)
    summation += (val*val)
    return None
def init():
    global stack
    global summation
    stack = []
    summation = 0
    return None
def getSquareSum():
    global summation
    return summation