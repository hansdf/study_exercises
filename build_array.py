#Leetcode 1920 - Build Array from Permutation
#Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
#A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

nums = [5,0,1,2,3,4]

def build_array(numbers_list):
    ans = []
    for num in numbers_list:
        ans.append(numbers_list[num])
    
    print(ans)
    return ans


build_array(nums)