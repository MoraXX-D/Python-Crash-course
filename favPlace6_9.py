favoritePlace = {
    'shashwat' : ['mumbai','ladhak','nepal'],
    'shashi' : ['banglore','noida','japan'],
    'eren' : ['vietnam','japan','australia']
}

for name, places in favoritePlace.items():
    print(name.title() + "favorite places are :")
    for place in places:
        print('\t\t\t\t'+place)
    
    print('\n')