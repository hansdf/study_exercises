word = "arara"
reversed_word_loop = ""

for char in word:
    reversed_word_loop = char + reversed_word_loop

print(f"This is the reversed word from a for loop: {reversed_word_loop}")

# print(word[::-1])   #[ start : stop : step ] - we omit the start and stop, increases steps from end to begin 

if reversed_word_loop.lower() == word.lower():
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


