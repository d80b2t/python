'''
Objective:: Today, we are taking what we learned yesterday about Inheritance and extending it to Abstract Classes. Because this is a very specific Object-Oriented concept, submissions are limited to the few languages that use this construct. Check out the Tutorial tab for learning materials and an instructional video!

Task:: Given a Book class and a Solution class, write a MyBook class that does the following:
-- Inherits from Book

-- Has a parameterized constructor taking these  parameters:
   -- string title
   -- string author
   -- int price
   
Implements the Book class abstract display() method so it prints these 3 lines:
 1. Title,  a space, and then the current instances title. 
 2. Author, a space, and then the current instances author. 
 3. Price,  a space, and then the current instances price.

Note: Because these classes are being written in the same file, you
must not use an access modifier (e.g.: ) when declaring MyBook or your
code will not execute.

Input Format:: You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object. 
'''

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
