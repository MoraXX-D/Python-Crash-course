car = 'subaru'
print("Is car == 'subaru'? i predict true")
print(car == 'subaru')

name = 'Shubham'
if name == 'Shubham':
    print("correct")
name = 'SHASHWAT'
if name.lower() == 'shashwat':
    print("correct")

foods = ['apple','pizza','burger']
print('apple' in foods)

if 'falafel' not in foods:
    print("Sorry! We dont have falafel")

for food in foods:
    if food == 'pizza':
        print("congratulation! We have 40% of on pizza today")