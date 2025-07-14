# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

nums = [5,7,7,8,8,10]
target = 8

def find_first_num(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            if nums[mid-1] != target:
                return mid
            else:
                right = mid+1
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
    return -1

def find_last_num(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
    pass


print(find_first_num(nums, target))