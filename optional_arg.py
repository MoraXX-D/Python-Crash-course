def get_formated_name(first_name, last_name, middle_name = ''):
    '''returning full name using optional argument'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


character_name = get_formated_name('eren','yeager')
print(character_name)

character_name = get_formated_name('shashi','chaudhary','ranjan')
print(character_name)