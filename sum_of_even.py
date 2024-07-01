# Write program to calculate and print the sum of all even numbers from 1 to 100. (2 + 4 + 6 + 8 ...)

sum_counter = 0

for num in range(1, 101):
    if num % 2 == 0:
        sum_counter += num

print(sum_counter)