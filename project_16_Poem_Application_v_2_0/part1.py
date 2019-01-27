import time
import threading
import random
import string

sleep_random_top_limit = 6

def worker(num):
    rand_sleep = random.randint(1, sleep_random_top_limit)
    time.sleep(rand_sleep)
    print("".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 9))) +
          " with delay = " + str(rand_sleep) + " \n\twith number = " + str(num+1))
    return

def main():
    Threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, ))
        Threads.append(t)
        t.start()


if __name__ == "__main__":
    main()
