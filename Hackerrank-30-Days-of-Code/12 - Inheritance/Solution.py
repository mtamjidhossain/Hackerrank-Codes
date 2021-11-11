class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        s = sum(scores)/ len(scores)

        match s:                            # Structural matching - python 3.10
            case x if 90 <= s <= 100:       # can be done with if-elif as well 
                return 'O'
            case x if 80 <= s <= 90:
                return 'E'
            case x if 70 <= s <= 80:
                return 'A'
            case x if 55 <= s <= 70:
                return 'P'
            case x if 40 <= s <= 55:
                return 'D'
            case x if        s < 40:
                return 'T'


inp = 'Kathryn Hodge 8292157'

line = inp.split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = '100 90 80 75 90 88 84 88 78 67' # not needed for Python
ip = '100 80'
scores = list( map(int, ip.split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
