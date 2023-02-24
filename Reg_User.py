from main import User

try:
    user_name = input("enter your name \n")
    user_email = input("enter your email \n")
    user_password = input("enter your password \n")

    User.create(name=user_name, email=user_email, password=user_password)
    print("User created successfully")

except:
    print("failed to create user ,use a different email")
