#Slicing

# To work with a specific group of items in a list we can use slice 
# to make slice, specify the index of first and last index

players = ['charles','martina','michales','florence','eli']
print(players[0:3]) 
print(players[1:4])
print(players[:4])  #leaving the first index ,start your slice from beginning
print(players[3:])  #prints to the last index
print(players[-3:]) #prints the last 3 element of a list

print("here is the list of top 3 players of my team")

for player in players[:3]:
    print(player)