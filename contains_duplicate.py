# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7]

# bruteforce solution = O(n^2)
def check_dupli(numlist):
    for n in numlist:
        counter = 0
        for i in numlist:
            if n == i:
                counter += 1
            if counter > 1:
                return True
    return False

# hashmap approach = O(n)?
def hashmap_check_dupli(numlist):
    hash_counter = {}
    for n in numlist:
        if n not in hash_counter:
            hash_counter[n] = 1
        else:
            hash_counter[n] += 1
    for key in hash_counter:
        # print(key, "->", hash_counter[key])
        if hash_counter[key] > 1:
            return True
    return False


print(hashmap_check_dupli(nums))