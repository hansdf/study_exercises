## Built-in Functions:

max(iterable) / min(iterable)
Returns the maximum or minimum value from an iterable (like a list or tuple).
Example: max([1, 3, 2]) # returns 3

abs(x)
Returns the absolute value of a number.
Example: abs(-5) # returns 5

round(number, ndigits)
Returns the number rounded to ndigits precision after the decimal point. If ndigits is omitted, rounds to the nearest integer.
Example: round(3.14159, 2) # returns 3.14

zip(*iterables)
Iterates over several iterables in parallel, aggregating elements into tuples.
Example: list(zip([1,2,3], ['a','b','c'])) # returns [(1, 'a'), (2, 'b'), (3, 'c')]

len(iterable)
Returns the number of elements in an iterable.
Example: len([1,2,3]) # returns 3

## String Methods:

isalnum()
Returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character; otherwise, False.
Example: "abc123".isalnum() # returns True

Slicing: array[::-1]
Returns a reversed copy of a list or string.
Example: "hello"[::-1] # returns "olleh"

reversed(iterable)
Returns an iterator that accesses the given iterable in reverse order. To obtain a list, wrap it with list().
Example: list(reversed([1,2,3])) # returns [3,2,1]

## List Methods

extend(iterable)
Appends all elements from the iterable to the end of the list.
Example:

lst = [1, 2]
lst.extend([3, 4])  # lst becomes [1, 2, 3, 4]

insert(index, element)
Inserts an element at the specified index, shifting subsequent elements to the right.
Example:
lst = [1, 2, 4]
lst.insert(2, 3)  # lst becomes [1, 2, 3, 4]

sorted(iterable, key=None, reverse=False)
Returns a new list containing all items from the iterable in sorted order, without modifying the original iterable.
Example: sorted([3,1,2]) # returns [1,2,3]

list.sort(key=None, reverse=False)
Sorts the list in place. This method modifies the original list and returns None.
Example:

lst = [3,1,2]
lst.sort()  # lst becomes [1,2,3]

## Operators and Other Expressions

Modulus Operator: %
Returns the remainder when dividing one number by another. Useful for checking even/odd (e.g., num % 2 == 0 means even).
Example: 7 % 3 # returns 1

## Set Operations

Creating a Set:
Use curly braces {} or the set() constructor.
Example: s = {1, 2, 3} or s = set([1,2,3])

add(element)
Adds an element to the set.
Example:
s = {1,2}
s.add(3)  # s becomes {1,2,3}

Set Intersection:
Use the & operator to find common elements between sets.
Example:
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 & s2  # returns {2, 3}

Set Union:
Use the | operator to combine all elements from both sets.
Example: s1 | s2 # returns {1,2,3,4}

Set Difference:
Use the - operator to get elements in one set that are not in another.
Example: s1 - s2 # returns {1}