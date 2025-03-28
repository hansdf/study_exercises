# 1827. Minimum Operations to Make the Array Increasing
# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

 
nums1 = [1,1,1] #Output: 3

nums2 = [1,5,2,4,1] #Output: 14

def minOperations(nums):
    if len(nums) == 1:
        return 0
    counter = 0

    i=0
    while i < len(nums)-1:
        print(f"nums: {nums}")
        print(f"nums[i]: {nums[i]}")
        print(f"nums[i+1]: {nums[i+1]}")

        if nums[i] >= nums[i+1]:
            nums[i+1] += 1
            counter += 1
            continue

        i +=1

    print("final counter: ", counter)
    return counter

minOperations(nums2)