import math

nums = [3, 13, 2, 34, 11, 26, 47, 99]

def find_median(list_of_nums):
    if len(list_of_nums) % 2 != 0:
        sorted_list = sorted(list_of_nums)
        print(sorted_list)
        median = math.floor(len(sorted_list) / 2)
        print(sorted_list[median])
    else:
        sorted_list = sorted(list_of_nums)
        print(sorted_list)
        half = int(len(sorted_list) / 2)
        median = (int(sorted_list[half]) + int(sorted_list[half-1])) / 2
        print(median)


        

find_median(nums)
