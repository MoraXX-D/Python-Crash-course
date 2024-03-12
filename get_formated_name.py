def get_formated_name(first_name, last_name):
    '''returning full name'''
    full_name = first_name + " " + last_name
    return full_name.title()
#infinite loop

while True:
    print("\nplease tell me your name ")
    print("(enter 'q' at any time to exit )")
    f_name = input('fisrt name ')
    if f_name.lower() == 'q':
        break
    l_name = input('Last name ')
    if l_name.lower() == 'q':
        break

    formatted_name = get_formated_name(f_name,l_name)
    print(formatted_name)

# character_name = get_formated_name('eren','yeager')
# print(character_name)