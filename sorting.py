cars = ['bmw','audi','mercedes','toyota','subaru']
cars.sort() #permanently sort the element of a list
print(cars)
cars.sort(reverse = True)   #permanentl sort the element of the list in reverse order
print(cars)

bikes = ['royal','ducati','suzuki','bmw','harley']
print('original list')
print(bikes)
print('sorted list\n')
print(sorted(bikes,reverse= True))    #sort the list without making changes in original list reverse = true work in this
print('original list')
print(bikes)
print("reversing the original list")
bikes.reverse() #reverse the order of the list
print(bikes)
print(len(bikes))   #print the length of a list