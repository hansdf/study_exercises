# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

def get_alternates(numlist):
    new_arr = []
    for n in range(0,len(numlist),2):
        new_arr.append(numlist[n])
    return new_arr

print(get_alternates([1, 2, 3, 4, 5, 6, 7]))