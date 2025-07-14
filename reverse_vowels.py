
# Leetcode 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

string_example = "IceCreAm" # Output: "AceCreIm"

def reverseVowels(s):
    vowels = ("aeiouAEIOU")
    left = 0
    right = len(s)-1
    arr_s = list(s)

    while left < right:
        if s[left] not in vowels:
            left += 1
        if s[right] not in vowels:
            right -= 1
        if s[left] in vowels and s[right] in vowels:
            print("swap")
            arr_s[left], arr_s[right] = arr_s[right], arr_s[left]
            left += 1
            right -= 1
    print(f"final arr_s = {arr_s}")
    
    ans = "".join(arr_s)
    return ans


print(reverseVowels(string_example))