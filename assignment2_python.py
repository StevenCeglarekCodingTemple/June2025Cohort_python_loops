print("Password Creator")
print("================")

while True:
    password = input("Create a password: ")
    
    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters!")
        continue
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
        if char in "0123456789":
            has_number = True
            break
    
    if not has_number:
        print("Password must contain at least one number!")
        continue
    
    # If we get here, password is valid
    print("Password accepted!")
    break