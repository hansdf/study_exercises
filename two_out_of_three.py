# Leetcode 2032. Two Out of Three
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
# Output expected: [3,2]

def twoOutOfThree(nums1, nums2, nums3):
    returnArr = []
    counter = {1:}
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    set4 = set1|set2|set3

    print(set4)


twoOutOfThree(nums1,nums2,nums3)




