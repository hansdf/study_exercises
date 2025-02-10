#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first. 

nums = [3,4,5,6,7]
target = 13

def two_sum_brute_force(numlist, target): # O(n^2)
    for n1 in range(len(numlist)):
        for n2 in range(len(numlist)):
            if numlist[n1] + numlist[n2] == target:
                print("found at indexes: ", n1, n2)
                return n1, n2


two_sum_brute_force(nums,target)