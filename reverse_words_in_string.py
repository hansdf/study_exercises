# leetcode 151. Reverse Words in a String
# Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

s = "the sky is blue" 
# expected output: "blue is sky the"

def reverseWords(string):
    split_s = s.split()
    reversed_s = split_s[::-1]
    ans_placeholder = []
    for word in reversed_s:
        ans_placeholder.append(word)
    ans2 = " ".join(ans_placeholder)
    return ans2


print(reverseWords(s))