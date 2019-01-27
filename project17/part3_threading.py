import threading
import time
import random


def handler_f(num):
    counter = 0

    space = []
    for j in range(3):
        s = ' ' * j * 40
        space.append(s)

    while True:
        sleep_time = random.randint(1, 4)

        print(space[num], 'counter' + str(num+1) + ':', counter, '\tsleep time:', sleep_time)
        counter += 1
        time.sleep(sleep_time)

threads = []
for i in range(3):
    thread = threading.Thread(target=handler_f, args=(i,))
    threads.append(thread)
    threads[i].start()
