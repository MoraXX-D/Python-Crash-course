digits = list(range(1,11))  #function to create a list using list function and range
print(digits)
print(min(digits))  #prints the mimimun no in a numeric list
print(max(digits))  #prints the maximum value from a numeric list
print(sum(digits))  #prints the sum of all digit in a muneric list

list comprehension allow you to generate the same list in one line of code
A list comprehension combine the 'for' loop and the creation of of new 
element into one line and append each new elements into one line. 

squares = [value ** 2 for value in range(1,11)]
print(squares) 

tuple is an immutable list. values in a tuple cannot be change
a tuble look like a list except it uses parentheses instead of square brackets

ex dimension = (200,500)

Althoug we can not modify a tuple, we can assign a new value to a variable that hold a touple. so if we want to chane out dimension we can just re-define the entire tuple

A dicionory in python is a collection of KEY-VALUE pair. Each KEY is connected with a VoALUE, And you can access the VALUE connected to that KEY. A KEY's value can be a number, string, a list or even a dictionory

alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

we can use '*del*' keyword to delete a key-value pair from a dictionary permanently

del alien_0['point']

we can also store numbers of similar data in a dictionary by breaking them into several line.

 ex: favoriteLanguages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'ruby',
        'phil' : 'python',
        }

****** LOOPING IN A DICTIONARY *******

We can access all the value of a dictionary using a for loop, By creating two variable to store keys and values of the dictionary.
**NOTICE** : in the looping python does not tracks the orders of dictionary

*the function .items() returns a list of key-value pair of the dictionary*

user_0 = {
    'userName' : 'MoraXX-D',
    'firstName' : 'eren',
    'lastName' : 'jeager'
}

for key, value in user_0.items():
    print('\nKeys : ' + key)
    print('Values : ' + value)


*********** *LOOPING THROUGH THE KEYS IN A DICTIONARY* *****

the key() method is use when we'll have to work with the keys only

for name in favoriteLanguages.keys():
    print(name.title())

**NOTICE** : Looping through the key is the default behaviour when looping through a dictionary so we can either add .key() method or not. 
            It just enhance the code readablity 

for name in favoriteLanguages:
    print(name.title())

# *LOOPING THROUGH A DICTIONARY IN ORDER*

dictionary always maintain a clear connection between each keys & it associative value but you never the the items from dictionary in order.

One way to return the item in a certain order in to sort the keys as they are returned in the for loop.

we can use the .sorted() method to get copy of the key in order 

for name in sorted(favoriteLanguages.keys()):
    print(name.title() + " thanks for choosing " +
          favoriteLanguages[name].title())

# *LOOPING THROUGH THE VALUES IN A DICTIONARY*

We can loop through the values of a dictionary use the .value() method.

for languages in sorted(favoriteLanguages.values()):
    print(languages.title())

**NOTICE** : since the value of a dictionary can be repetative in case of a poll. so we can use set() function/method. python doesnt trace the order of set

A *set* is similar to a list in python except each items in a set must be unique

for languages in sorted(set(favoriteLanguages.values())):
    print(languages.title())

# *NESTING*

We can list into dictionary, dictionary into list and dictionary into dictionary

*list into deictionary*

favoritePlace = {
    'shashwat' : ['mumbai','ladhak','nepal'],
    'shashi' : ['banglore','noida','japan'],
    'eren' : ['vietnam','japan','australia']
}

*dictionary into list*

shashwatRaj = {
    'first_name':'Shashwat',
    'last_name':'Raj',
    'age':21,
    'city':'jaipur'
    }

shashiRanjan = {
    'first_name' : 'Shashi',
    'last_name' : 'Ranjan',
    'age' : 21,
    'city' : 'Shiroi'
}

shubhamKumar = {
    'first_name' : 'Shubham',
    'last_name' : 'Kumar',
    'age' : 20,
    'city' : 'Jaipur'
}

peoples = [shashwatRaj,shashiRanjan,shubhamKumar]

for people in peoples:
    print(people)


*dictionary into dictionary*


cities = {
    'jaipur' : {
        'country' : 'india',
        'polulation' : '42 lakh',
        'facts' : 'It is known as pink city'
    },

    'new york' : {
        'country' : 'USA',
        'population' : '85 lakh',
        'facts' : 'it is known as the city that never sleeps'
    },

    'tokyo' : {
        'country' : 'japan',
        'population' : '12.50 cr',
        'fact' : "Tokyo was previously called edo"
    }
}

# input()

we can take user input by using the input() method in python.

The input() method pauses your program and waits for user to enter some text.

