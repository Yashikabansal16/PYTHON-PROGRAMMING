# Defining Parent class
class Animal:
    def sound(self):
        print("Animal makes sound") # sound print

# Defining child class Dog inheriting from Animal
class Dog(Animal):
    def sound(self):
        print("Dog barks") # sound for dog 

# Defining child class Cat inheriting from Animal       
class Cat(Animal):
    def sound(self):
        print("Cat meows") # sound for Cat

# Created object of Dog class and call sound()
Dog().sound() # call overridden

# Created object of Cat class and call sound()
Cat().sound() # call overridden