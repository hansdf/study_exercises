def countdown(i):
    print(i)
    if i <= 0: # Base case
        return 0
    else: # Recursive case
        countdown(i-1)

nums = [2,4,5,6,7,11,15,20,55]
def recursive_sum(numlist): # recursive func to calculate sum of list of numbers
    
    if len(numlist) <= 0: # base case, where it stops recursion
        return 0
    
    return numlist[0] + recursive_sum(numlist[1:]) # add to call stack and continue

# print(recursive_sum(nums))

def recursive_lenght(numlist):
    if len(numlist) == 0:
        return 0
    return 1 + len(numlist[1:])

# print(recursive_lenght(nums))

def recursive_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(recursive_max(nums))
