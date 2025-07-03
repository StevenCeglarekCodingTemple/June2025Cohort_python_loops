# Without loops - printin numbers 1 to 5

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)


# # Counting up from 1 to 5
# # Basic counter
# print("Counting from 1 to 5")
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter = counter + 1 # counter += 1
    
# print("Done counting")

# Counting down from 5 to 1
# print("Rocket countdown")
# countdown = 5
# while countdown >= 1:
#     print(f"T-minus {countdown}")
#     countdown -= 1
# print("Blast off!")

# print("Custom Counter Program")
# print("------------------------")

# # get a starting number
# start = int(input("Enter starting number: "))
# end = int(input("Enter an ending number: "))

# # Count up or down depending on start/end
# if start <= end:
#     # Count up
#     print(f"Counting from {start} to {end}: ")
#     print("Counting from " + str(start) + " to " + str(end) + ": ")
#     current = start
#     while current <= end:
#         print(current)
#         current += 1
# else:
#     # Count down
#     print(f"Counting from {start} down to {end}")
#     current = start
#     while current >= end:
#         print(current)
#         current -= 1
        
# print("Counting Complete!!")

start = int(input("Start: "))
end = int(input("End: "))
step = int(input("Count by: "))

current = start
while current <= end:
    print(current)
    current += step