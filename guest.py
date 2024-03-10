guests = ['eren','mikasa','armin']
print("Hi," + guests[0].title() + " please come to the party")
print("Hi," + guests[1].title() + " please come to the party")
print("Hi," + guests[2].title() + " please come to the party")

cantCome = guests.pop(2)
print(cantCome.title() + " can not join the party due to complicacy")
guests.append('Levi')
print("Hi," + guests[0].title() + " please come to the party")
print("Hi," + guests[1].title() + " please come to the party")
print("Hi," + guests[2].title() + " please come to the party")

print("GOOD NEWS!, I found a new dinning table")
guests.insert(0,'shasha')
guests.insert(2,'ichigo')
guests.append('gojo')
print(guests)