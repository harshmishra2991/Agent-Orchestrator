import threading
import time

def task(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finihed")

thread1 = threading.Thread(target=task, args=("A",2))
thread2 = threading.Thread(target=task, args=("B",1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All done. ")
