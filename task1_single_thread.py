import threading
import time

def display_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Create a thread
t1 = threading.Thread(target=display_numbers)

# Start the thread
t1.start()

# Wait for the thread to finish
t1.join()

print("Program completed.")