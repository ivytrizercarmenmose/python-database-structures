from main import User

myusers = User.select()
for User in myusers:
    print(User.name, User.email, User.password)
