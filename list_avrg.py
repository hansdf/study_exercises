# Get the average from a list of numbers. The average is the sum of all the numbers divided by the amount of items.

nums = [10, 5, 8, 20, 300, 99, 150, 2, 10, 10, 10, 5, 20, 5, 300, 99]

def list_average(nums):
    counter = 0
    if nums == []:
        return None

    for num in nums:
        counter = num + counter

    average = counter / len(nums)

    print(f"The average of all numbers in the list is {average}")

list_average(nums)