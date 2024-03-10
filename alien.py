alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0   #adding key-value pair in a dictionary
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'Blue' # changing values in a dictionary 

print(alien_0)  

del alien_0['point']    # permanently remove a key-value pair from a dictionary

print(alien_0)  
