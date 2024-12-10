"""
You have the following string:
input = '3, 5, 7, 9, 11'
Split the input string into a:
• list of numbers.
• tuple of numbers.
"""

input = '3, 5, 7, 9, 11'

list_numbers = [int(x) for x in input.split(', ')]
tuple_numbers = tuple(list_numbers)

print(list_numbers)
print(tuple_numbers)

"""
The input contains numbers separated by commas and spaces.
The split(', ') method splits the string into a list of substrings. 
Then a comprehension is used to iterate over each substring in order to be converted to an integer.

The tuple() function takes an iterable and converts it into a tuple.
"""
