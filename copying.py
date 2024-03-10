#we can copy a list using the slice function if we dont use slice then python will
# refers to the same list with diffrent variable name, And changes made in one
# will reflect in other


myFood = ['cheese cake','falafel','pizza']
friendFood = myFood[:]

print(myFood)
print(friendFood)

myFood.append('Noodles')
friendFood.append('Pasta')

print(myFood)
print(friendFood)