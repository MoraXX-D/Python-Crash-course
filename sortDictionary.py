favoriteLanguages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name in sorted(favoriteLanguages.keys()):
    print(name.title() + " thanks for choosing " +
          favoriteLanguages[name].title())
    
for languages in sorted(favoriteLanguages.values()):
    print(languages.title())

print("\nusing set method\n")

for languages in sorted(set(favoriteLanguages.values())):
    print(languages.title())