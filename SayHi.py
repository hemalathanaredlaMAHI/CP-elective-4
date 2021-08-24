# Write a class called Dog that has two properties: name and age.
# Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi,
#  my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!
# from _typeshed import Self


class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
def sayHi(dog):
    r="my name is {} and i am {} years old!".format(dog.name,dog.age)
    return r

    

d1=Dog("abc",7)
d2=Dog("xyz",8)
print(sayHi(d1))
print(sayHi(d2))
    
