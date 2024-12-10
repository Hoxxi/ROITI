"""
Write a function power which accepts two integer arguments and has a default value
of 4 for the second argument. It should return the first argument to the power of the
second one. It should also check to make sure that each argument is an integer.
Example: power(2, 5) -> 32
"""
def power(a, b=4):
    try:
        return int(a) * int(b)
    except ValueError:
        return "Numbers should be integers!"

a = input()
b = input()

print(power(a, b))

"""
The given Python function, power, takes two arguments, a and b, and attempts to multiply them. 
If the arguments cannot be converted to integers, it raises an exception and returns the string 
"Numbers should be integers!". 
The "a" parameter is mandatory, as the "b" parameter has a default value of 4
"""



