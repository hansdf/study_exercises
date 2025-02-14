#Leetcode 2011 - Final Value of Variable After Performing Operations
#There is a programming language with only four operations and one variable X:
    #++X and X++ increments the value of the variable X by 1.
    #--X and X-- decrements the value of the variable X by 1.
#Initially, the value of X is 0.
#Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

operations = ["--X","X++","X++"]

def calculate_value(operations_list):
    x = 0
    for num in range(0, len(operations)):
        #print(operations_list[num])
        if operations_list[num] == "X++" or operations_list[num] == "++X":
            x += 1

        if operations_list[num] == "X--" or operations_list[num] == "--X":
            x -= 1
        
        print(x)

    

calculate_value(operations)