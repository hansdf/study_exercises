numslist = [5, 3, 6, 15, 10, 1, 7, 22]

def findSmallest(arr): 
    smallest = arr[0] # Stores the smallest value 
    smallest_index = 0 # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Now you can use this function to write selection sort:
def selectionSort(arr): #Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# print(selectionSort(numslist))


def find_smallest_num_index(nums):
    smallest = float("inf")
    index_smallest = 0
    index = 0
    for num in nums:
        if num < smallest:
            smallest = num
            index_smallest = index
        index += 1
    return index_smallest


def selection_sort(nums):
    sorted_array = []

    for num in range(len(nums)):
        smol = find_smallest_num_index(nums)
        sorted_array.append(nums.pop(smol))
    return sorted_array


print(selection_sort(numslist))


