def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Take input from user
number = int(input("Enter a number to calculate its factorial: "))

# Calculate and print the factorial
print(f"The factorial of {number} is {factorial(number)}")
