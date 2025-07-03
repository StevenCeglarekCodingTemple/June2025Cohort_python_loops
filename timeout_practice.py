import time

timeout_seconds = 5  # Set timeout to 5 seconds
start_time = time.time()
counter = 1

print("Starting the timed while loop...")
while (time.time() - start_time) < timeout_seconds:
    print("Performing an operation within the loop...")
    print(counter)
    # Simulate some work or a delay
    time.sleep(1)
    counter += 1

print("While loop finished (either by timeout or other conditions).")