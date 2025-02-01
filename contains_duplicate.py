# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

nums = [1, 2, 3, 4, 5, 5]

#bruteforce solution = O(n^2)
def check_dupli(numlist):
    for n in numlist:
        counter = 0
        for i in numlist:
            if n == i:
                counter += 1
            if counter > 1:
                return True
    return False

print(check_dupli(nums))