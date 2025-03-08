import threading
import time

def counter (name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"{name}: {i}")


thread1 = threading.Thread(target=counter, args=("Counter 1", 1))
thread2 = threading.Thread(target=counter, args=("Counter 2", 2))
thread3 = threading.Thread(target=counter, args=("Counter 1", 0.5))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()