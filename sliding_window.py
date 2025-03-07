# Leetcode 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest without duplicate characters.

s = "abcabcbb" # The answer is "abc", with the length of 3.

def find_longest_substring(string):
    longest = 0 # highest valid substring lenght found
    l = 0 # left pointer




    return longest



# Maximum Sum Subarray of Size K
# Problem: Given an array of integers and a positive integer k, find the maximum sum of any contiguous subarray of size k.

def max_sum_window(nums, arr_size):
    curSum = 0
    maxSum = 0
    left = 0
    for right in range(len(nums)):
        curSum = curSum + nums[right]
        
        if right >= arr_size-1:
            maxSum = max(curSum, maxSum)
            curSum -= nums[left]
            left += 1
    
    return maxSum


arr = [2, 1, 5, 1, 3, 2]
k = 2


print(max_sum_window(arr, k))
        