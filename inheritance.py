"""class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print(f"The name of the employee: {self.id} is {self.name}")


class programmer(Employee):
    def show_language(self):
        print("The default language is python")


e1=Employee("jai digpal",119) #THIS IS USING ONLY CLASS FUNCTION AND SHOW DETAILS
e1.show_details()
e2=programmer("sameer",120)  #IT IS INHERITANCE OF A CLASS FUNCTION BY THIS WE CAN USE ALL PROPERTY OF CLASS EMPLOYEE AND ADD FUNCTION WITH THE HELP OF INHERITANCE
e2.show_language()

print(e1)
print(e2)"""

#INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

#SINGLE HERITANCE
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")

child = Child()
child.parent_method()  # Output: This is the parent method.
child.child_method()   # Output: This is the child method.
    
#MULTIPLE INHERITANCE
class Father:
    def father_method(self):
        print("This is the father method.")

class Mother:
    def mother_method(self):
        print("This is the mother method.")

class Child(Father, Mother):
    def child_method(self):
        print("This is the child method.")

child = Child()
child.father_method()  # Output: This is the father method.
child.mother_method()  # Output: This is the mother method.
child.child_method()   # Output: This is the child method.

#MULTILEVEL INHERITANCE 
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")

child = Child()
child.grandparent_method()  # Output: This is the grandparent method.
child.parent_method()       # Output: This is the parent method.
child.child_method()        # Output: This is the child method.

#Hierarchical Inheritance
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")

child1 = Child1()
child2 = Child2()

child1.parent_method()  # Output: This is the parent method.
child1.child1_method()  # Output: This is the child1 method.

child2.parent_method()  # Output: This is the parent method.
child2.child2_method()  # Output: This is the child2 method.

#Hybrid Inheritance
class A:
    def method_a(self):
        print("This is method A.")

class B(A):
    def method_b(self):
        print("This is method B.")

class C(A):
    def method_c(self):
        print("This is method C.")

class D(B, C):
    def method_d(self):
        print("This is method D.")

d = D()
d.method_a()  # Output: This is method A.
d.method_b()  # Output: This is method B.
d.method_c()  # Output: This is method C.
d.method_d()  # Output: This is method D.













