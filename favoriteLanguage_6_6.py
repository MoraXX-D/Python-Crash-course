favoriteLanguages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'c++',
    'eren' : 'python',
    'shashwat' : 'javascript'
    }

voters = ['jen','sarah','eren','shashi','dhruv','nilesh','shashwat']

for voter in voters:
    if voter not in favoriteLanguages.keys():
        print("please vote " + voter.title())

    else:
        print("Thanks for voting " + voter.title())

print('list of all the languages choosen are \n')

for language in sorted(set(favoriteLanguages.values())):
    print(language.title())

