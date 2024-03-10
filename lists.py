names = ['shashwat','shubham','shashi','ranjan','kumar','chaudary']
print(names[3].upper())
bikes = ['honda','yamaha','suzuki']
bikes.append('ducati')  #add element to the last of a list
print(bikes)
bikes.insert(2,'hero')
print(bikes)
del bikes[2]    #delete element from a specific location
print(bikes)
poppedBikes = bikes.pop() #pop an item from original list and can be stored in a variable
print('the last bike i owened was ' + poppedBikes)
poppedBikesAtDiffIndx = bikes.pop(0)
print("the first bike i owned was " + poppedBikesAtDiffIndx)
print(names)
names.remove('ranjan')  #remove first occurance of an element by value
print(names)
