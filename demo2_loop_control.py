import time

# print("Game Menu")
# print("=========")
# print("1. Start new game")
# print("2. Load saved game")
# print("3. View high score")
# print("4. Exit game")

# while True:
#     choice = input("Select option (1 - 4): ")
    
#     if choice == "1":
#         print("Starting new game....")
#         break
#     elif choice == "2":
#         print("Loading saved game....")
#         break
#     elif choice == "3":
#         print("Showing high scores....")
#         break
#     elif choice == "4":
#         print("Goodbye")
#         break
#     else:
#         print("Invalid choice! Please enter 1, 2, 3, or 4")
        
# print("Menu selection complete!")

# print("Looking for the number 7")
# counter = 1
# while counter <= 10:
#     print(f"Checking {counter}")
#     if counter == 7:
#         print("Found it!!")
#         break
#     counter += 1
#     time.sleep(1)
# print("Search Complete!")

print("Printing only odd number from 1 to 10")
counter = 0
while counter < 10:
    counter += 1
    print(counter % 2)
    if counter % 2 == 0:
        continue
    print(counter)
    # time.sleep(1)