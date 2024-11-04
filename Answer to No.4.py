# Function to generate the Syracuse sequence
def syracuse_sequence(x):
    if x <= 0:
        return "Please enter a natural number (positive integer)."
    
    sequence = [x]
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    
    return sequence

# Get user input
try:
    start_value = int(input("Enter a natural number to start the Syracuse sequence: "))
    result = syracuse_sequence(start_value)
    print("The Syracuse sequence is:", result)
except ValueError:
    print("Please enter a valid integer.")
