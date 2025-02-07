# Write function to calculate and print the sum of all even numbers from 1 to 100. (2 + 4 + 6 + 8 ...)

def sum_of_even(max):
    sum_counter = 0
    for num in range(1, max):
        if num % 2 == 0:
            sum_counter += num
    print(sum_counter)

# sum_of_even(100)

# Sum of Even Numbers in a List
# Problem: Return the sum of all even numbers in a given list.

def sum_even_list(nums):
    sums = 0
    for n in nums:
        pass


numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

sum_even_list(numlist)