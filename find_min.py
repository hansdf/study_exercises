nums = [7, 4, 3, 100, 2343243, 343434, 4, 1, 32]

def find_minimum(lst):
    min_number = float("inf")
    for num in lst:    
        if num <= min_number:
            min_number = num
    print(min_number)

find_minimum(nums)