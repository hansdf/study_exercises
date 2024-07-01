# Question 9: Write a Python program to find the second largest number in a list.

nums = [10, 5, 8, 20, 300, 99, 150, 2, 10]

def find_second_largest(nums_list):
    largest = 0
    second_largest = 0

    for num in nums_list:
        if num >= largest:
            largest = num
        elif num > second_largest and second_largest < largest:
            second_largest = num

    print(f"{largest} is the largest number")
    print(f"{second_largest} is the second largest number")


find_second_largest(nums)