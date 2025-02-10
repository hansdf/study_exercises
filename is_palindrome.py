word = "ar ar a"
reversed_word_loop = ""

for char in word:
    reversed_word_loop = char + reversed_word_loop
print(f"This is the reversed word from a for loop: {reversed_word_loop}")

# print(word[::-1])   #[ start : stop : step ] - we omit the start and stop, increases steps from end to begin 

if reversed_word_loop.lower() == word.lower():
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

def two_pointing(stringtest): #two pointer tests
    slist = list(stringtest)
    start = 0
    end = len(stringtest)-1
    while start<end:
        slist[start],slist[end]=slist[end],slist[start]
        start+=1
        end-=1
    entire_word = "".join(slist)
    print(entire_word)

two_pointing(word)


