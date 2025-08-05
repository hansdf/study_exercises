# Leetcode 3541. Find Most Frequent Vowel and Consonant
# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:    Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
#                     Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

test_input = "successes" # expected output: 6 - The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2. The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4. 2 + 4 = 6

def maxFreqSum(s):
        vowels_set = set("aeiou")
        total_vowels = {}
        total_consonants = {}
        ans = 0

        for char in s:
            if char not in total_vowels and char in vowels_set:
                total_vowels[char] = 1
            elif char in total_vowels:
                total_vowels[char] += 1
        
        for char in s:
            if char not in total_consonants and char not in total_vowels:
                total_consonants[char] = 1
            elif char in total_consonants:
                total_consonants[char] += 1

        sorted_vowels_freq = sorted(total_vowels.items(), key=lambda x:x[1], reverse=True)
        sorted_consonants_freq = sorted(total_consonants.items(), key=lambda x:x[1], reverse=True)

        if sorted_vowels_freq and sorted_consonants_freq:
            print("both vowels and consonants if reached")
            ans = sorted_vowels_freq[0][1] + sorted_consonants_freq[0][1]
            return ans
        elif not total_consonants:
            print("no consonants in word")
            ans = sorted_vowels_freq[0][1]
            return ans
        elif not total_vowels:
            print("no vowels in word")
            ans = sorted_consonants_freq[0][1]
            return ans
        
print(maxFreqSum(test_input))