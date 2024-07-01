nums = [10, 5, 8, 20, 300, 99, 150, 2, 10]

def find_largest(list_of_nums):
    largest_so_far = 0
    for num in list_of_nums:
        if num > largest_so_far:
            largest_so_far = num  
    print(largest_so_far)

find_largest(nums)
