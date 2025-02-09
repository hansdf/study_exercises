#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays. Return the array ans.

def conc_array(nums): # two iterations, O(n)? / Could be better optimized for a single pass through
    len_nums = len(nums)
    ans = []
    len_ans = len_nums*2
    for n in nums:
        ans.append(n)
    for n in nums:
        ans.append(n)
    print(ans)
    return ans


conc_array([1,3,2,1])