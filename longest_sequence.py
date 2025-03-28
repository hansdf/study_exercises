# Leetcode 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

exe1 = [100,4,200,1,3,2] # Output: 4

exe2 = [0,3,7,2,5,8,4,6,0,1] # Output: 9

def findLongestSeq(nums):
    if not nums:
        return 0  # Edge case: empty list

    numset = set(nums)  # O(n) space and time to create the set
    longest = 0

    for num in numset:  # O(n) since we iterate each unique number once
        if num - 1 not in numset:  # Start of a new sequence
            current_length = 1
            while num + 1 in numset:  # Expand sequence
                num += 1
                current_length += 1
            longest = max(longest, current_length)

    return longest



print(findLongestSeq(exe1))