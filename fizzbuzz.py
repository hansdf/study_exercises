# The FizzBuzz problem  requires writing a function that prints numbers from 1 to a given limit, but with a twist:
    #For multiples of 3, print "Fizz" instead of the number.
    #For multiples of 5, print "Buzz" instead of the number.
    #For numbers which are multiples of both 3 and 5, print "FizzBuzz".

def fizzbuzz(num_end):
    for num in range(1, num_end+1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

def fizzbuzz_string(num_end): # string approach
    for num in range(1, num_end+1):
        fizzbuzz_s = ""
        if num % 3 == 0:
            fizzbuzz_s += "fizz"
        if num % 5 == 0:
            fizzbuzz_s += "buzz"
        elif num % 5 != 0 and num % 3 != 0:
            fizzbuzz_s += str(num)
        print(fizzbuzz_s)
    

# fizzbuzz(35)

fizzbuzz_string(15)