# Read input values
input_line = input().strip()

# Parse the input values
x_str, y_str, decimal_places_str = input_line.split()
x = float(x_str)
y = float(y_str)
decimal_places = int(decimal_places_str)

# Multiply the two floats
result = x * y

# Round the result to the specified number of decimal places
rounded_result = round(result, decimal_places)

# Format the output string
output = f"{x} * {y} equals to {rounded_result:.{decimal_places}f}"

# Print the formatted string
print(output)