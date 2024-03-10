favoriteLanguages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite programming language is " +
          language.title())

print("\n*** looping through only keys in dictionary\n")   

for name in favoriteLanguages.keys():
    print(name.title())

# for name in favoriteLanguages:
#     print(name.title())
    
print("\nusing if statement\n")

friends = ['phil','sarah']
for name in favoriteLanguages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
            " your favourite language is " +
             favoriteLanguages[name].title())
        
print("\nwe can also use keys methon to check if a particular person has polled or not\n")

if 'eren' not in favoriteLanguages.keys():
    print("Eren, please vote")