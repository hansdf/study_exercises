
def find_factorial(number):
    factorial = 1
    for num in range(1, number+1):
        if number <= 1:
            print(f"factorial of {number} is {factorial}")
        else:
            factorial = factorial * num
    print(f"factorial of {number} is {factorial}")


find_factorial(5)
            