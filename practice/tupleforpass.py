usernames = ('test', 'abc', 'user')
passwords = ('test123', 'abc675', 'strongpassword')

username = input("Enter username: ")
password = input("Enter password: ")

if username not in usernames:
    print("User not found")
else:
    uidx = usernames.index(username)
    correct_pass = passwords[uidx]

    if correct_pass == password:
        print("User successfully authenticated.")
    else:
        print("User is not authenticated.")