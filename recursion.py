def countdown(i):
    print(i)
    if i <= 0: # Base case
        return 0
    else: # Recursive case
        countdown(i-1)


print(countdown(15))