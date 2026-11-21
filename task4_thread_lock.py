import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter

for i in range(100000):
    counter += 1

# Create two threads
t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print("Final Counter:", counter)