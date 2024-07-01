# Find the median item in a list
# The median is the item in the middle, not the average. If the list has an odd number of items, the median is the two in the middle, added and divided by 2.

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
