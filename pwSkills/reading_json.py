import json
data = {
    "name": "John",
    "age": 30,
    "city": ["New York",'california','Washington'],
    "email": "john@example.com",
    "phone": "123-456-7890"
}

with open('data.json', 'w') as f:
    json.dump(data,f)
with open('data.json', 'r') as f:
    data1 =json.load(f)
    print(data1)
    print(data1['city'][2])   