import io

with open('data.bin', 'wb') as f:
    file = io.BufferedWriter(f)
    file.write(b"This is first line.\n")
    file.write(b"This is second line.\n")
    file.close()
    
with open('data.bin', 'rb') as f:
    file = io.BufferedReader(f)
    data = file.read()
    print(data)
    print(data.decode('utf-8')) # decode the bytes to string