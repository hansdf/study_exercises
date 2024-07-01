phrase = str(input("Enter a phrase: "))

allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
miss_count = 0

for char in phrase:
    if char not in allowed_characters:
        print(f"{char} is not an allowed character")
        miss_count += 1


print(f"This phrase has {miss_count} numbers / symbols.")	