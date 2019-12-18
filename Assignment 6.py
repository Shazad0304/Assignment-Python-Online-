#Answer 1:
    #It is approach, we map all our entities into class and make their instance
#Answer 2:
    #Code reuseablity
    #Code sharing
    #data hiding

#Answer 3:
    #Performing any action is called functaion
    #Manipulating the attribute and performing action is method, it is within the class

#Answer 4:
    #Class: A blueprint of a object
    #Object: any entity/ ussage of class
    #Attribbute: State of a object/ class variable
    #Behaviour: Methods of a class

#Answer 5:

class Car():
    def __init__(self,*specs):
        self.lis = specs
    
    def printModel(self):
        print(self.lis[0])
    def printColor(self):
        print(self.lis[1])
    def printName(self):
        print(self.lis[2])

one = Car('2001','black','civic')
three = Car('2002','grey','cultus')
two = Car('2005','white','mira')

one.printModel()
two.printColor()
three.printName()
