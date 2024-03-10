unconfirmedUser = ['alice','brian','candace']
confirmedUser = []

while unconfirmedUser:
    currentUser = unconfirmedUser.pop()
    print('varifying ' + currentUser.title())
    confirmedUser.append(currentUser)

print("the following user have been confirmed")
for user in confirmedUser:
    print(user.title())