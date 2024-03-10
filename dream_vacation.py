dream_vacation = {}

poll_active = True

while poll_active:
    name = input("please, enter your name: ")
    location = input("If you could visit one place in the world, where would you go:")

    dream_vacation[name] = location

    again = input("Do you want to continue the poll: (Y/N)")

    if again.lower() == 'n':
        break

for name,location in dream_vacation.items():
    print(name.title() + " would like to visit " + location.title())