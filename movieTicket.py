prompt = "Enter your age: "
prompt += "\nEnter 'quit' to exit\n"
active = True

while active:
    age = input(prompt)
    if age.lower() != 'quit':
        age = int(age)
        if age < 3:
            print("The ticket is free")
        
    
        elif age >= 3 and age <= 12:
            print("your ticket price is $10")
        

        else:
            print("your ticket price is $15")

    else:
        active = False
    



