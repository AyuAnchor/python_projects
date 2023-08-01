import time

user = input("Press Enter to start the stopwatch.")
start = time.time()

user = input("Press Enter to stop the stopwatch.")
stop = time.time()

print('{:.2f} seconds'.format(stop - start))