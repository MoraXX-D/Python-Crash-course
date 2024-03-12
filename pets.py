pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

def describe_pet(pet_type, pet_name):
    print("I have a " + pet_type.title())
    print("My " + pet_type.title() + "'s name is " + pet_name.title())
          
    
describe_pet('Dog','oat meal')