The input() function take one argument: the *prompt* , or instruction

when you use input() function,Python interprets everything user enters as a string.

we can resolve this issue by using the int() function,Which tell python to treate the input as a 
numeric value.

age = input("enter your age: ")
print(age)
print(type(age))
age = int(age)
print(type(age))

# Modulo operator %

A modulo operator devide a number with another number and returns the remainder
ex: 4%3 = 1

# while loop

The *for* loop takes a collection of items and executes a block of code once for each items int the collection.
In contrast, the *while* loop runs as long as a certain condition is true.

# flag

For a program that should run only as long as many conditions are true,
we can define a variable that determine whether or not the entire program
is active. This variable is called the *flag*, act as a signal to the program.

prompt = "Tell me something, and I'll repeat it back to you : "
prompt += "\nEnter 'quit' to exit \n"

active = True 
while active:
    message = input(prompt)
    
    if message.lower() == 'quit':
        active = False

    else:
        print(message)


**break statement** --> To exit a while loop immediately without running any remaining code in the loop,
                        regardless of the result of any conditional test, use the break statement.

**continue statement**  --> The continue statement is use to return to the beginning of the loop based on the result
                            of a conditional statement

# FUNCTION

*function* are named block of code that are designed to do one specific job.
when you want to perform a particular task that you've defined in a function,
you call the name of function responsible for it.

def greetUser():
    '''Display a simple greeting'''
    print("Hello!")

greetUser()

The *def* keyword is use to inform python that you are defining a function.

The ***'''Display a simple greeting'''*** is a commented text called **docstring** 
Which describe what a function does. Docstring are enclosed in a triple quotation either
'''xyz''' or """xyz"""

To call a function, We write the name of the function, followed by any neccessary information
in parentheses.

We can pass information in function by adding a variable in the parentheses.

def greetUser(username):
    '''Display a simple greeting'''
    print("Hello! " + username.title())

greetUser('Eren')

The variable 'username' in the defination of greetUser is an example of ***parameter***,
a part of information the function needs to do its job.

The value 'Eren' in greetUser('Eren') is a example of ***argument***
An argument is a peice of information that is passed from a function call to 
a function.

A function defination can have multiple parameters, a function call may need multiple arguments.

*positional arguments* needs to be in the same order the parameters were written.

*keyword arguments* consists of a variable name and a value; list and dictionaries of values .

# positional argument
In positional arguments the argument passed in function call must follow the order of parameters
in function defination.

def describe_pet(pet_type, pet_name):
    print("I have a " + pet_type.title())
    print("My " + pet_type.title() + "'s name is " + pet_name.title())
          
    
describe_pet('Dog','oat meal')

# keyword argument
A keyword argument is a name-value pair that you pass to a function. you directly assosiate the 
name and the value within the argument, so when you pass the argument to the function, there is no 
confusion 

def describe_pet(pet_type, pet_name):
    print("I have a " + pet_type.title())
    print("My " + pet_type.title() + "'s name is " + pet_name.title())
          
    
describe_pet(pet_type = 'Dog', pet_name = 'oat meal')

*** Default values ***
when writing a function, we can define a default *value* for each parameter. 
if an argument for a parameter is provided in the function call, python uses the 
argument value. 

def describe_pet(pet_namek, pet_type = 'Dog'):
    print("I have a " + pet_type.title())
    print("My " + pet_type.title() + "'s name is " + pet_name.title())
          
    
describe_pet('oat meal')

**NOTE**
When using default value, any parameter with a default value needs to be listed after all
the parameters that dont have default values. This allow Python to continue interpretating 
positional argument correctely.


*optional argument* - we can use default value to make a argument optional 
for ex. in case of 'middle name'

*We can create a copy of list using slice method*
unprinted_model_copy = unprinted_model[:]  #copy of original list using slice

**Pass statement**
* The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


* Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

def initlog(*args):
    pass   # Remember to implement this!

**Match Statement**
A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it’s more similar to pattern matching in languages like Rust or Haskell. Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

The simplest form compares a subject value against one or more literals:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        

**Arbitary Argument**
In Python, arbitrary arguments are a special syntax that allows you to pass an unknown number of arguments to a function. This is done by using the asterisk (*) operator before the parameter name in the function definition.

def print_args(*args):
  for arg in args:
    print(arg)

print_args(1, 2, 3, 4, 5)

Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

**Unpacking Argument lists**
* The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:

list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

* In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

**Lamda function**
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression.

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)


f(0)
42
f(1)
43

**Function anotations**
* They are evaluated at the compile time not at run time. They are used by a third party or external python library.

