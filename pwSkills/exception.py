try:
    with open('name/txt', 'r') as f:
        data = f.read()
        print(data)
except Exception as e:
    print("Error: unable to open file", e)
else:
    f.close()