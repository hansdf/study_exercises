# Multiply two integers without using multiplication, division and bitwise operators

5 * 6 # 6 times the number 5

def multiply_loop(x,y):
    total = 0
    for i in range(y):
        total = total + x
    print(total)

multiply_loop(5,5)

def multiply_recursive(x,y):
    pass