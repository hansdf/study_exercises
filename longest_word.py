# Given a string containing multiple words, return the longest word. If there are multiple words of the same length, return the first one.

teststring = "hello my name is applepineapple hans."

def find_longest_word(phrase):
    # split phrase into words list
    words_list = phrase.split(" ")
    
    # start a counter variable to store longest word so far
    largest_word = ""

    # loop through each word
    for word in words_list:

        # check if current word is bigger than the previous one, if is, store this as the new longest word
        if len(word) > len(largest_word):
            largest_word = word
    
    # after loop finished, return longest of all
    print("Largest word on the phrase is: ", largest_word)


find_longest_word(teststring)