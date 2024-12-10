"""
 You have two lists:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
Write a program which prints the numbers from the two lists in pairs. Meaning, the
output should be:
1 5
2 6
3 7
4 8

"""

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

for n1, n2 in zip(list1, list2):
    print(n1, n2)

"""
The zip() function puts together iterables into a single iterable of tuples.

Each tuple contains one element from each iterable, paired together based on their index.
In this case the zip looks like:
[(1, 5), (2, 6), (3, 7), (4, 8)]

In each iteration:
n1 takes the first element of the current tuple (list1).
n2 takes the second element of the current tuple (list2).
"""


"""
If one of the lists is longer
"""

max_len = max(len(list1), len(list2))

for i in range(max_len):
    a = list1[i] if not i == len(list1) else 'None'
    b = list2[i] if not i == len(list2) else 'None'

    print(a, b)

"""
Here the code attempts to iterate through list1 and list2 up to the length of the longer list (max_len).
The range(max_len) ensures the loop runs for the length of the longer list.

At the end it prints either a number ot "None" is there are no numbers left in the list.
"""

