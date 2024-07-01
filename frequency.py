# Question 5: Write a Python program to count the frequency of each element in a list.

nums = [10, 5, 8, 20, 300, 99, 150, 2, 10, 10, 10, 5, 20, 5, 300, 99]

def count_frequency(list_of_nums):
    dict_counter = {}

    for num in list_of_nums:
        if num not in dict_counter:
            dict_counter[num] = 1
        else:
            dict_counter[num] += 1
        
    print(dict_counter)
    
count_frequency(nums)