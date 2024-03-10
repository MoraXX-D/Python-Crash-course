# input() method
# prompt = "Tell me something, and I'll repeat it back to you : "
# prompt += "\nEnter 'quit' to exit \n"
# message = ""
# while message.title() != 'Quit':
#     message =input(prompt)
#     print(message.title())

#####################  USING FLAG VARIABLE #################

prompt = "Tell me something, and I'll repeat it back to you : "
prompt += "\nEnter 'quit' to exit \n"

active = True 
while active:
    message = input(prompt)
    
    if message.lower() == 'quit':
        active = False

    else:
        print(message)
