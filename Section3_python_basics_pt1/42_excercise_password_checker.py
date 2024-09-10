username = input("Provide username? \n")
password = input("Provide password? \n")
password_count = len(password)
password_hidden = '*' * password_count

print('Hey {username}, your password {password_hidden} is {password_count} letters long'
      .format(username = username,password_hidden = password_hidden , password_count = password_count))