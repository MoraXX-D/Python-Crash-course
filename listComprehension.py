#list comprehension allow you to generate the same list in one line of code
# A list comprehension combine the 'for' loop and the creation of of new 
# element into one line and append each new elements into one line. 

squares = [value ** 2 for value in range(1,11)]
print(squares) 

# Try Yourself

for value in range(1,21):   #4.3
    print(value)

millions = [value for value in range(1,1000001)]    #4.5
print(min(millions))
print(max(millions))
print(sum(millions))

oddNumber = [value for value in range(1,21,2)]      #4.6
print(oddNumber)

mulipleOfThree = [value for value in range(3,31,3)]     #4.7
print(mulipleOfThree)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)
