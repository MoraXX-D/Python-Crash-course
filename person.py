def build_person(first_name,last_name):
    '''returning a dictionary '''
    person = {'first' : first_name.title(),
              'second' : last_name.title()}
    return person

musician = build_person('taylor','swift')
print(musician)