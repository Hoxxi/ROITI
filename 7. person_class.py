"""
Write a class Person that has two properties – name and age.

Write static method compare in class Person that accepts two arguments p1 and
p2 of type Person and returns True if age in p1 is greater than age in p2.

Write a program that creates two objects of class Person. The first object should
have properties set to name = "Peter" and age = 15.

The second object should
have properties set to name = "Ivan" and age = 23.

 Call static method compare
and print the result from the comparison of the two objects
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def compare(p1, p2):
        return p1.age > p2.age



first_person = Person("Peter", 15)
second_person = Person("Ivan", 23)
print(Person.compare(first_person, second_person))

"""
The __init__ method initializes the name and age for every Person object.
The static method "compare" is defined by using the @staticmethod decorator.

It can compare the age of the p1 object and p2 and returns True if p1's age is greater than p2's age.
Respectively returns False if it isn't.
The static method is called using Person.compare(person1, person2).
"""

