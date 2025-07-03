# print("Number Guessing Game")
# print("====================")
# print("I'm thinking of a number between 1 and 100...")

# secret_number = 42
# attempts = 0
# max_attempts = 7

# while attempts < max_attempts:
#     try:
#         guess = int(input("\nEnter your guess: "))
#         attempts += 1
        
#         # Validate range
#         if guess < 1 or guess > 100:
#             print("Please guess between 1 and 100")
#             continue
        
#         # Check the guess
#         if guess < secret_number:
#             print("Too low!!")
#         elif guess > secret_number:
#             print("Too high!")
#         else:
#             print(f"Congratulations! You got it in {attempts} attempt(s)!!")
#             break
        
#         remaining = max_attempts - attempts
#         if remaining > 0:
#             print(f"You have {remaining} attempts left.")
        
#     except ValueError:
#         print("Please enter a valid number!!")
    
# if attempts >= max_attempts and guess != secret_number:
#     print(f"Sorry!! The number was {secret_number}. Better luck next time.")
    
    
print("Simple Calculator")
print("=================")

while True:
    # Show menu
    print("\nCalulator Menu: ")
    print("1. Add two numbers ")
    print("2. Subtract two numbers ")
    print("3. Multiply two numbers ")
    print("4. Divide two numbers ")
    print("5. Exit ")
    
    # Get choice
    choice = input("Choose an opperation: ")
    
    # Handle exit
    if choice == "5":
        print("Thanks for using the calculator!")
        break
    
    # Validate choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select 1-5")
        continue
    
    # Get numbers (with error handling)
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Perform calculations
    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

print("Calculator Closed!!")