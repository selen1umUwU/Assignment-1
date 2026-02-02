attempts = 0
correct_user = "python"
correct_pass = "rules"

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_user and password == correct_pass:
        print("welcome")
        break
    else:
        attempts += 1
        if attempts == 5:
            print("Access denied")
        else:
            print("Incorrect, try again.")