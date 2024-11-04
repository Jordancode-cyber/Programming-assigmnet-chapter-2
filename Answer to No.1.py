# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
# Get user input
try:
    n = int(input("Enter the position (n) of the Fibonacci sequence you want to compute: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
except ValueError:
    print("Please enter a valid integer.")
