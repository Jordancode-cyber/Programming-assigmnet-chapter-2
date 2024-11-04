# Function to calculate the GCD using Euclid's algorithm
def gcd(m, n):
    while m != 0:
        m, n = n % m, m
    return n

# Get user input
try:
    m = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    result = gcd(m, n)
    print(f"The GCD of {m} and {n} is: {result}")
except ValueError:
    print("Please enter valid integers.")
