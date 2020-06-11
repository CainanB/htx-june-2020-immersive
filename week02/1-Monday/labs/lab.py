

# # 1. Create an empty class called "Student"

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"Initilaized {self.name} object")
#     def greeting(self, name):
#         return f"Good morning {name}"

# jake = Student("jake")
# joe = Student("joe")
# cainan = Student("cainan")
# steve = Student("steve")
# jeremy = Student("jeremy")


# print(jake.greeting("jake"))
# joe.greeting("joe")
# cainan.greeting("cainan")
# steve.greeting("steve")
# jeremy.greeting("jeremy")
# #2. Create 5 students objects (instances of the class "Student") of "Student" types
# class Person:
#     def __init__(self, name, Lname, birthdate, address, phone, email):
#         self.name = name
#         self.Lname = Lname
#         self.birthdate = birthdate
#         self.address = address
#         self.phone = phone
#         self.email = email

#         print("Initialized")
#     def printName(self):
#         print(f"Hello {self.name} {self.Lname}")

#     def printDetails():
#         print("Details")

# # class MyClass:
# #     def SayHello():
# #         print("hello there")
# cainan = Person("Cainan", "Mathias", "1/1/2020", "123 fake st", "123-456-7890", "Cainan@email.com")
# print(cainan.name)
# cainan.printName()
# Person.printDetails()
#3a. Create a "greeting" method inside of the class "Student" class that 
# takes as a parameter "name". The return of the  method should be
# "Good morning {name}" 


#4. Call the greet  method on each of the students in # 5 passing in a different
# name argument each time.

#5a. Create a constructor for the Student class. 
#5b. Create a print statement inside of the constructor
#5c. Run your lab.py again and you should see a print statement for each student object 
# That you created 


#6a. Pass in "name" as a parameter to your Student constructor. 
#6b. Create an instance variable for name
#6c. Refactor your greeting method by removing the name parameter and 
# adding a "self" in front of the printed "name" variable in the return statement 
#6d. Refactor your Student objects by passing in the name as an argument when the
# object gets instantiated 

#7. Class Methods
#7a. Create a "Class" method inside of the "Student" called "campus" that returns the 
# Statement "Digital Crafts - Houston"
# Campus is a "Class" method so it should not have "self" as an argument. 
#7b. call the campus method by invoking Student.campus()
#7c. Call the campus method on each of the student objects 
#7d. Return the name of the student in the campus method (instance variable) (you should
# get an error)

#8. Class Variables 
#8a. Create a class variable inside of the Student class called "cohort" whose value is
# "June 2020 Cohort"
#8b. Print to the console each class variable for each of the student objects, i.e. 
# Michah.cohort 
#8c. Refactor your class method to print out the class variable when it is called 
#8d. Call the class method on the class (i.e. Student.campus())
#8e. Call the class method on each object (i.e. Dan.campus())

#9. Accessor Modifiers 
# Refactor your constructor to take a parameter for studentID
#9a. Create a new instance variable for studentID with the value _studentID
# Refactor the student objects to pass a studentID argument
#9b. Print the studentID value to the console
# Change the value of studentID to __studentID 
# Print the value to the console (you should get an error)


#. Inheritance 
# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#     def CarDetails(self):
#         print(f"Here are the details of this car {self.make}, {self.model}, {self.color}")

# class Hybrid(Car):
#     def __init__(self, make, model, color):
#         print("hybrid car")
#         super(Hybrid, self).__init__(make, model, color)
#     def car_type(self):
#         print("I am a hybrid car")
# class Electric(Car):
#     def __init__(self, make, model, color):
#         print("Electric Car")
#         super(Electric, self).__init__(make, model, color)
#     def car_type(self):
#         print("I am an electric car")

# # mustang = Car()
# hCar = Hybrid("Toyota", "Camry", "Silver")
# eCar = Electric("Tesla", "Model S", "Blue")
# hCar.car_type()
# eCar.car_type()
# hCar.CarDetails()
# eCar.CarDetails()

# Create a new class called Car with the following method :
# CarDetails which prints "Here are details of this car"

# Create a new class called Hybrid that inherits from the Car class
#  with the following method: CarType which prints "I am a hybrid car" 


# Create a new class called Electric that inherits from the Car class
#  with the following  method: CarType which prints "I am a hybrid car" 

# Create a Hybrid instance and an Electric instance
# Call the method CarType on the Hybrid Instance and Electric Instance 
# Call the method Car Details on each instance



# Add the following instance variables to the Car class :
# - make 
# - model 
# - color








# Implicit Inheritance 

#. Override Explicitly

# Alter Before or After

# Super()

# COMPOSITION





# class Person: def __init__(self, name, email, phone):
#     self.name = name
#     self.email = email
#     self.phone = phone

#     def greet(self, other_person):
#         print(f"Hello {}, I am {}!")



# class SString(str):
#     def reverse(self, name):
#         rstring = ""
#         for char in rstring:
#             rstring = char + rstring
#         return rstring

# myString = SString("hello")

# print(myString.capitalize())
# print(myString.reverse("hello"))


# class AccountHolder:
#     def __init__(self, fname, lname, accountType, status, balance):
#         self.fname = fname
#         self.lname = lname
#         self.accountType = accountType
#         self.status = status
#         self.balance = balance

# class Bank:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.accounts = []
#     def open_new_account(self, fname, lname, accountType, status, balance):
#         temp = AccountHolder(fname, lname, accountType, status, balance)
#         self.accounts.append(temp)
#         return f"Account for {temp.fname} {temp.lname} was created with balance of {temp.balance}"
#     # def show_account_holders(self):

# Bank.open_new_account("Cainan", "Barboza", "Checking", "New", "300")

class AccountHolder :
    
    def __init__(self, fname, lname, accountType, status, balance):
        self.first_name = fname
        self.last_name = lname
        self.accountType = accountType 
        self.status = status 
        self.balance = balance


class Bank:
    def __init__(self, name, address):
        self.name = name 
        self.address = address
        self.accounts = []
        
    
    def open_new_account(self, fname, lname, accountType, status, balance):
        # Create account holder 
        temp = AccountHolder(fname, lname, accountType, status, balance)
        
        # store new account holder inside account list 
        
        self.accounts.append(temp)
        
        return f"Account for {temp.first_name} {temp.last_name} was successfully created with a balance of {temp.balance}"
    
    def show_account_holders(self):
        
        for account_holder_obj in self.accounts:
            print(f'{account_holder_obj.first_name} {account_holder_obj.last_name} {account_holder_obj.balance}')
            

def main():
    wellsfargo = Bank("wells fargo", "123 sesame street")
    action = 1
    
    while action != 6:
        print("1. Create an account")
        print("2 Print list of all account holders")
        print("6. Exit application")
        
        action = int(input("What would you like to do?"))
        
        if (action == 1):
            
            fname = input("What is the first name? ")
            lname = input("What is the last name?")
            atype = input("What would like to open? Checking or Savings")
            deposit = int(input("How much would you like to deposit?"))
            
            
            response = wellsfargo.open_new_account(fname, lname,  atype, "new", deposit)
            print(response)
        elif (action == 2):
            wellsfargo.show_account_holders()
        
        elif (action == 6):
            break

main()