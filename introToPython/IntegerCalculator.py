def evaluate(expr):
    # Evaluate the expression and return the result as an integer
    try:
        # Use eval to evaluate the expression
        result = eval(expr)
        return int(result)
    except Exception as e:
        # In case of any error, return None or handle it as needed
        return None

# Note that the following code is for local testing purposes only.
# You should leave this part of code unchanged and not submit it to the OJ system.
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        result = evaluate(input().strip())
        print(result)