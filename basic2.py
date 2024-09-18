def fibonacci(n: int) -> list:
    # In case of n = 1 and n = 2, return 0 or 0, 1
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    n_1 = fibonacci(n - 1) # Using recursion, n_1 is a list of (n - 1) fibonacci numbers
    nth = n_1[-1] + n_1[-2] # defining nth number as (n - 1)th + (n - 2)th number
    
    n_1.append(nth)
    return n_1

# taking input from user
n = input("Enter n: ")

# error handling for type conversion
try:
    n = int(n)
    print(", ".join(map(str,fibonacci(n)))) if (n > 0) else print("Error: Input cannot be negative")
except ValueError:
    print("Error: Invalid input")
