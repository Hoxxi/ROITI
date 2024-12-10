"""
You have the list:
list1 = list(range(20))
Create a second list, list2, which has all elements from list1 which are greater
than 10.
"""

list1 = list(range(20))
list2 = list1[11:]


"""
The Range(20) function generates an inclusive sequence of numbers from 0 to 19.
After the list() function converts the sequence into a list, the slicing syntax 
allows the original list to be separated and to select a portion 
of list1 starting from index 11 to the end of the list. 
This ensures that all numbers which are less or equal to 10 are excluded. 

But if we don't know the order of the elements, this can be done with comprehension:
"""

list1 = list(range(20))
list2 = [x for x in list1 if x > 10]
print(list2)
