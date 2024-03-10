prompt = "\n Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    else:
        print("I'd love to go to " + message.title())