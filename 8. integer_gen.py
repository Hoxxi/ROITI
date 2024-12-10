"""
Write a generator function which returns all positive integers. Print the first 5
numbers that the generator returns
"""

# def possitive_integers(num):
#     while True:
#         yield num
#         num += 1
#
# for i in range(1, 6):
#     print(next(possitive_integers(i)))

def possitive_integers():
    num = 1
    while True:
        yield num
        num += 1

int_gen = possitive_integers()
for i in range(5):
    print(next(int_gen))


"""
A generator function allows you to iterate over a sequence one at a time by using the yield keyword.

In this case we want possitive numbers, so "num = 1" initializes num to 1.
The loop will continue to generate positive integers as long as we ask for them.
And the yield statement returns the current value of num then  it pauses the function. 
The state of the function is saved, so the next time it's called, execution resumes from where it left off 
(the line after yield).

After that the function increments num by 1 for the next iteration using "num += 1".
"""