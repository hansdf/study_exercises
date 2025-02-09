# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

testcase = [2,1,4,1,2,4,1,2,7,1,2,4]

def single_number(nums): #hashmap - O(n+n?)
    counter_hash = {}
    for num in nums:
        if num not in counter_hash:
            counter_hash[num] = 1
        else:
            counter_hash[num] += 1
    print(counter_hash)
    for key in counter_hash:
        print(key, "->", counter_hash[key])
        if counter_hash[key] < 2:
            print(f"{key} is the element that appears a single time")


single_number(testcase)

