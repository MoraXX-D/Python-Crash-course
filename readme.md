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

**
