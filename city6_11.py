cities = {
    'jaipur' : {
        'country' : 'india',
        'polulation' : '42 lakh',
        'facts' : 'It is known as pink city'
    },

    'new york' : {
        'country' : 'USA',
        'population' : '85 lakh',
        'facts' : 'it is known as the city that never sleeps'
    },

    'tokyo' : {
        'country' : 'japan',
        'population' : '12.50 cr',
        'fact' : "Tokyo was previously called edo"
    }
}

for city in cities.keys():
    print(city)
    for info, values in cities[city].items():
        print(info + " : " + values)
    
    print("\n")