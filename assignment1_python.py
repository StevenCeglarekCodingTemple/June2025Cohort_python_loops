import time
import random

# Count from 10 down to 1
# number = 10
# while number >= 1:  # Fill in the condition
#     print(number)  # Fill in what to print
#     number = number - 1  # Fill in the update
# print("Finished!")

secret_number = random.randint(1, 100)

isDone = False
counter = 1
print("Program is starting.....")
while not isDone:
    print(counter)
    if counter > 10:
        print("Finished")
        isDone = True
    counter += 1
    time.sleep(1)
print("Program is done.")