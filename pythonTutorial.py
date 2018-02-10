#!/usr/bin/python

#Welcome to the OOP tutorial!
#3 main concepts
#encapsulation (data hiding)
#inheritance
#polymorphism

#Lesson1 encapsulation private members. Very useful in OOP
class Parent:

    #Sometimes variables might be declared like this. This can be directly accessed by the dot operator.
    notHiddenVariable = 1

    #This is a constructor called on instantiation of the object.
    # It must always have the self parameter which is a reference to itself.
    def __init__(self, hiddenValue):
        #This is setting a private member variable to the paramter passed in on object creation.
        self.__hiddenVariable = hiddenValue


    def getHiddenVariable(self):
        return self.__hiddenVariable

    def setHiddenVariable(self,newValue):
        self.__hiddenVariable = newValue

    def doACalc(self):
        return self.notHiddenVariable + 12


#In python there is no main you just begin scripting. All functions and classes are reliant on indentation.
#Lets create an instance of a parent object! It will start with __hiddenVariable = 3
p = Parent(3)



#This will work because this member variable is not private
print(p.notHiddenVariable)

#This will not work because this member variable IS private (indicated by two underscores). #Try uncommenting this.
#print(p.__hiddenVariable)

#we can get the variable using our get method
print(p.getHiddenVariable())

#lets change the private member variable
p.setHiddenVariable(5)
print(p.getHiddenVariable())

#Lets define a subclass of Parent!
class Child(Parent):

    notHiddenVariable =3
    def __init__(self,hiddenValue):
        #This line is tricky. Child is a subclass of parent.
        #So technically this object is also an instance of a parent object and calls its constructor.
        super(Child,self).__init__(hiddenValue-1)

        self.__hiddenVariable = hiddenValue

    def revealChildHiddenVariable(self):
        return self.__hiddenVariable

    def doACalc(self):
        return self.notHiddenVariable +3

c = Child(5)

#These variables will not be the same because hidden variable was private so it was not inherited.
#The notHiddenVariable will be overided because it was not private.
print(c.getHiddenVariable())
print(c.revealChildHiddenVariable())

#Examples of method overrideing Since c is instance of child it calls child method.
print(c.doACalc())