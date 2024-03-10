prompt = "Enter the topping you want on your pizza"
prompt += "\nEnter 'quit' to exit "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        print("thanks for odering")
        break
    else:
        print(topping.title() + " will be added to pizza")