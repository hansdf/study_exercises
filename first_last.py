#Leetcode 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

nums = [5,7,7,8,8,10]
target = 8


#brute force solution, O(n)
def brute_first_last(nums, target):
    arr_indexes = []
    index1 = 0
    index2 = len(nums)-1
    for num in nums:
        if num == target:
            arr_indexes.append(index1)
            break
        index1 += 1
    
    for num2 in nums[::-1]:
        if num2 == target:
            arr_indexes.append(index2)
            break
        index2 -= 1

    print(arr_indexes)



brute_first_last(nums,target)