import csv

data = [['name','email','phone'],
        ['John','john@example.com','123456'],
        ['Anna','anna@example.com','654321'],
        ['Peter','peter@example.com','789012'],
]
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    
    for i in data:
        writer.writerow(i)
        
with open('data.csv', 'r') as csvfile:
    read_csv = csv.reader(csvfile)
    
    for i in read_csv:
        print(i)