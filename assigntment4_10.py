items = ['books','notebooks','pencil','pen','colours','phone','laptop','ipad']
print("first three items of list is ")
fItems=[value for value in items[0:3]]
print(fItems)
print("items from middle are")
mItems = [value for value in items[(len(items))//2-1:(len(items))//2+2]]
print(mItems)
print("Items from last ")
lItems = [value for value in items[-3:]]
print(lItems)

#rev
lItems.reverse()
print(lItems)
print(list(reversed(lItems)))