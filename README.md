# Python-basic
This repo will act as my personal projects built using python

Basics of python:
  -Variable:
    They can be used to store value
    Rules:
      A variable name must start with a letter or the underscore character.
      A variable name cannot start with a number.
      A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
      Variable names are case-sensitive (name, Name and NAME are three different variables).
      The reserved words(keywords) cannot be used naming the variable.
     
     
  -String:
   A string is a series of characters, surrounded by single or double quotes.
   Rules:
        A = "This is a sample of string"
        B = 'This is another sample of string
   
   
 - Lists:
   A list stores a series of items in a particular order. You access items using an index, or within a loop.
   Rules:
     Stored using []  / sample = ["A", "B", "C"]
     A single list may contain DataTypes like Integers, Strings, as well as Objects. 
     Lists are mutable, and hence, they can be altered even after their creation.
     
 
 - Tuples:
   Tuples are similar to lists, but the items in a tuple can't be modified.
   Rules:
    Tuples use parentheses ()
    Sample below:
      tup1 = ('physics', 'chemistry', 1997, 2000);
      tup2 = (1, 2, 3, 4, 5 );
      tup3 = "a", "b", "c", "d";
      
      
 - IF Statements:
   It decides whether certain statements need to be executed or not. It checks for a given condition, if the condition is true, then the set of code        present inside the ” if ” block will be executed otherwise not.
   Rules:
          If ( EXPRESSION == TRUE ):
           Block of code
      else:
           Block of code
           
   If elif else statement:
            if age < 4:
               ticket_price = 0
            elif age < 18:
               ticket_price = 10
            else:
               ticket_price = 15
               
  - User Input:
    Your programs can prompt the user for input. All input is stored as a string
    Rule:
      Python input is dynamic - default on string, it can be modified using other data types
      Code:
        name = input("What's your name? ")
        print("Hello, " + name + "!")
        
        
  - While Loops:
    A while loop repeats a block of code as long as a certain condition is true.
    Code:
      current_value = 1
      while current_value <= 5:
       print(current_value)
       current_value += 1
       
  - Functions:
     Functions are named blocks of code, designed to do one specific job. Information passed to a function is called an argument, and information              received by a function is called a parameter.
     Code:
      def greet_user():
          """Display a simple greeting."""
          print("Hello!")
      greet_user()
      
      
   - Classes:
   A class defines the behavior of an object and the kind of information an object can store. The information in a class is stored in attributes, and        functions that belong to a class are called methods. 
   A child class inherits the attributes and methods from its parent class.
   Code:
   
    class Dog():
       """Represent a dog."""
       def __init__(self, name):
         """Initialize dog object."""
         self.name = name
       def sit(self):
         """Simulate sitting."""
         print(self.name + " is sitting.")
       
    my_dog = Dog('Peso')
    print(my_dog.name + " is a great dog!")
    my_dog.sit()
