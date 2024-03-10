rivers = {
    'nile' : 'egypt',
    'indus' : 'india',
    'tigris' : 'turkey'
}

for river in rivers:
    print('The ' + river.title() +
          " flows throuh " + rivers[river].title()
          )

print('\n\n')

for river in rivers.keys():
    print(river.title())

print('\n\n')

for country in rivers.values():
    print(country.title())