1. Function annotation for simple parameters: we can use colons after the argument name and then we can write the expression after the colon. The expression can be anything like any data type of the argument or any string which contains any message.

def functionName(argumentName : expression): 

2. Function annotations for excess parameters:If we want an arbitrary number of arguments as function parameters with the same expression, then we can use this way of function annotation.

def fxn(*arg1: expression1,**arg2:expression2): 

3. Function annotations for the return type: Annotation of the return type is done by the '->' operator.

def fxn(var1:expression) -> expression2:  

4. Using '__annotations__':The attribute __annotations__ is used to get all the annotations in a function. It returns the dictionary, which contains the pairs of keys and values where the key will be the arguments and the value will be their individual expression.


def fibonacci(n:'int', res:'list'=[])-> 'list':  
    if n == 0:  
        return res  
    else:  
        if len(res)< 2:  
            res.append(1)  
            fibonacci(n-1, res)  
        else:  
            last = res[-1]  
            second_last = res[-2]  
            res.append(last + second_last)  
            fibonacci(n-1, res)  
        return res  
print(fibonacci(8))  
print(fibonacci.__annotations__)  

**Alias**
* If the name of the function you're importing might conflict with an existing name in your program or if the function
name is long,we can use a short ,unique alias - an alternate name similar to a nickname
ex-

from pizza import make_pizza as mp

* similarly we can rename an entire module

import pizza as p

* we can use * to import all function in module

from piza import *

****
### Classes and Objects

*  A class represent a real world thing. It is user defined data type.
* An object is a *instantiation* of class.
* A function that is a part of class is called method.
* the `__init__ ` method is a special method Python runs automatically whenever we create a new instance based on the class.
* To access the attributes of an instance, we use dot notation.
* In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() 
method; if you do this for an attribute, you don’t have to include a parameter for that attribute  

`class Car():
    def __init__(self,make,model,year) -> None:
        '''initialize attribute to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.ododmeter_reading = 0

    def get_description_name(self):
        '''return a nearly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''print a message shoing car mileage'''
        print("This car has " + str(self.ododmeter_reading) + " mileage on it")

    def update_odometer_reading(self,mileage):
        '''this function update odometer reading using a method and preventing roll back'''
        if mileage > self.ododmeter_reading:
            self.ododmeter_reading = mileage
        else:
            print("You cannot roll back the reading.")
    
```my_new_car = Car('audi','a4',2016)
print(my_new_car.get_description_name())
my_new_car.read_odometer()```

# Inheritance
* You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another 
class you wrote, you can use inheritance.
* When one class inherits from another, it automatically takes on all the attributes and methods of the first class.
*  The original class is 
called the parent class, and the new class is the child class. 
* The ***super()*** function at x is a special function that helps Python make connections between the parent and child class. 
This line tells Python to call the __init__() method from parent class, which gives an instance all the attributes of its parent class.
* You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, 
you define a method in the child class with the same name as the method you want to override in the parent class.
* Python lets you store classes in modules and then import the classes you need into your main program.
* The Python standard library is a set of modules included with every Python installation.
* You can use any function or class in the standard library by including a simple import statement at the top of your file.

```class Car():
    def __init__(self,make,model,year) -> None:
        '''initialize attribute to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.ododmeter_reading = 0

    def get_description_name(self):
        '''return a nearly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''print a message shoing car mileage'''
        print("This car has " + str(self.ododmeter_reading) + " mileage on it")

    def update_odometer_reading(self,mileage):
        '''this function update odometer reading using a method and preventing roll back'''
        if mileage > self.ododmeter_reading:
            self.ododmeter_reading = mileage
        else:
            print("You cannot roll back the reading.")

    def fill_gas_tank(self):
        '''This method show that it need gas or not'''
        print("This car need gasoline to run")

class Capacity():
    def __init__(self):
        self.capacity = 4
        self.trunk_capacity = 20

    def no_of_people(self):
        '''creating new class to show car capacity as doing so in the same class
        can make it unreadable'''
        print("This car can fit " + str(self.capacity) + " no of people")

    def trunk(self):
        '''trunk capacity of the car'''
        print('This car has a trunk capacity of ' + str(self.trunk_capacity) + ' ltr')

class ElectricCar(Car):
    '''represent aspect of car, specific to EVs'''
   
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
        self.capacity = Capacity()

    def describe_battery(self):
        '''describing battery'''
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def fill_gas_tank(self):
        '''Overridding the parent class method'''
        print("It is an electic car hence it doesn't need gas")```