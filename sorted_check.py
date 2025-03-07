# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

arr = [90, 80, 100, 70, 40, 30]
arr2 = [10, 20, 30, 40, 50]

def sort_check(numlist):

    for i in range(len(numlist)):
        if numlist[i+1] < numlist[i]:
            return False
        else:
            return True
        
print(sort_check(arr))
