string_test = "aabcdeffff"

def letter_freq_counter(string):
    hash_counter = {}
    for letter in string_test:
        if letter not in hash_counter:
            hash_counter[letter] = 1
        else:
            hash_counter[letter] += 1
    return hash_counter

#print(letter_freq_counter(string_test))

## Find the First Non-Repeating Character
## Problem: Given a string, return the first character that appears only once.

input_test = "racecar"
def first_non_repeat(text):
    dict_counter = {}
    for letter in text:
        if letter not in dict_counter:
            dict_counter[letter] = 1
        elif letter in dict_counter:
            dict_counter[letter] += 1
    print(dict_counter)
    for key in dict_counter:
        if dict_counter[key] == 1:
            print(f"{key} is the first non-repeating character in {text}.")
            break

first_non_repeat(input_test)