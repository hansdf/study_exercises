# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

testcase = [-4,-2,1,4,8]

def find_closest_number(nums):
    closest = nums[0] 
    for num in nums:
        if abs(num) < abs(closest): # Absolute value, such that -4 and 4 are = 4
            closest = num

    if closest < 0 and abs(closest) in nums: # closest value less than 0 and absolute value of closest is in the nums array 
        return abs(closest)
    else:
        return closest 
    
print(find_closest_number(testcase))