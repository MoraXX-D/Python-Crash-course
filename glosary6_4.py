glosary = {'for loop' : "use for looping or repeating a set of task until requirement is met",
           'print()' : "use to print data into console",
           'list()' : 'a list is a collection of same or different kinds or elements',
           'dictionary' : "a dictionary is a data structure in python which is use to store data in form of key_value pair",
           'slice' : "slice() is a method in python which take two index value and gives a list from the sliced list and give a new list"
           }

for term, use in sorted(glosary.items()):
    print(term.upper() + 
          "-->\n" +
          use.title() + "\n")