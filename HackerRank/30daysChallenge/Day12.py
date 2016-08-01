'''
Objective:: Today, we are delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task:: You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:
A Student class constructor, which has  parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scores.

A char calculate() method that calculates a Student object''s average and returns the grade character representative of their calculated average. 


Sample Input:: 
Heraldo Memelli 8135627
2
100 80

Sample Output::

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

'''

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
	self.lastName = lastName
	self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = scores
		
    def calculate(self):
        average = 0
        for i in self.testScores:
            average += i

        average = average / len(self.testScores)
		
        if(average >= 90):
            return 'O' # Outstanding
        elif(average >= 80):
            return 'E' # Exceeds Expectations
        elif(average >= 70):
            return 'A' # Acceptable
        elif(average >= 55):
            return 'P' # Poor
        elif(average >= 40):
            return 'D' # Dreadful
        else:
            return 'T' # Troll



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

