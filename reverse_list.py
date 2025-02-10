#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

input_string = ["h","e","l","l","o"]

def reverse_string(text): #two pointer approach
    #text.reverse() #only works for arrays
    left = 0
    right = len(text)-1

    print("start:",left,"/ end:", right)

    while left < right:
        text[left], text[right] = text[right], text[left]
        left+=1
        right-=1
    print(text)


reverse_string(input_string)