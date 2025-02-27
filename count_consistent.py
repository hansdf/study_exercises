# Leetcode 1684. Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

def count_consistent(wordlist, allow):
        counter = 0
        for word in wordlist:
                
            print(word)
        return counter

print(count_consistent(words,allowed))